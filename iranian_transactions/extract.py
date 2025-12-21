from pathlib import pathlib
import pandas as pd

import logging 

logger = logger.getLogger(__name__)
logger = addHandler(logging.NullHandler())
logger.propagate = False