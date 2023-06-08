# flaskapp
## Running the app
- Run `virtualenv myenv` to create a virtual env
- Run `myenv/Scripts\activate` to activate the virtual env
- Run `pip install flask, flask_cors, flask_sqlalchemy, flask_wtf, psycopg2` to install the dependencies

- (pipenv shell)

## Generating secret tokens
- Run `python3` on command line to start python interpreter

- Run `import secrets` to import secrets
- Run `secrets.token_hex(16)` to get secret token
