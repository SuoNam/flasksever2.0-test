from flask import  Flask
from app.blueprint.user import user_blue
from extends import db
import config
from model import pre_exit_id

port=2849
#port=sys.argv[1]
app=Flask(__name__,template_folder='templates',static_folder='static')

app.config.from_object(config)

app.register_blueprint(user_blue)

app.secret_key = config.secret_key



db.init_app(app)
with app.app_context():
    db.create_all()






if __name__=='__main__':
    app.run(app.run(host='0.0.0.0', port=int(port),debug=True))