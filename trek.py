import cli
from app import create_app
from app.extensions import db
from app.models.models import User

app = create_app()
app.app_context().push()
cli.register(app)

@app.shell_context_processor
def make_shell_context():
    """Creates a shell context that adds the database instance and models to the shell session."""
    return {
        'db': db,
        'User': User, 
        }

if __name__ == '__main__':
    print('Running the application!')