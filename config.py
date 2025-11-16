"""
Configuration settings for Gravity Analysis App
"""
import os
from datetime import timedelta

class Config:
    """Base configuration"""
    
    # Flask
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'gravity-analysis-secret-key-2025'
    DEBUG = False
    TESTING = False
    
    # Database
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///gravity_analysis.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Upload settings
    UPLOAD_FOLDER = 'uploads/mhtml'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB
    ALLOWED_EXTENSIONS = {'mhtml', 'mht'}
    
    # Session
    PERMANENT_SESSION_LIFETIME = timedelta(hours=24)
    
    # Microservices URLs (update these if running on different hosts)
    GRAVITY_TSE_URL = os.environ.get('GRAVITY_TSE_URL') or 'http://localhost:5001'
    TECH_ANALYSIS_URL = os.environ.get('TECH_ANALYSIS_URL') or 'http://localhost:5002'
    CODAL_SERVICE_URL = os.environ.get('CODAL_SERVICE_URL') or 'http://localhost:5003'
    FUNDAMENTAL_ANALYSIS_URL = os.environ.get('FUNDAMENTAL_ANALYSIS_URL') or 'http://localhost:5004'
    
    # Cache settings
    CACHE_TYPE = 'simple'
    CACHE_DEFAULT_TIMEOUT = 300
    
    # Pagination
    ITEMS_PER_PAGE = 20


class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True
    

class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    
    # Use PostgreSQL in production if needed
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


class TestingConfig(Config):
    """Testing configuration"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}
