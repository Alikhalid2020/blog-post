import os


class Config:

    UPLOADED_PHOTOS_DEST ='app/static/photos'
    SQLALCHEMY_TRACK_MODIFICATIONS =False


    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://morninga:Alikhalid3436@localhost/blog'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    QUOTE_BASE_URL="http://quotes.stormconsultancy.co.uk/random.json"



class ProdConfig(Config):
    pass
class DevConfig(Config):
    DEBUG = True

 # email configurations
    MAIL_SERVER='smtp.gmail.com'
    MAIL_PORT=587
    MAIL_USE_TLS=True
    MAIL_USERNAME=os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD=os.environ.get("MAIL_PASSWORD")
    MAIL_USERNAME="lanrakhaled@gmail.com"

config_options = {
'development':DevConfig,
'production':ProdConfig
}