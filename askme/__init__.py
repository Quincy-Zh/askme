# askme/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_uploads import UploadSet, IMAGES, configure_uploads, ALL
from config import config

db = SQLAlchemy()

def create_app(config_name):    
    app = Flask(__name__)    
    app.config.from_object(config[config_name])    
    config[config_name].init_app(app)
    db.init_app(app)    
    
    app.config['UPLOADED_PHOTO_DEST'] = 'd:/tmp'
    app.config['UPLOADED_PHOTO_ALLOW'] = IMAGES

    images = UploadSet('PHOTO')
    configure_uploads(app, images)
    
    app.config['images'] = images
    
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    return app
    