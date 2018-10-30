from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

bcrypt = Bcrypt()
db = SQLAlchemy()

class User(db.Model):
    """User for bolt"""

    __tablename__ = 'users'

    id = db.Column(
        db.Integer,
        primary_key=True,
    )

    first_name = db.Column(
        db.Text,
        nullable=False
    )

    last_name = db.Column(
        db.Text,
        nullable=False
    )

    email = db.Column(
        db.Text,
        nullable=False,
        unique=True
    )

    username = db.Column(
        db.Text,
        nullable=False,
        unique=True
    )

    image_url = db.Column(
        db.Text,
        default="/static/images/default.jpg",
    )

    bio = db.Column(
        db.Text,
    )

    password = db.Column(
        db.Text,
        nullable=False,
    )



    @classmethod
    def signup(cls, first_name, last_name, email, username, password):
        """Signs up user.

        Hashes password and adds user to system.
        """

        hashed_pwd = bcrypt.generate_password_hash(password).decode('UTF-8')

        user = User(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=username,
            password=hashed_pwd
        )

        db.session.add(user)
        return user

    @classmethod
    def authenticate(cls, username, password):
        """Find user with `username` and `password`.

        This is a class method (call it on the class, not an individual user.)
        It searches for a user whose password hash matches this password
        and, if it finds such a user, returns that user object.

        If can't find matching user (or if password is wrong), returns False.
        """

        user = cls.query.filter_by(username=username).first()

        if user:
            is_auth = bcrypt.check_password_hash(user.password, password)
            if is_auth:
                return user

        return False


class Workspace(db.Model):
    """Workspace model for bolt"""

    __tablename__ = 'workspaces'

    formatted_name = db.Column(
        db.Text,
        primary_key=True
    )

    readable_name = db.Column(
        db.Text,
        nullable=False,
        unique=True
    )





# class WorkspaceUser(db.Model):
#     """Many to many between workspaces and users"""

#     __tablename__ = 'workspaces_users'

#     workspace_formatted_name = db.Column(
#         db.Integer,
#         db.ForeignKey('workspaces.formatted_name', ondelete="cascade"),
#         primary_key = True
#     )

#     user_id = db.Column(
#         db.Integer,
#         db.ForeignKey('users.id', ondelete="cascade"),
#         primary_key = True
#     )



def connect_db(app):
    """Connect this database to provided Flask app.

    """
    
    db.app = app
    db.init_app(app)
