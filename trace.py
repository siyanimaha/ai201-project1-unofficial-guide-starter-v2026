"""Simple tracing helper for the agent loop."""

_enabled = False
_steps = []


def start():
    global _enabled, _steps
    _enabled = True
    _steps = []


def stop():
    global _enabled
    _enabled = False


def step(name, inputs=None, result=None):
    if not _enabled:
        return

    entry = {
        "step": name,
        "inputs": inputs,
        "result": result,
    }
    _steps.append(entry)

    print(f"\n[TRACE] {name}")
    if inputs is not None:
        print(f"  inputs: {inputs}")
    if result is not None:
        print(f"  result: {result}")


def get_steps():
    return list(_steps)
