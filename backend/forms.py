from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, Length


class UserAddForm(FlaskForm):
    """Form for adding users."""
    first_name = StringField("First name", validators=[DataRequired()])
    last_name = StringField("Last name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[Length(min=6)])


class UserUpdateForm(FlaskForm):
    """Form for updating users."""
    first_name = StringField("First name", validators=[DataRequired()])
    last_name = StringField("Last name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    image_url = StringField("Image URL")
    bio = StringField("Bio")


class LoginForm(FlaskForm):
    """Login form."""
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[Length(min=6)])


class WorkspaceAddUpdateForm(FlaskForm):
    """Form for adding workspaces."""

    readable_name = StringField("Readable Name", validators=[DataRequired()])


class TeamAddUpdateForm(FlaskForm):
    """Form for validating adding and updating a team."""
    name = StringField("Name", validators=[DataRequired()])

