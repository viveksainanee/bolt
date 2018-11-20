import os

from flask import Flask, render_template, request, flash, redirect, session, g, jsonify
from sqlalchemy.exc import IntegrityError
from flask_bcrypt import Bcrypt
from slugify import slugify
from SECRET import SECRET_KEY
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

bcrypt = Bcrypt()



from forms import UserAddForm, UserUpdateForm, WorkspaceAddUpdateForm, LoginForm, TeamAddUpdateForm, TaskAddForm, TaskUpdateForm, WorkspaceUserAddForm
from models import db, connect_db, User, Workspace, WorkspaceUser, Team, Task

# Import helper functions
from helpers import conv_obj_to_dict, update_obj_with_data


app = Flask(__name__)

# Get DB_URI from environ variable (useful for production/testing) or,
# if not set there, use development local db.
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
    "DATABASE_URL", "postgres:///boltv1"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = False
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
app.config["SERVER_NAME"] = "localhost.com:5000"
app.config["JWT_SECRET_KEY"] = SECRET_KEY
jwt = JWTManager(app)
connect_db(app)

#####################################################################################
# User API routes

@app.route("/login", methods=["POST"])
def login():
    """Login a user"""
    email = request.json.get('email', None)
    password = request.json.get('password', None)
    user = User.query.filter_by(email=email).first()
    if user:
        is_auth = bcrypt.check_password_hash(user.password,password)
        if is_auth:
            userData = user.to_dict()
            token = create_access_token(identity=userData['id'])
            return (jsonify({"data":{"token":token}}), 201)

@app.route("/users", methods=["GET"])
@jwt_required
def get_users():
    """Get all users"""
    users = User.query.all()
    return jsonify(
        {
            "data": [
                {
                    "id": user.id,
                    "firstName": user.first_name,
                    "lastName": user.last_name,
                    "email": user.email,
                    "imageUrl": user.image_url,
                    "bio": user.bio,
                }
                for user in users
            ]
        }
    )


@app.route("/users", methods=["POST"])
def add_user():
    """Add a user"""
    form = UserAddForm(csrf_enabled=False, data=request.json)
    try:
        if form.validate():
            first_name = form.data["first_name"]
            last_name = form.data["last_name"]
            email = form.data["email"]
            password = form.data["password"]

            user = User.signup(
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password,
            )
            db.session.add(user)
            db.session.commit()
            userData = user.to_dict()
            token = create_access_token(identity=userData['id'])
            return (jsonify({"data":{"token":token}}), 201)

        return jsonify({"errors": form.errors}), 400
    except IntegrityError as e:
        return jsonify({"errors": "Email taken"}), 400


@app.route("/users/<int:id>", methods=["GET"])
def get_user(id):
    """Get a user"""
    user = User.query.filter(User.id == id).first()
    if not user:
        return jsonify({"errors": "User not found"}), 404
    return jsonify(data=user.to_dict())


@app.route("/users/<int:id>", methods=["PATCH"])
def update_user(id):
    """Update user"""
    try:
        form = UserUpdateForm(csrf_enabled=False, data=request.json)
        if form.validate():
            user = User.query.filter(User.id == id).first()

            user.first_name = form.data["first_name"]
            user.last_name = form.data["last_name"]
            user.email = form.data["email"]
            if "image_url" in form.data:
                user.image_url = form.data["image_url"]

            if "bio" in form.data:
                user.bio = form.data["bio"]

            db.session.commit()
            return jsonify({"data": user.to_dict()})
        else:
            return jsonify({"errors": "Missing fields"}), 400

    except IntegrityError as e:
        return jsonify({"errors": "Email taken"}), 400


@app.route('/users/<int:id>', methods=["DELETE"])
def delete_user(id):
    """Delete a user"""
    user = User.query.filter(User.id == id).first()
    if(not user):
        return jsonify({'errors': 'User not found'}), 404

    db.session.delete(user)
    db.session.commit()
    return jsonify({'data': 'User deleted'})


