import os
from configparser import ConfigParser

working_dir = os.path.dirname(__file__)
configuration_dir = os.path.dirname(working_dir)
configuration_path = os.path.join(configuration_dir, "reservas.ini")

parser = ConfigParser()
parser.read(configuration_path)

app = parser["app"]
api = parser["academico_api"]
persistence = parser["persistence"]

