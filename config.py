import configparser
import os

# Set some Variables from the settings.conf:
config = configparser.ConfigParser()
config.read('settings.ini')

def get_config(sys, key, as_boolean=False):
    val = config[sys][key]
    if val.startswith('ENV:'):
        var = val.removeprefix('ENV:')
        val = os.environ[var]
    if as_boolean:
        return val == 'True'
    else:
        return val