# ##############################################################################
# # Workspace routes:

@app.route("/workspaces")
def list_workspaces():
    """API to list all workspaces

    Can take a 'q' param in querystring to search by that workspace name.
    """

    search = request.args.get("q")

    if not search:
        workspaces = Workspace.query.all()
    else:
        # TODO: make this work for case insensitive searches
        workspaces = Workspace.query.filter(
            Workspace.readable_name.like(f"%{search}%")).all()

    return jsonify(
        {
            "data": [
                {
                    "formatted_name": workspace.formatted_name,
                    "readable_name": workspace.readable_name
                }
                for workspace in workspaces
            ]
        }
    )


@app.route("/workspaces", methods=["POST"])
def add_workspace():
    """ Handle add workspace API  """
    try:
        form = WorkspaceAddUpdateForm(csrf_enabled=False, data=request.json)

        # If the form has been submitted and is valid, add the new workspace to the DB
        if form.validate_on_submit():
            new_workspace = Workspace(
                formatted_name=slugify(
                    form.data["readable_name"]
                ),
                readable_name=form.data["readable_name"],
            )
            db.session.add(new_workspace)
            db.session.commit()
            return (jsonify(data=new_workspace.to_dict()), 201)
        else:
            return jsonify({"errors": form.errors}), 400
    except IntegrityError as e:
        return jsonify({"errors": "Workspace name taken"}), 400


#need to figure out why this isn't working for new workspaces
@app.route("/", subdomain="<workspace_formatted_name>", methods=["GET"])
def get_workspace(workspace_formatted_name):
    """Get a workspace"""
    workspace = Workspace.query.filter(
        Workspace.formatted_name == workspace_formatted_name).first()
    if not workspace:
        return jsonify({"errors": "Workspace not found"}), 404
    return jsonify(data=workspace.to_dict())


# @app.route("/", subdomain="<workspace_formatted_name>", methods=["PATCH"])
# def update_workspace(workspace_formatted_name):
#     """Update workspace"""
#     try:
#         form = WorkspaceAddUpdateForm(csrf_enabled=False, data=request.json)
#         if form.validate():
#             workspace = Workspace.query.filter(Workspace.formatted_name == workspace_formatted_name).first()
#             workspace.readable_name=form.data["readable_name"]
#             workspace.formatted_name=slugify(form.data["readable_name"])
#             db.session.add(workspace)
#             db.session.commit()
#             return (jsonify(data=workspace.to_dict()), 201)
#         else:
#             return jsonify({"errors": "Missing fields"}), 400

#     except IntegrityError as e:
#         return jsonify({"errors": str(e)}), 400


@app.route("/users", subdomain="<workspace_formatted_name>", methods=["GET"])
def get_workspace_users(workspace_formatted_name):
    """Get all users for a workspace"""
    workspace_users = WorkspaceUser.query.filter(WorkspaceUser.workspace_formatted_name == workspace_formatted_name).all()
    return jsonify({"data": [conv_obj_to_dict(user) for user in workspace_users]})



@app.route("/users", subdomain="<workspace_formatted_name>", methods=["POST"])
def add_workspace_user(workspace_formatted_name):
    """Add a workspace user"""
    try:
        form = WorkspaceUserAddForm(csrf_enabled=False, data=request.json)
        if form.validate():
            workspace_formatted_name = form.data["workspace_formatted_name"]
            user_id = form.data["user_id"]
            workspace_user = WorkspaceUser(user_id=user_id, workspace_formatted_name=workspace_formatted_name)
            db.session.add(workspace_user)
            db.session.commit()
            ret_workspace_user=conv_obj_to_dict(workspace_user)
            return jsonify({"data": ret_workspace_user}), 201
        return jsonify({"errors": form.errors}), 400
    except IntegrityError as e:
        return jsonify({"errors": "Workspace User already exists"}), 400


