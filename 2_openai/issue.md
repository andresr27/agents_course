# OpenAI Agents SDK Tracing Issues: Diagnosis and Fix

## Overview

When implementing tracing in the OpenAI Agents SDK, several common pitfalls can cause runtime errors and prevent proper span export. This document summarizes the issues discovered during debugging and provides concrete solutions.

## The Problem

### Issue 1: Manual Trace Management Causes Errors

**Problematic Code:**
```python
prov = tracing.get_trace_provider()
trace_obj = prov.create_trace("Automated SDR")
if hasattr(trace_obj, "start"):
    trace_obj.start()

scope = Scope()
token = scope.set_current_trace(trace_obj)

# ... do work ...

scope.reset_current_trace(token)
prov.shutdown()
```

**Symptoms:**
- Spans created within may become `NoOpSpan` (no actual tracing)
- Potential memory leaks from improper cleanup
- Complexity in managing tokens and scope

### Issue 2: Using `prov.create_span()` Creates Malformed Spans

**Problematic Code:**
```python
span = prov.create_span("my-span")
```

**Symptoms:**
- `span_data` becomes a `str` instead of proper `SpanData` object
- Export fails with: `AttributeError: 'str' object has no attribute 'export'`
- Span cannot be properly exported to tracing backend

### Issue 3: Missing Required Parameters for Specific Span Types

**Problematic Code:**
```python
with tracing.handoff_span("agent-handoff") as handoff:
    pass
```

**Symptoms:**
- Export fails with: `Invalid type for 'span_data.to_agent': expected a string, but got null instead`
- Required fields not populated for certain span types

### Issue 4: Incorrect Data Types for Generation Spans

**Problematic Code:**
```python
with tracing.generation_span("llm-generation") as gen:
    gen.span_data.input = "User prompt"  # String instead of array
    gen.span_data.output = "Model response"  # String instead of array
```

**Symptoms:**
- Export fails with: `Invalid type for 'span_data.input': expected an array of objects, but got a string instead`
- Generation spans expect OpenAI-style message arrays

## The Solution

### Fix 1: Use the Recommended `trace()` Context Manager

Instead of manual trace management, use the built-in context manager:

```python
# CORRECT APPROACH
with tracing.trace("Automated SDR") as trace:
    print(f"Trace started: {trace.trace_id}")
    
    # All spans created here are automatically associated with this trace
    result = await Runner.run(agent, message)
    
    # Trace automatically finishes and exports when exiting context
```

**Benefits:**
- Automatic activation/deactivation
- Exception-safe cleanup
- No manual token management
- Clearer code structure

### Fix 2: Use Specific Span Functions, Not `prov.create_span()`

Instead of generic `create_span()`, use the appropriate span function for your use case:

```python
# CORRECT APPROACH
# Generic span
with tracing.custom_span("operation-name") as span:
    pass

# Function call
with tracing.function_span("function-name") as span:
    pass

# LLM generation
with tracing.generation_span("llm-generation") as span:
    span.span_data.input = [{"role": "user", "content": "Prompt"}]
    span.span_data.output = [{"role": "assistant", "content": "Response"}]
    pass

# Agent operation
with tracing.agent_span("agent-name") as span:
    pass

# Response handling
response_obj = SomeResponseClass()  # Must have .id attribute
with tracing.response_span(response_obj) as span:
    pass
```

**Available Span Functions:**
- `custom_span()` - Generic operations
- `function_span()` - Function calls
- `generation_span()` - LLM generations
- `agent_span()` - Agent operations
- `response_span()` - Responses (requires object with `.id`)
- `handoff_span()` - Agent handoffs (requires `to_agent` parameter)
- `guardrail_span()` - Safety checks

### Fix 3: Provide Required Parameters for Span Types

Always check required parameters for specific span types:

```python
# CORRECT - handoff_span requires to_agent
with tracing.handoff_span("agent-handoff", to_agent="target_agent_name") as handoff:
    pass

# CORRECT - response_span requires object with id
class Response:
    def __init__(self):
        self.id = "response_123"
        
with tracing.response_span(Response()) as rsp:
    pass
```

### Fix 4: Use Correct Data Types for Generation Spans

Generation spans expect OpenAI-style message arrays:

```python
# CORRECT - Input/output as arrays of message objects
with tracing.generation_span("chat-completion") as gen:
    gen.span_data.input = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Tell me a joke."}
    ]
    
    gen.span_data.output = [
        {"role": "assistant", "content": "Why did the chicken cross the road?"}
    ]
    
    # Optional: Add metadata
    gen.span_data.metadata = {
        "model": "gpt-4",
        "temperature": 0.7,
        "max_tokens": 100
    }
```

## Summary of Best Practices

1. **Always use `with tracing.trace()`** for trace context management
2. **Never use `prov.create_span()`** - it creates malformed spans
3. **Use specific span functions** (`custom_span`, `generation_span`, etc.)
4. **Provide all required parameters** (e.g., `to_agent` for handoff spans)
5. **Use correct data types** - arrays for generation inputs/outputs, objects with `.id` for responses
6. **Let context managers handle start/finish** - don't call `.start()` or `.finish()` manually

## Complete Working Example

```python
import agents.tracing as tracing
import asyncio

async def main():
    with tracing.trace("my-application") as trace:
        print(f"Trace started: {trace.trace_id}")
        
        # Track a function call
        with tracing.function_span("data-processing") as span:
            # Process data
            await asyncio.sleep(0.1)
        
        # Track an LLM generation
        with tracing.generation_span("llm-call") as gen:
            gen.span_data.input = [{"role": "user", "content": "Hello"}]
            gen.span_data.output = [{"role": "assistant", "content": "Hi there!"}]
            # Call your LLM
            await asyncio.sleep(0.1)
        
        # Track an agent handoff
        with tracing.handoff_span("agent-handoff", to_agent="target_agent") as handoff:
            # Perform handoff
            await asyncio.sleep(0.1)
    
    # Trace automatically exported

if __name__ == "__main__":
    asyncio.run(main())
```

By following these practices, your tracing will work reliably and produce properly structured spans that can be exported to any compatible tracing backend.