from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer,primary_key=True)
	screenname = db.Column(db.String(255))
	emailid = db.Column(db.String(255),unique=True)
	password = db.Column(db.String(255),unique=True)

	def __init__(self, emailid, screenname, password):
		self.screenname = screenname
		self.emailid = emailid
		self.password = password

	def __repr__(self):
		return('<User %r>' % self.screenname)


class Connection(db.Model):
	__tablename__ = 'connections'

	id = db.Column(db.Integer,primary_key=True)
	s_id = db.Column(db.String(255),unique=True)
	u_id = db.Column(db.Integer, db.ForeignKey('users.id'))

	def __init__(self, u_id, s_id):
		self.u_id = u_id
		self.s_id = s_id

	def __repr__(self):
		return('<Connection %s %s>'.format(self.s_id, self.u_id))

