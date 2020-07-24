import typer
app = typer.Typer()

from . import database as db

@app.command()
def migrate():
  def get_migrations(tx):
    return tx.run("""
      MATCH (m:MIGRATION) RETURN m ORDER BY m.created_at ASC;
    """)
  
  results = db.read(get_migrations)
  typer.echo(f"{[result for result in results]}")

if __name__ == "__main__":
    app()
