from flask import Flask
import logging
from home_route import home_route_blueprint
from container import Container
import home_route


def create_app():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - %(levelname)s - %(message)s")
    app = Flask(__name__)
    app.container = Container()
    app.register_blueprint(home_route_blueprint)
    app.container.wire(modules=[home_route.__name__])
    return app


app = create_app()


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)
