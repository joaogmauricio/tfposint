from core.database.db import SessionLocal
from core.adapters.base import UsernameAdapter
from core.database.models import Username
import uuid

class SherlockAdapter(UsernameAdapter):
    def run(self, username: str):
        session = SessionLocal()
        # mock result URLs
        urls = [f"https://twitter.com/{username}", f"https://instagram.com/{username}"]
        results = []
        for url in urls:
            u = Username(
                id=str(uuid.uuid4()),
                person_id=None,
                username=username,
                platform="sherlock",
                source_id=None
            )
            session.add(u)
            results.append({"url": url, "tool": "sherlock"})
        session.commit()
        session.close()
        return results
