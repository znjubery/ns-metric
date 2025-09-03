"""Minimal smoke test: just checks that the plugin imports cleanly."""
import importlib

mod = importlib.import_module("nerfacto_metric")
# touch the API so we fail early if it’s missing
_ = mod.get_trainer()

print("OK: plugin import")
