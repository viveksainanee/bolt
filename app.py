import os

from flask import Flask, render_template, request, flash, redirect, session, g, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from sqlalchemy.exc import IntegrityError

from forms import UserAddForm, WorkspaceAddForm, LoginForm
from models import db, connect_db, User, Workspace

CURR_USER_KEY = "curr_user"

app = Flask(__name__)

# Get DB_URI from environ variable (useful for production/testing) or,
# if not set there, use development local db.
app.config['SQLALCHEMY_DATABASE_URI'] = (
    os.environ.get('DATABASE_URL', 'postgres:///boltv1'))



app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', "it's a secret")
toolbar = DebugToolbarExtension(app)

connect_db(app)


##############################################################################
# User getstarted/signup/login/logout


@app.before_request
def add_user_to_g():
    """If we're logged in, add curr user to Flask global."""

    if CURR_USER_KEY in session:
        g.user = User.query.get(session[CURR_USER_KEY])

    else:
        g.user = None


def do_login(user):
    """Log in user."""

    session[CURR_USER_KEY] = user.id


def do_logout():
    """Logout user."""
    if CURR_USER_KEY in session:
        del session[CURR_USER_KEY]

# @app.route('/get-started', methods=["GET"])
# def get_started():
#     """Handle get started page. Allows for user to search for a workspace
#     and join the correct one """
#     return render_template


@app.route('/signup', methods=["GET", "POST"])
def signup():
    """Handle user signup.

    Create new user and add to DB. Redirect to home page.

    If form not valid, present form.

    If the there already is a user with that username: flash message
    and re-present form.
    """

    form = UserAddForm()
    if form.validate_on_submit():
        try:
            user = User.signup(
                first_name=form.data['first_name'],
                last_name=form.data['last_name'],
                email=form.data['email'],
                username=form.data['username'],
                password=form.data['password']
            )
            db.session.commit()

        except IntegrityError as e:
            # need to also handle "Email already taken" errors
            flash("Username already taken", 'danger')
            return render_template('users/signup.html', form=form)
        do_login(user)

        return redirect("/")
    else:
        return render_template('users/signup.html', form=form)


@app.route('/login', methods=["GET", "POST"])
def login():
    """Handle user login."""

    form = LoginForm()

    if form.validate_on_submit():
        user = User.authenticate(form.data['username'],
                                 form.data['password'])

        if user:
            do_login(user)
            flash(f"Welcome back, {user.first_name}!", "success")
            return redirect("/")

        flash("Invalid credentials.", 'danger')

    return render_template('users/login.html', form=form)


@app.route('/logout')
def logout():
    """Handle logout of user."""
    do_logout()
    flash('Logged out successfully.', 'success')
    return redirect("/login")



##############################################################################
# General user routes:


@app.route('/')
def home():
    return render_template("home.html")



@app.route('/users')
def list_users():
    """Page with listing of users.

    Can take a 'q' param in querystring to search by that username.
    """

    search = request.args.get('q')

    if not search:
        users = User.query.all()
    else:
        users = User.query.filter(User.username.like(f"%{search}%")).all()

    return render_template('users/index.html', users=users)


@app.route('/users/<int:user_id>')
def users_show(user_id):
    """Show user profile."""

    user = User.query.get_or_404(user_id)
    return render_template('users/show.html', user=user)



##############################################################################
# Workspace routes:

@app.route('/workspaces/add', methods=["GET", "POST"])
def add_workspace():
    """ Handle add workspace form

    - if form not filled out or invalid: show form
    - if valid: add playlist to SQLA and redirect to worksplaces list
    """

    form = WorkspaceAddForm()

    #If the form has been submitted and is valid, add the new workspace to the DB
    if form.validate_on_submit():
        new_workspace = Workspace(formatted_name=form.data['formatted_name'], readable_name=form.data['readable_name'])
        db.session.add(new_workspace)
        db.session.commit()
        return redirect('/workspaces')
    #Otherwise show the new workspace form
    else:
        return render_template("workspaces/add-workspace.html", form=form)

    


@app.route('/workspaces')
def list_workspaces():
    """Page with listing of workspaces.

    Can take a 'q' param in querystring to search by that workspace name.
    """

    search = request.args.get('q')

    if not search:
        workspaces = Workspace.query.all()
    else:
        workspaces = Workspace.query.filter(Workspace.name.like(f"%{search}%")).all()

    return render_template('workspaces/index.html', workspaces=workspaces)


@app.route('/<name>')
def workspace_show(name):
    """Show workspace page."""
    workspace=[]

    # workspace = Workspace.query.filter(Workspace.name==name).first()
    return render_template('workspaces/show.html', workspace=workspace)



##############################################################################
# Settings routes:


@app.route('/settings')
def settings():
    """Show settings page."""

    return render_template('/show.html', workspace=workspace)

