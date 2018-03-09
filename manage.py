
from FlaskApp.app import create_app
import os 
environment = os.environ.get('appconfig')
app = create_app(environment)


if __name__ == '__main__':
    app.run()