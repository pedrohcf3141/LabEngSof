
ENV ='prod'
if ENV == 'dev':
    DEBUG = True
    SQLALCHEMY_DATABASE_URI ='mysql+pymysql://newuser:password@localhost/receitaria'
else:
    DEBUG = False
    DATABASE_URL='postgres://xfvzhhpmjbyrpi:b9b5fc657feb67ea6a033431f17629632e7148ea9536d90452298a305cd743d0@ec2-54-243-92-68.compute-1.amazonaws.com:5432/da4c7l8pb3kae9'
    SQLALCHEMY_DATABASE_URI = DATABASE_URL.replace("://", "ql://", 1)

SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = 'receitaria'
