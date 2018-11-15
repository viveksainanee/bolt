from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField
from wtforms.validators import DataRequired, Email, Length


class UserAddUpdateForm(FlaskForm):
    """Form for adding users."""

    first_name = StringField("First name", validators=[DataRequired()])
    last_name = StringField("Last name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[Length(min=6)])


class LoginForm(FlaskForm):
    """Login form."""

    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[Length(min=6)])


class WorkspaceAddForm(FlaskForm):
    """Form for adding workspaces."""

    readable_name = StringField("Readable Name", validators=[DataRequired()])


class TeamAddUpdateForm(FlaskForm):
    """Form for validating adding and updating a team."""

    name = StringField("Name", validators=[DataRequired()])


class TaskAddForm(FlaskForm):
    """Form for validating adding tasks"""

    creator_id = IntegerField("Creator", validators=[DataRequired()])
    assignee_id = IntegerField("Assignee")
    title = StringField("Title", validators=[DataRequired()])
    description = StringField("Description")
    priority = StringField("Priority")
    status = StringField("Status", validators=[DataRequired()])
    queue = IntegerField("Queue")
    team = IntegerField("Team", validators=[DataRequired()])


class TaskUpdateForm(FlaskForm):
    """Form for validating updating tasks"""

    creator_id = IntegerField("Creator")
    assignee_id = IntegerField("Assignee")
    title = StringField("Title")
    description = StringField("Description")
    priority = StringField("Priority")
    status = StringField("Status")
    queue = IntegerField("Queue")
    team = IntegerField("Team")
