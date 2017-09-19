import configparser

import torch

config = configparser.ConfigParser()
config.read('./config.ini')
deff = config['DEFAULT']['def_loc']
vecf = config['DEFAULT']['vec_loc']


