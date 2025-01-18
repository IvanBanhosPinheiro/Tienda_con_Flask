class Config:
    SECRET_KEY="3-H^fJTYrwi4hjs"


class DevelopmentConfig(Config):
    DEBUG = True
    # MYSQL_HOST = 'localhost'
    # MYSQL_DATABASE = 'tiendaflask'
    # MYSQL_USER = 'root'
    # MYSQL_PASSWORD = 'abc123.'
    

config = {
    "development" : DevelopmentConfig,
    "default" : DevelopmentConfig
}