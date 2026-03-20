import os
import time
import traceback

from agents import enable_verbose_stdout_logging, trace as trace_helper
import agents.tracing as tracing
from agents.tracing.traces import Scope

enable_verbose_stdout_logging()

print("Python:", os.sys.version)
print("OPENAI_AGENTS_TRACES:", os.environ.get("OPENAI_AGENTS_TRACES"))
print("OPENAI_API_KEY present:", bool(os.environ.get("OPENAI_API_KEY")))
print("agents version:", getattr(__import__("agents"), "__version__", None))
print("tracing module:", tracing)

prov = tracing.get_trace_provider()
print("trace provider:", prov)

def ensure_span_id(span):
    if getattr(span, "id", None) is None:
        sid = tracing.gen_span_id()
        try:
            setattr(span, "id", sid)
        except Exception:
            pass
        try:
            if hasattr(span, "span_data"):
                setattr(span.span_data, "id", sid)
                setattr(span.span_data, "span_id", sid)
        except Exception:
            pass
    return getattr(span, "id", None)

# Simple response wrapper so exporter won't crash expecting .id
class SimpleResp:
    def __init__(self, id, text):
        self.id = id
        self.text = text

def run_test_with_trace_obj(trace_obj):
    # start trace if possible
    if hasattr(trace_obj, "start"):
        try:
            trace_obj.start()
        except Exception:
            pass
    print("trace started id:", getattr(trace_obj, "trace_id", None) or getattr(trace_obj, "id", None))

    scope = Scope()
    token_trace = scope.set_current_trace(trace_obj)
    print("Set current trace:", getattr(trace_obj, "trace_id", None) or getattr(trace_obj, "id", None))

    try:
        # open a response span
        with tracing.response_span("test-response") as span:
            # ensure current span token
            token_span = scope.set_current_span(span)
            # optionally start the span
            if hasattr(span, "start"):
                try:
                    span.start()
                except Exception:
                    pass

            print("Created span object:", repr(span))
            sid = ensure_span_id(span)
            print("Span id after ensure:", sid)

            # attach a response object so exporter doesn't crash
            resp = SimpleResp("resp_test_1", "ok")
            try:
                if hasattr(span, "span_data"):
                    span.span_data.response = resp
            except Exception:
                traceback.print_exc()

            # finish if available
            if hasattr(span, "finish"):
                try:
                    span.finish()
                except Exception:
                    pass

            # reset span token
            scope.reset_current_span(token_span)

    finally:
        # reset trace token
        scope.reset_current_trace(token_trace)
        print("Reset current trace")

if __name__ == "__main__":
    # Try the high level helper first
    try:
        t = trace_helper("test-trace-helper")
        print("trace_helper returned:", repr(t), "id:", getattr(t, "id", None))
        # if the helper returned a usable trace object and it appears active, try to use it
        if getattr(t, "id", None) is not None and tracing.get_current_trace() is not None:
            print("trace helper created an active trace; using it.")
            run_test_with_trace_obj(t)
        else:
            # fallback: create a trace from the provider
            print("trace helper did not activate trace automatically; using provider.create_trace fallback")
            trace_obj = prov.create_trace("test-trace-fallback")
            run_test_with_trace_obj(trace_obj)
    except Exception as e:
        print("trace_helper attempt failed:", e)
        traceback.print_exc()
        print("Using provider.create_trace fallback")
        trace_obj = prov.create_trace("test-trace-fallback-2")
        run_test_with_trace_obj(trace_obj)

    # give the exporter a moment to run (BatchTraceProcessor may export on background thread)
    print("Sleeping briefly to allow exporter to flush...")
    time.sleep(2)

    # attempt to shutdown provider cleanly (calls exporter flush)
    try:
        prov.shutdown()
        print("Provider shutdown called")
    except Exception as e:
        print("Provider shutdown failed:", e)
        traceback.print_exc()

    print("Done. Watch for 'Exported X items' messages and check spans' IDs above.")