@app.route("/users/<int:user_id>", subdomain="<workspace_formatted_name>", methods=["DELETE"])
def delete_workspace_user(workspace_formatted_name, user_id):
    """Delete a workspace_user"""
    workspace_user = WorkspaceUser.query.filter(WorkspaceUser.workspace_formatted_name == workspace_formatted_name, WorkspaceUser.user_id == user_id).first()
    if not workspace_user:
        return jsonify({"errors": "Workspace user not found"}), 404
    db.session.delete(workspace_user)
    db.session.commit()
    return jsonify({"data": "Workspace user deleted"})





#####################################################################################
# Team API routes

@app.route("/teams", subdomain="<workspace>", methods=["GET"])
def get_teams(workspace):
    """Get all teams"""
    teams = Team.query.filter(Team.workspace_name == workspace).all()
    return jsonify({"data": [conv_obj_to_dict(team) for team in teams]})


@app.route("/teams/<int:id>", subdomain="<workspace>", methods=["GET"])
def get_team(workspace, id):
    """Get a single team"""
    team = Team.query.filter(Team.workspace_name ==
                             workspace, Team.id == id).first()
    if not team:
        return jsonify({"errors": "team not found"}), 404
    return jsonify({"data": conv_obj_to_dict(team, ['name'])})


@app.route("/teams", subdomain="<workspace>", methods=["POST"])
def add_team(workspace):
    """Add a team"""
    form = TeamAddUpdateForm(csrf_enabled=False, data=request.json)
    if form.validate():
        name = form.data["name"]
        team = Team(name=name, workspace_name=workspace)
        db.session.add(team)
        db.session.commit()
        return jsonify({"data": name}), 201
    return jsonify({"errors": form.errors}), 400


@app.route("/teams/<int:id>", subdomain="<workspace>", methods=["PATCH"])
def update_team(workspace, id):
    """Update team name"""
    form = TeamAddUpdateForm(csrf_enabled=False, data=request.json)
    if form.validate():
        team = Team.query.filter(
            Team.workspace_name == workspace, Team.id == id
        ).first()
        update_obj_with_data(team, form.data)
        db.session.commit()
        return jsonify({"data": team.name})
    return jsonify({"errors": form.errors}), 400


@app.route("/teams/<int:id>", subdomain="<workspace>", methods=["DELETE"])
def delete_team(workspace, id):
    """Delete a team"""
    team = Team.query.filter(Team.workspace_name ==
                             workspace, Team.id == id).first()
    if not team:
        return jsonify({"errors": "team not found"}), 404

    db.session.delete(team)
    db.session.commit()
    return jsonify({"data": "team deleted"})


#####################################################################################
# Task API routes

@app.route("/teams/<int:id>/tasks", subdomain="<workspace>", methods=["GET"])
def get_tasks(workspace, id):
    """Get all tasks for a team"""
    team = Team.query.filter(Team.workspace_name ==
                             workspace, Team.id == id).first()
    tasks = team.tasks
    data = [conv_obj_to_dict(task) for task in tasks]
    return jsonify({"data": data})


@app.route("/teams/<int:id>/tasks/<int:task_id>", subdomain="<workspace>", methods=["GET"])
def get_task(workspace, id, task_id):
    """Get a single task"""
    task = Task.query.filter(Task.team == id, Task.id == task_id).first()
    if not task:
        return jsonify({"errors": "task not found"}), 404
    return jsonify({"data": conv_obj_to_dict(task)})


@app.route("/teams/<int:id>/tasks", subdomain="<workspace>", methods=["POST"])
def add_task(workspace, id):
    """Add a task"""
    form = TaskAddForm(csrf_enabled=False, data=request.json)
    if form.validate():
        creator_id = form.data.get('creator_id', None)
        assignee_id = form.data.get('assignee_id', None)
        title = form.data.get('title', None) 
        description = form.data.get('description', None) 
        priority = form.data.get('priority', None) 
        status = form.data.get('status', None) 
        queue = form.data.get('queue', None) 
        team = form.data.get('team', None) 

        task = Task(creator_id=creator_id,assignee_id=assignee_id,title=title,description=description,priority=priority,status=status,queue=queue,team=team)
        ret_task = conv_obj_to_dict(task)
        db.session.add(task)
        db.session.commit()
        return jsonify({"data": ret_task}), 201
    return jsonify({"errors": form.errors}), 400


