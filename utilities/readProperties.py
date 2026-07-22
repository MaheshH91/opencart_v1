import configparser
import os

config = configparser.RawConfigParser()

config_path = os.path.join(os.getcwd(), "configurations", "config.ini")

print("Current Working Directory:", os.getcwd())
print("Config Path:", config_path)

files = config.read(config_path)

print("Files Read:", files)
print("Sections:", config.sections())


class ReadConfig:

    @staticmethod
    def getApplicationURL():
        return config.get("commanInfo", "baseURL")

    @staticmethod
    def getUserEmail():
        return config.get("commanInfo", "email")

    @staticmethod
    def getPassword():
        return config.get("commanInfo", "password")