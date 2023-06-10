from models import User

def initialise_database():
    User.create_table()


