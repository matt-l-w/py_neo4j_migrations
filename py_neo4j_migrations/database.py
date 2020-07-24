from typing import Any, Callable
from neo4j import GraphDatabase, Session

from . import config

# encryption not on by default in neo4j 4.0
# see https://github.com/neo4j/neo4j-python-driver/issues/335#issuecomment-575706688
driver = GraphDatabase.driver(config.DATABASE_URL, auth=(config.DATABASE_USERNAME, config.DATABASE_PASSWORD), encrypted=False)

def read(func: Callable[[Any, Any], Any]):
  with driver.session() as session:
    return session.read_transaction(func)
