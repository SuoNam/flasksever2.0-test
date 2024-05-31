import secrets
from itsdangerous import URLSafeSerializer
Username="root"
Hostname='localhost'#123.57.28.236
port=3306
password='w29.21.28'#iBC:EY3Cegh;
database='normal_account'#app.config['']=
db_url=f"mysql+pymysql://{Username}:{password}@{Hostname}:{port}/{database}?charset=utf8"
SQLALCHEMY_DATABASE_URI=db_url

secret_key = secrets.token_hex(16)#密钥
serializer = URLSafeSerializer(secret_key)
