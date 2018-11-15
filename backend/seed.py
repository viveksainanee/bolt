"""Seed database with sample data from CSV Files."""

from models import db, User, Workspace, Team, WorkspaceUser, Segment, Member, Task
from flask_bcrypt import Bcrypt
from app import app

bcrypt = Bcrypt()


# Create all tables
db.create_all()

# If table are not empty, empty them
User.query.delete()
Workspace.query.delete()
Team.query.delete()
WorkspaceUser.query.delete()

# Add users
hashed_pwd = bcrypt.generate_password_hash("testtest").decode('UTF-8')
u1 = User(first_name="Jon", last_name="Snow",
          email="jsnow@winterfell.com", password=hashed_pwd)
u2 = User(first_name="Jamie", last_name="Lannister",
          email="jlannister@rock.com", password=hashed_pwd)


# Add workspaces
w1 = Workspace(formatted_name="my-first-workspace",
               readable_name="My First Workspace")
w2 = Workspace(formatted_name="spotify", readable_name="Spotify")


# Add new objects to session, so they'll persist
db.session.add(u1)
db.session.add(u2)
db.session.add(w1)
db.session.add(w2)

# Commit--otherwise, this never gets saved!
db.session.commit()

# Add teams
t1 = Team(name="playlist", workspace_name="spotify")
t2 = Team(name="formatting", workspace_name="my-first-workspace")


# Add Jon to My First Workspace
wu1 = WorkspaceUser(workspace_formatted_name="my-first-workspace",
                    user_id=u1.id)

wu2 = WorkspaceUser(workspace_formatted_name="spotify",
                    user_id=u1.id)

# Add new objects to session, so they'll persist
db.session.add(t1)
db.session.add(t2)
db.session.add(wu1)
db.session.add(wu2)

db.session.commit()

# Add tasks
task1 = Task(creator_id=u1.id, assignee_id=u2.id,
             title="Fix this", status="In Progress", team=t1.id)
task2 = Task(creator_id=u2.id, assignee_id=u1.id,
             title="Do stuff", status="Done", team=t2.id)


# Add segments to teams
s1 = Segment(team_id=t1.id, name="Design", lead=u1.id)
s2 = Segment(team_id=t1.id, name="Engineering", lead=u1.id)
s3 = Segment(team_id=t1.id, name="Product", lead=u2.id)

# Add new objects to session, so they'll persist
db.session.add(s1)
db.session.add(s2)
db.session.add(s3)
db.session.add(task1)
db.session.add(task2)

# Commit--otherwise, this never gets saved!
db.session.commit()

# Add members to teams
m1 = Member(role="Designer", user_id=u1.id, segment_id=s1.id)
m2 = Member(role="Engineer", user_id=u1.id, segment_id=s2.id)
m3 = Member(role="Product Manager", user_id=u2.id, segment_id=s3.id)

# Add new objects to session, so they'll persist
db.session.add(m1)
db.session.add(m2)
db.session.add(m3)

# Commit--otherwise, this never gets saved!
db.session.commit()
