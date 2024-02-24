from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# Creating the extention database
db = SQLAlchemy()

def create_app():

    app = Flask(__name__)

    # Config settings
    app.config.from_mapping(
        DEBUG = True,
        SECRET_KEY ='dev',
        SQLALCHEMY_DATABASE_URI ='sqlite:///todolist.db'
    )

    # Initializing conexion the database
    db.init_app(app)

    # Registering the blueprint
    from . import todo
    app.register_blueprint(todo.bp)

    from . import auth
    app.register_blueprint(auth.bp)

    @app.route('/')
    def index():
        return render_template('index.html')
    
    with app.app_context():
        db.create_all()

    return app
