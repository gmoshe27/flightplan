from configparser import ConfigParser

class Settings(object):
    def __init__(self, config_file):
        self.config_file = config_file
        self.api_key = ""
        self.home_address = ""
        self.work_address = ""

    def read_config(self):
        config = ConfigParser()
        config.read(self.config_file)

        self.api_key = config.get("commute", "api_key")
        self.home_address = config.get("commute", "home_address")
        self.work_address = config.get("commute", "work_address")

    def get_api_key(self):
        return self.api_key

    def get_home_address(self):
        return self.home_address.replace(" ", "+")

    def get_work_address(self):
        return self.work_address.replace(" ", "+")
