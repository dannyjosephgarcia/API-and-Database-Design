from flask import Flask
import logging


# Note that, in order to output logs in the PyCharm terminal, you cannot write logs to the log.log file
logging.basicConfig(level=logging.INFO, filename="log.log", filemode='w',
                    format="%{asctime}s - %{levelname}s - %{message}s")


# Recall that there are 5 levels of logs that can be surfaced
# logging.debug()
# logging.info()
# logging.warning()
# logging.error()
# logging.critical()

app = Flask(__name__)


@app.route("/")
def create_app():
    logging.info(f"The {create_app.__name__} route has started")
    test_string = "Hello World"
    logging.info(f"The {create_app.__name__} route has ended")
    return test_string


if __name__ == "__main__":
    app.run('127.0.0.1', port=5000, debug=True)
