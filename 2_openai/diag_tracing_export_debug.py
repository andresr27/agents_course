# ultimate_tracing_test.py
import os
import time
import asyncio
from dotenv import load_dotenv
from agents import (
    Agent,
    Runner,
    set_tracing_export_api_key,
    trace,
)
import agents.tracing as tracing

load_dotenv(override=True)

print("=" * 80)
print("ULTIMATE TRACING TEST - OpenAI Platform")
print("=" * 80)

# ============================================
# STEP 1: Configure tracing
# ============================================
print("\n[STEP 1] Configuring tracing...")
openai_api_key = os.environ.get("OPENAI_API_KEY")
print(f"  OPENAI_API_KEY: {openai_api_key[:15]}..." if openai_api_key else "  OPENAI_API_KEY: NOT FOUND")

if not openai_api_key:
    print("  ❌ ERROR: OPENAI_API_KEY not found!")
    exit(1)

# Set the tracing export API key
set_tracing_export_api_key(openai_api_key)
print("  ✓ set_tracing_export_api_key() called")

# Enable verbose tracing
os.environ["OPENAI_AGENTS_TRACES"] = "1"

# ============================================
# STEP 2: Create models with LiteLLM
# ============================================
print("\n[STEP 2] Creating models with LiteLLM...")

from agents.extensions.models.litellm_model import LitellmModel

# DeepSeek model via LiteLLM
deepseek_api_key = os.getenv("DEEPSEEK_API_KEY")
if deepseek_api_key:
    deepseek_model = LitellmModel(
        model="deepseek/deepseek-chat",
        api_key=deepseek_api_key,
    )
    print("  ✓ DeepSeek model configured")
else:
    print("  ⚠ DEEPSEEK_API_KEY not found")

# ============================================
# STEP 3: Create a simple agent
# ============================================
print("\n[STEP 3] Creating simple agent...")

agent = Agent(
    name="Test Agent",
    instructions="You are a helpful assistant. Be very concise.",
    model=deepseek_model,
)

print(f"  ✓ Agent created")

# ============================================
# STEP 4: Run with trace context manager
# ============================================
print("\n[STEP 4] Running agent with trace...")

# Create a unique trace name
trace_name = f"test-trace-{int(time.time())}"
print(f"  Trace name: {trace_name}")


async def run_with_trace():
    with trace(trace_name) as t:
        print(f"  Trace ID: {t.trace_id}")
        print(f"  Trace started: {t.trace_id}")

        # Run the agent (no special run_config needed)
        print("  Running agent...")
        result = await Runner.run(agent, "Say hello in 3 words")

        print(f"  Agent response: {result.final_output}")
        return result


# Run the async function
result = asyncio.run(run_with_trace())

# ============================================
# STEP 5: Force processor flush
# ============================================
print("\n[STEP 5] Forcing trace export...")

# Get provider and shutdown to flush
prov = tracing.get_trace_provider()
print(f"  Provider: {type(prov).__name__}")

# Try to add a processor if none exists
if hasattr(prov, '_processors') and len(prov._processors) == 0:
    print("  ⚠ No processors found! Adding default processor...")
    from agents.tracing.processors import BatchTraceProcessor
    from agents.tracing.export import OpenTelemetryExporter

    # The SDK should have a default exporter
    if hasattr(tracing, 'default_exporter'):
        exporter = tracing.default_exporter()
    else:
        # Create a simple exporter
        class SimpleExporter:
            def export(self, spans):
                print(f"    Exporting {len(spans)} spans...")
                return True


        exporter = SimpleExporter()

    processor = BatchTraceProcessor(exporter=exporter)

    if hasattr(prov, 'add_processor'):
        prov.add_processor(processor)
        print("  ✓ Processor added via add_processor()")
    elif hasattr(tracing, 'add_trace_processor'):
        tracing.add_trace_processor(processor)
        print("  ✓ Processor added via add_trace_processor()")

# Shutdown to force export
if hasattr(prov, 'shutdown'):
    print("  Shutting down provider...")
    prov.shutdown()
    print("  ✓ Provider shutdown")

# ============================================
# STEP 6: Wait and verify
# ============================================
print("\n[STEP 6] Waiting for traces to export...")
for i in range(5):
    print(f"  Waiting... {i + 1}/5 seconds")
    time.sleep(1)

# ============================================
# STEP 7: Create second trace with OpenAI model
# ============================================
print("\n[STEP 7] Creating second trace with OpenAI model...")

from agents import OpenAIChatCompletionsModel
from openai import AsyncOpenAI

openai_client = AsyncOpenAI(api_key=openai_api_key)
openai_model = OpenAIChatCompletionsModel(model="gpt-4o-mini", openai_client=openai_client)

agent2 = Agent(
    name="OpenAI Test Agent",
    instructions="Be very brief",
    model=openai_model,
)

trace_name2 = f"openai-trace-{int(time.time())}"
print(f"  Trace name: {trace_name2}")


async def run_second():
    with trace(trace_name2) as t:
        print(f"  Second trace ID: {t.trace_id}")
        result = await Runner.run(agent2, "Say hi")
        print(f"  Response: {result.final_output}")


asyncio.run(run_second())

# ============================================
# STEP 8: Final flush
# ============================================
print("\n[STEP 8] Final flush...")
time.sleep(2)

prov = tracing.get_trace_provider()
if hasattr(prov, 'shutdown'):
    prov.shutdown()

# ============================================
# SUMMARY
# ============================================
print("\n" + "=" * 80)
print("TEST COMPLETE")
print("=" * 80)
print(f"\nTrace names created:")
print(f"  1. {trace_name}")
print(f"  2. {trace_name2}")
print(f"\n📊 CHECK TRACES AT: https://platform.openai.com/traces")
print("\nTroubleshooting if still not visible:")
print("  1. Make sure you're logged into the correct OpenAI account")
print("  2. Check the organization selector in top-right corner")
print("  3. Set time range filter to 'Last hour'")
print("  4. Try a different browser or incognito mode")
print("  5. Wait up to 2 minutes - sometimes there's delay")
print("\nIf still no traces, your OpenAI account may need:")
print("  - Traces feature enabled (contact OpenAI support)")
print("  - Beta access to telemetry features")
print("=" * 80)

time.sleep(2)