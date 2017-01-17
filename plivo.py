from flask import Flask, render_template, request, redis, random
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/meghdeepbasu'
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "account"
    id = db.Column(db.Integer, primary_key=True)
    auth_id = db.Column(db.String(40), unique=True)
    username = db.Column(db.String(30), unique=True)

class Phone(db.Model):
    __tablename__ = "phone_number"
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String(40), unique=True)
    account_id = db.Column(db.Integer, unique=True)


@app.route('/inbound/sms', methods=['POST'])

	if request.method == 'POST':
		check_auth_params();

		from_field = request.json['from'];
		to_field = request.json['to'];
		text_field = request.json['text'];

		if (from_field is not None):
			return jsonify(message='Missing Parameter', error='from is missing', status = 400)

		elif (to_field is not None):
			return jsonify(message='Missing Parameter', error='to is missing', status = 400)
		
		elif (text_field is not None):
			return jsonify(message='Missing Parameter', error='text is missing', status = 400)

		elif not db.session.query(Phone).filter(Phone.number == to_field and Phone.account_id == account.id).count():
			return jsonify(message='Invalid Parameter', error='to parameter not found', status = 400)

		else (text_field == 'STOP' or text_field == 'STOP\n' or text_field == 'STOP\r\n'):
			
			radisdb = redis.Redis('localhost')
			ttl = 14400
			random = random.getrandbits(128)

	        event['from'] = from_field
	       	event['to'] = to_field
	        event['ttl'] = ttl

	        db.delete(random)
	        db.hmset(random, event)
	        db.expire(random, ttl)
	
	else:
		return jsonify(message='Method Not Allowed', error='Invalid Method', status = 400)

@app.route('/outbound/sms', methods=['POST'])

	if request.method == 'POST':
		check_auth_params();

		from_field = request.json['from'];
		to_field = request.json['to'];
		text_field = request.json['text'];

		if (from_field is not None):
			return jsonify(message='Missing Parameter', error='from is missing', status = 400)

		elif (to_field is not None):
			return jsonify(message='Missing Parameter', error='to is missing', status = 400)
		
		elif (text_field is not None):
			return jsonify(message='Missing Parameter', error='text is missing', status = 400)

		elif not db.session.query(Phone).filter(Phone.number == to_field and Phone.account_id == account.id).count():
			return jsonify(message='Invalid Parameter', error='to parameter not found', status = 400)

		else (text_field == 'STOP' or text_field == 'STOP\n' or text_field == 'STOP\r\n')
	
	else:
		return jsonify(message='Method Not Allowed', error='Invalid Method', status = 400)

def check_auth_params():
	
	auth_id = request.headers['auth_id']
    username = request.headers['username']
	
	if not db.session.query(User).filter(User.auth_id == auth_id and User.username == username).count():
        return jsonify(message='Authentication Failed', error='Invalid Credentials', status = 403)

if __name__ == '__main__':
    app.debug = True
    app.run()