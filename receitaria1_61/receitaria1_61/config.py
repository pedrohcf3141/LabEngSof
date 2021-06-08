
ENV ='prod'
if ENV == 'dev':
    DEBUG = True
    SQLALCHEMY_DATABASE_URI ='mysql+pymysql://newuser:password@localhost/receitaria'
else:
    DEBUG = False
    DATABASE_URL='postgres://lmlplfveounlkm:2b5c108b51e365ee3cc4dbcf5505f6d4d09775f6d9351b616e334a072dc5f621@ec2-54-145-224-156.compute-1.amazonaws.com:5432/d1a4t79ulmm07e'
    SQLALCHEMY_DATABASE_URI = DATABASE_URL.replace("://", "ql://", 1)

SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = 'receitaria'
