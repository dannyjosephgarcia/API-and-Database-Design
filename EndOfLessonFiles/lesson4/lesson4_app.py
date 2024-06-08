from flask import Flask
import logging
from lesson4_routes import home_route_blueprint


# Note that, in order to output logs in the PyCharm terminal, you cannot write logs to the log.log file
logging.basicConfig(level=logging.INFO, filename="log.log", filemode='w',
                    format="%{asctime}s - %{levelname}s - %{message}s")


# Recall that there are 5 levels of logs that can be surfaced
# logging.debug()
# logging.info()
# logging.warning()
# logging.error()
# logging.critical()


def create_app():
    app = Flask(__name__)
    app.register_blueprint(home_route_blueprint)
    return app


app = create_app()


if __name__ == "__main__":
    app.run('127.0.0.1', port=5000, debug=True)