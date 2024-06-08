import logging
import lesson5_routes
from flask import Flask
from lesson5_container import Container
from lesson5_routes import home_route_blueprint


logging.basicConfig(level=logging.INFO,  format="%{asctime}s - %{levelname}s - %{message}s")


def create_app():
    app = Flask(__name__)
    app.register_blueprint(home_route_blueprint)
    app.container = Container()
    app.container.wire(modules=[lesson5_routes.__name__])
    return app


app = create_app()


if __name__ == "__main__":
    app.run('127.0.0.1', port=5000, debug=True)
