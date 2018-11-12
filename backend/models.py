from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

bcrypt = Bcrypt()
db = SQLAlchemy()


class User(db.Model):
    """User for bolt"""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    first_name = db.Column(db.Text, nullable=False)

    last_name = db.Column(db.Text, nullable=False)

    email = db.Column(db.Text, nullable=False, unique=True)

    image_url = db.Column(db.Text, default="/static/images/default.jpg")

    bio = db.Column(db.Text)

    password = db.Column(db.Text, nullable=False)

    @classmethod
    def signup(cls, first_name, last_name, email, password):
        """Signs up user.

        Hashes password and adds user to system.
        """

        hashed_pwd = bcrypt.generate_password_hash(password).decode("UTF-8")

        user = User(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=hashed_pwd,
        )

        return user

    # @classmethod
    # def authenticate(cls, username, password):
    #     """Find user with `username` and `password`.

    #     This is a class method (call it on the class, not an individual user.)
    #     It searches for a user whose password hash matches this password
    #     and, if it finds such a user, returns that user object.

    #     If can't find matching user (or if password is wrong), returns False.
    #     """

    #     user = cls.query.filter_by(username=username).first()

    #     if user:
    #         is_auth = bcrypt.check_password_hash(user.password, password)
    #         if is_auth:
    #             return user

    #     return False

    def to_dict(self):
        """Serialize user to a dict of user info. does not return pw"""

        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "image_url": self.image_url,
            "bio": self.bio,
        }


class Workspace(db.Model):
    """Workspace model for bolt"""

    __tablename__ = "workspaces"

    formatted_name = db.Column(db.Text, primary_key=True)

    readable_name = db.Column(db.Text, nullable=False, unique=True)


class Team(db.Model):
    """Team model for bolt"""

    __tablename__ = "teams"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)

    name = db.Column(db.Text, nullable=False)

    workspace_name = db.Column(
        db.Text,
        db.ForeignKey("workspaces.formatted_name", ondelete="cascade"),
        nullable=False,
    )


class WorkspaceUser(db.Model):
    """Many to many between workspaces and users"""

    __tablename__ = "workspaces_users"

    workspace_formatted_name = db.Column(
        db.Text,
        db.ForeignKey("workspaces.formatted_name", ondelete="cascade"),
        primary_key=True,
    )

    user_id = db.Column(
        db.Integer, db.ForeignKey("users.id", ondelete="cascade"), primary_key=True
    )


class Segment(db.Model):
    """A team can have many segment, such as design, engineering, and pm"""

    __tablename__ = "segments"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)

    team_id = db.Column(
        db.Integer, db.ForeignKey("teams.id", ondelete="cascade"), nullable=False
    )

    name = db.Column(db.Text, nullable=False)

    lead = db.Column(
        db.Integer, db.ForeignKey("users.id", ondelete="cascade"), nullable=False
    )


class Member(db.Model):
    """A person can be a member of a segment, like Design on the spotify playlist team """

    __tablename__ = "members"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)

    role = db.Column(db.Text, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id", ondelete="cascade"))

    segment_id = db.Column(db.Integer, db.ForeignKey("segments.id", ondelete="cascade"))


def connect_db(app):
    """Connect this database to provided Flask app.

    """

    db.app = app
    db.init_app(app)
