import json
import subprocess
from pathlib import Path


def aocd_entrypoint(year, day, data):
    module_path = Path(__file__).parent / str(year) / f"{day:02d}"
    if not module_path.is_dir():
        return None, None
    tofu_proc_out = subprocess.check_output(
        ("tofu", "apply", "-auto-approve", "-json", "-var", f"puzzle_input='{data}'"),
        cwd=module_path
    )
    # stdout of tofu in json mode should be one object per line
    tofu_messages = (json.loads(line) for line in tofu_proc_out.splitlines())
    # There should be 2 messages of type outputs. One for the plan and one for
    # the apply.
    plan_out, apply_out = filter(lambda a: a["type"]=="outputs", tofu_messages)
    # Remove fluff around the output key-value pairs
    module_outputs = {name: attrs["value"] for name, attrs in apply_out["outputs"].items()}
    return module_outputs.get("solution_a"), module_outputs.get("solution_b")