@app.route("/teams/<int:id>/tasks/<int:task_id>", subdomain="<workspace>", methods=["PATCH"])
def update_task(workspace, id, task_id):
    """Update task"""
    form = TaskUpdateForm(csrf_enabled=False, data=request.json)
    if form.validate():
        task = Task.query.filter(Task.team == id, Task.id == task_id).first()
        update_obj_with_data(task, form.data)
        ret_task = conv_obj_to_dict(task)
        db.session.commit()
        return jsonify({"data": ret_task})
    return jsonify({"errors": form.errors}), 400


@app.route("/teams/<int:id>/tasks/<int:task_id>", subdomain="<workspace>", methods=["DELETE"])
def delete_task(workspace, id, task_id):
    """Delete a task"""
    task = Task.query.filter(Task.team == id, Task.id == task_id).first()
    if not task:
        return jsonify({"errors": "task not found"}), 404
    db.session.delete(task)
    db.session.commit()
    return jsonify({"data": "task deleted"})


# from flask_debugtoolbar import DebugToolbarExtension

# CURR_USER_KEY = "curr_user"
# app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "it's a secret")
# toolbar = DebugToolbarExtension(app)

# ##############################################################################
# # User getstarted/signup/login/logout


# @app.before_request
# def add_user_to_g():
#     """If we're logged in, add curr user to Flask global."""

#     if CURR_USER_KEY in session:
#         g.user = User.query.get(session[CURR_USER_KEY])

#     else:
#         g.user = None


# def do_login(user):
#     """Log in user."""

#     session[CURR_USER_KEY] = user.id


# def do_logout():
#     """Logout user."""
#     if CURR_USER_KEY in session:
#         del session[CURR_USER_KEY]


# @app.route('/get-started', methods=["GET"])
# def get_started():
#     """Handle get started page. Allows for user to search for a workspace
#     and join the correct one """
#     return render_template


# @app.route("/signup", methods=["GET", "POST"])
# def signup():
#     """Handle user signup.

#     Create new user and add to DB. Redirect to home page.

#     If form not valid, present form.

#     If the there already is a user with that username: flash message
#     and re-present form.
#     """

#     form = UserAddForm()
#     if form.validate_on_submit():
#         try:
#             username = generate_username(
#                 form.data["first_name"], form.data["last_name"]
#             )

#             user = User.signup(
#                 first_name=form.data["first_name"],
#                 last_name=form.data["last_name"],
#                 email=form.data["email"],
#                 username=username,
#                 password=form.data["password"],
#             )
#             db.session.commit()

#         except IntegrityError as e:
#             # need to also handle "Email already taken" errors
#             flash("Username already taken", "danger")
#             return render_template("users/signup.html", form=form)
#         do_login(user)

#         return redirect("/")
#     else:
#         return render_template("users/signup.html", form=form)


# @app.route("/login", methods=["GET", "POST"])
# def login():
#     """Handle user login."""

#     form = LoginForm()

#     if form.validate_on_submit():
#         user = User.authenticate(form.data["username"], form.data["password"])

#         if user:
#             do_login(user)
#             flash(f"Welcome back, {user.first_name}!", "success")
#             return redirect("/")

#         flash("Invalid credentials.", "danger")

#     return render_template("users/login.html", form=form)


# @app.route("/logout")
# def logout():
#     """Handle logout of user."""
#     do_logout()
#     flash("Logged out successfully.", "success")
#     return redirect("/login")




# @app.route('/users')
# def list_users():
#     """Page with listing of users.

#     Can take a 'q' param in querystring to search by that username.
#     """

#     search = request.args.get('q')

#     if not search:
#         users = User.query.all()
#     else:
#         users = User.query.filter(User.username.like(f"%{search}%")).all()

#     return render_template('users/index.html', users=users)
