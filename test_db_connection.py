from sqlalchemy import create_engine
from config import settings

engine = create_engine(settings.database_url)
with engine.connect() as conn:
    print("✅ Connected to the database successfully!")
