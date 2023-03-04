from pyhere import here
import sys
from mangum import Mangum

sys.path.append(str(here().resolve()))

from app import app

handler = Mangum(app, lifespan="off")
