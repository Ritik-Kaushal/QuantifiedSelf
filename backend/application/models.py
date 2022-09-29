from database.database_config import db
from flask_security import UserMixin, RoleMixin
import datetime
class Roles_Users(db.Model):
    """
    Class that defines which user has which roles associated with himself/herself.
    """

    __tablename__ = 'roles_users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    role_id = db.Column(db.Integer,db.ForeignKey('role.id'))

class User(db.Model, UserMixin):
    """
    Class that define users.
    """

    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    email = db.Column(db.String,unique=True,nullable=False)
    password = db.Column(db.String,nullable=False)
    active = db.Column(db.Boolean())
    fs_uniquifier = db.Column(db.String,unique=True,nullable=False)
    roles = db.relationship('Role',secondary='roles_users',backref=db.backref('users'))
    trackers = db.relationship('Tracker',backref='user',cascade="all,delete")
    confirmed_at = db.Column(db.String())

class Role(db.Model,RoleMixin):
    """
    Class that define roles.
    """

    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String,unique=True)
    description = db.Column(db.String)

class TrackerType(db.Model):
    """
    Class that define the type of trackers.
    """

    __tablename__ = 'trackerType'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    tracker_type_name = db.Column(db.String, nullable = False, unique = True)

class Tracker(db.Model):
    """
    Class that define the details of trackers.
    """

    __tablename__ = 'tracker'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    tracker_name = db.Column(db.String, nullable = False)
    tracker_description = db.Column(db.String, default="-")
    tracker_type = db.Column(db.String, db.ForeignKey("trackerType.tracker_type_name"),nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"),nullable = False)
    times_edited = db.Column(db.Integer, default=0)
    last_edited = db.Column(db.String)
    reqd_values = db.Column(db.String)
    logs = db.relationship('TrackerLogs',backref='tracker',cascade="all,delete")

class TrackerLogs(db.Model):
    """
    Class that define the logs of trackers.
    """

    __tablename__ = 'trackerLogs'
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    time_stamp = db.Column(db.String, nullable = False)
    tracker_id = db.Column(db.Integer,db.ForeignKey("tracker.id"),nullable = False)
    value = db.Column(db.String, nullable = False)
    note = db.Column(db.String)
