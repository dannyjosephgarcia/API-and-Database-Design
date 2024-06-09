import logging
import lesson17_routes
from flask import Flask
from lesson17_container import Container
from lesson17_routes import home_route_blueprint


def create_app():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - %(levelname)s - %(message)s")
    app = Flask(__name__)
    app.register_blueprint(home_route_blueprint)
    app.container = Container()
    app.container.wire(modules=[lesson17_routes.__name__])
    return app


app = create_app()


if __name__ == "__main__":
    app.run('127.0.0.1', port=5000, debug=True)
