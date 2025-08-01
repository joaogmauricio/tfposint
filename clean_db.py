from core.database.models import Base
from core.database.db import engine

Base.metadata.drop_all(bind=engine)
print("Database wiped clean.")
