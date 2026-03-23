# diag_tracing_ids_final.py
import os
import time

os.environ.setdefault("OPENAI_AGENTS_TRACES", "1")

import agents.tracing as tracing

print("OPENAI_AGENTS_TRACES:", os.environ.get("OPENAI_AGENTS_TRACES"))
print("gen_trace_id():", tracing.gen_trace_id())
print("gen_span_id():", tracing.gen_span_id())

prov = tracing.get_trace_provider()
print("trace provider:", repr(prov))

# ============================================
# Method 1: Using trace() with specific span functions
# ============================================
print("\n" + "=" * 60)
print("Method 1: Using trace() with specific span functions")
print("=" * 60)

with tracing.trace("my-trace") as trace:
    print(f"Trace started: {trace.trace_id}")

    # Use custom_span for generic spans
    print("\n-- Creating a custom span --")
    with tracing.custom_span("basic-custom-span") as span:
        print(f"  Custom span created: {type(span).__name__}")
        print(f"  Span ID: {span.span_id}")
        print(f"  Span trace_id: {span.trace_id}")
        time.sleep(0.1)

    # Use function_span for function calls
    print("\n-- Creating a function span --")
    with tracing.function_span("my-function") as span:
        print(f"  Function span ID: {span.span_id}")
        time.sleep(0.1)

    # Create a response span with a proper response object
    print("\n-- Creating a response span --")


    class MockResponse:
        def __init__(self):
            self.id = "response_123"
            self.output = "This is a mock response"


    response = MockResponse()

    with tracing.response_span(response) as rsp:
        print(f"  Response span created: {type(rsp).__name__}")
        print(f"  Response span ID: {rsp.span_id}")
        print(f"  Response span_data type: {type(rsp.span_data)}")
        time.sleep(0.1)

    # Create nested spans
    print("\n-- Creating nested spans --")
    with tracing.custom_span("parent-operation") as parent:
        print(f"  Parent span ID: {parent.span_id}")

        with tracing.custom_span("child-operation-1") as child1:
            print(f"    Child 1 span ID: {child1.span_id}")
            time.sleep(0.05)

        with tracing.custom_span("child-operation-2") as child2:
            print(f"    Child 2 span ID: {child2.span_id}")
            time.sleep(0.05)

    # Create a generation span with proper input/output
    print("\n-- Creating a generation span --")
    with tracing.generation_span("llm-generation") as gen:
        print(f"  Generation span ID: {gen.span_id}")
        if hasattr(gen, 'span_data'):
            gen.span_data.input = [{"role": "user", "content": "User prompt"}]
            gen.span_data.output = [{"role": "assistant", "content": "Model response"}]
        time.sleep(0.1)

print("\nTrace completed and automatically exported")

# ============================================
# Method 2: Creating span without active trace
# ============================================
print("\n" + "=" * 60)
print("Method 2: Creating span without active trace")
print("=" * 60)

with tracing.custom_span("span-without-trace") as span:
    print(f"  Span without trace: {type(span).__name__}")
    print(f"  Is NoOpSpan? {type(span).__name__ == 'NoOpSpan'}")
    time.sleep(0.1)

# ============================================
# Method 3: Agent interaction example
# ============================================
print("\n" + "=" * 60)
print("Example: Tracing an agent interaction")
print("=" * 60)

with tracing.trace("agent-interaction") as trace:
    print(f"Trace ID: {trace.trace_id}")


    class AgentResponse:
        def __init__(self, text):
            self.id = f"resp_{hash(text)}"
            self.output = text
            self.raw_response = {"content": text}


    with tracing.custom_span("agent-processing") as processing:
        print(f"  Processing span: {processing.span_id}")

        with tracing.custom_span("tool-call") as tool_span:
            print(f"    Tool call span: {tool_span.span_id}")
            time.sleep(0.1)

        with tracing.generation_span("response-generation") as gen:
            print(f"    Generation span: {gen.span_id}")
            if hasattr(gen, 'span_data'):
                gen.span_data.input = [{"role": "user", "content": "What is the weather?"}]
                gen.span_data.output = [{"role": "assistant", "content": "The weather is sunny."}]
            time.sleep(0.05)

        response = AgentResponse("This is the agent's response")

    with tracing.response_span(response) as rsp:
        print(f"  Response span: {rsp.span_id}")
        time.sleep(0.05)

# ============================================
# Method 4: Adding metadata to spans
# ============================================
print("\n" + "=" * 60)
print("Example: Adding metadata to spans")
print("=" * 60)

with tracing.trace("attributed-trace") as trace:
    print(f"Trace ID: {trace.trace_id}")

    with tracing.custom_span("api-call") as span:
        print(f"  API call span: {span.span_id}")
        if hasattr(span, 'span_data') and hasattr(span.span_data, 'metadata'):
            span.span_data.metadata = {
                "http.method": "GET",
                "http.url": "https://api.example.com/data",
                "user.id": "user_123"
            }
        time.sleep(0.1)

    with tracing.generation_span("chat-completion") as gen:
        print(f"  Generation span: {gen.span_id}")
        gen.span_data.input = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Tell me a joke."}
        ]
        gen.span_data.output = [
            {"role": "assistant", "content": "Why did the chicken cross the road? To get to the other side!"}
        ]
        gen.span_data.metadata = {
            "model": "gpt-4",
            "temperature": 0.7,
            "max_tokens": 100
        }
        time.sleep(0.1)

# ============================================
# Method 5: Using different span types (fixed)
# ============================================
print("\n" + "=" * 60)
print("Example: Using different span types")
print("=" * 60)

with tracing.trace("span-types-demo") as trace:
    print(f"Trace ID: {trace.trace_id}")

    # Agent span
    with tracing.agent_span("my-agent") as agent_span:
        print(f"  Agent span: {agent_span.span_id}")
        time.sleep(0.05)

    # Handoff span - REQUIRES to_agent parameter
    with tracing.handoff_span("agent-handoff", to_agent="target_agent") as handoff:
        print(f"  Handoff span: {handoff.span_id}")
        time.sleep(0.05)

    # Guardrail span
    with tracing.guardrail_span("safety-check") as guardrail:
        print(f"  Guardrail span: {guardrail.span_id}")
        time.sleep(0.05)

# ============================================
# Summary of working span types
# ============================================
print("\n" + "=" * 60)
print("SUMMARY: Working span types")
print("=" * 60)
print("✓ tracing.custom_span() - Generic spans")
print("✓ tracing.function_span() - Function calls")
print("✓ tracing.generation_span() - LLM generations (requires input/output arrays)")
print("✓ tracing.response_span() - Responses (requires object with .id)")
print("✓ tracing.agent_span() - Agent operations")
print("✓ tracing.handoff_span() - Agent handoffs (requires to_agent parameter)")
print("✓ tracing.guardrail_span() - Safety checks")
print("\n❌ DO NOT USE: prov.create_span() - Creates malformed spans")
print("\n✅ ALWAYS USE: with tracing.trace() as trace: for trace context")
print("=" * 60)

# Give background thread time to export spans
time.sleep(2)

print("\nAll traces completed successfully!")