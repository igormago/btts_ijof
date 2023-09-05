from configparser import ConfigParser, ExtendedInterpolation
import os

conf = ConfigParser(interpolation=ExtendedInterpolation())
path_dir = os.path.dirname(os.path.abspath(__file__))
path_config_file = os.path.join(path_dir, 'conf.ini')
conf.read(path_config_file)

