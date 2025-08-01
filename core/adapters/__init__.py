import importlib
import pkgutil
from typing import List
from .base import UsernameAdapter

def get_username_adapters() -> List[UsernameAdapter]:
    adapters: List[UsernameAdapter] = []

    # 1) Look for modules in the app.adapters package
    package = importlib.import_module("core.adapters")
    prefix = package.__name__ + "."

    for finder, name, ispkg in pkgutil.iter_modules(package.__path__, prefix):
        module = importlib.import_module(name)
        # 2) Inspect module for UsernameAdapter subclasses
        for attr in dir(module):
            obj = getattr(module, attr)
            if (
                isinstance(obj, type)
                and issubclass(obj, UsernameAdapter)
                and obj is not UsernameAdapter
            ):
                adapters.append(obj())

    return adapters
