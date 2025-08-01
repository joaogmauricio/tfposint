from core.adapters.base import UsernameAdapter
from core.database.db import SessionLocal
from core.database.models import Username
import uuid

class MaigretAdapter(UsernameAdapter):
    def run(self, username: str):
        session = SessionLocal()
        # mock result URLs
        urls = [f"https://vk.com/{username}", f"https://ok.ru/{username}"]
        results = []
        for url in urls:
            u = Username(
                id=str(uuid.uuid4()),
                person_id=None,
                username=username,
                platform="maigret",
                source_id=None
            )
            session.add(u)
            results.append({"url": url, "tool": "maigret"})
        session.commit()
        session.close()
        return results
