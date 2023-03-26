from pyhere import here
import sys
from mangum import Mangum

sys.path.append(str(here().resolve()))

from app import app

def handler(event, context):
    "custom handler to receive userid globally"
    asgi_handler = Mangum(app, lifespan="off")
    response = asgi_handler(
        event, context
    )  # Call the instance with the event arguments

    return response
