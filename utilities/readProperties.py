import configparser

config = configparser.RawConfigParser()
config.read("/home/mubashar/PycharmProjects/SeleniumScrapper/Configurations/config.ini")


class ReadConfig():
    @staticmethod
    def getAppURL():
        url = config.get('common info', 'baseURL')
        return url