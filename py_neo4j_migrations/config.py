import os

DATABASE_URL = os.getenv("DATABASE_URL", "bolt://localhost:7687")
DATABASE_USERNAME = os.getenv("DATABASE_USERNAME", "neo4j")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD", "password")