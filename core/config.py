import os
from dotenv import load_dotenv
from urllib.parse import urlparse

load_dotenv()

class Settings:
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///core/database/data/tfposint.db")
    API_KEYS = {
        "pimeyes": os.getenv("PIMEYES_API_KEY", ""),
    }

    def validate(self):
        parsed = urlparse(self.DATABASE_URL)
        if parsed.scheme not in ("sqlite","postgresql","mysql"):
            raise ValueError(f"Unsupported DB scheme: {parsed.scheme}")
        for name, key in self.API_KEYS.items():
            if not key:
                print(f"[WARN] API key for {name} is empty")

settings = Settings()
settings.validate()
