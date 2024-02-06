class Config(object):
    def __init__(self):
        self.SECRET_KEY = 'ini sangat rahasia bro'
        self.DB_PLATFORM = "mysql+pymysql"
        self.DB_SERVER = "localhost"
        self.DB_USERNAME = "root"
        self.DB_PASSWORD = ""
        self.DB_PORT = 3306
        self.DB_NAME = "dbname"
        self.DB_URI = f"{self.DB_PLATFORM}://{self.DB_USERNAME}:{self.DB_PASSWORD}@{self.DB_SERVER}:{self.DB_PORT}/{self.DB_NAME}"
        
        
        self.SESSION_LIFETIME = 10800
        # self.DB_URI = 'mysql://root:root@localhost:3306/test1'
        #nama_sql://username:password@IP:port/nama_database