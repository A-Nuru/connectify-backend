from router import app
from database import initialise_database

if __name__ == '__main__':
    initialise_database()
    app.run(debug=True)
