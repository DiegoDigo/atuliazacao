from configparser import ConfigParser
from infra import postgres, dbmaker

if __name__ == '__main__':
    config = ConfigParser()
    config.read(config.read('settings\config.ini'))
    postgres.select_client(dict(config['POSTGRES']))
    dbmaker.select_client(dict(config['DBMAKER']))
