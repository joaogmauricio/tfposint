from abc import ABC, abstractmethod
from typing import List, Dict

class UsernameAdapter(ABC):
    @abstractmethod
    def run(self, username: str) -> List[Dict[str, str]]:
        "Return list of dicts: {'url':..., 'tool':...}"
        ...
