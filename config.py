import os

class Config:
    # MySQL Configuration
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = '12345'
    MYSQL_DB = 'gestion_compras'

    # MongoDB Configuration (usando MongoDB Atlas)
    MONGO_URI = "mongodb+srv://JULIANSARAIVAN:IVANJULIANSARA@clusterbdfinal.4baix.mongodb.net/"

    # Flask Configuration
    SECRET_KEY = os.urandom(24)
