from flask.cli import FlaskGroup
from src import db, create_app
from src.api.models import User

app = create_app()
cli = FlaskGroup(create_app=create_app)

@cli.command('seed_db')
def seed_db():
    db.session.add(User(username="Jaa", email="jaa@gmail.com"))
    db.session.add(User(username="Lee", email="lee@gmail.com"))
    db.session.commit()

@cli.command('recreate_db')
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

if __name__ == "__main__":
    cli()