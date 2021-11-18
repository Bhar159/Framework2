import configparser

config=configparser.RawConfigParser()
config.read("C:\\Users\\ADMIN\\PycharmProjects\\Framework2\\Configuration\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationUrl():
        url=config.get('credential','baseUrl')
        return url
    @staticmethod
    def getUsername():
        username = config.get('credential', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('credential', 'password')
        return password

    @staticmethod
    def getDRurl():
        drurl=config.get('DRLoginCred','drURL')
        return drurl
    @staticmethod
    def getdruserid():
        userid=config.get('DRLoginCred','userID')
        return userid

    @staticmethod
    def getdrpwd():
        drpwd=config.get('DRLoginCred','pwd')
        return drpwd

    @staticmethod
    def getdrupn():
        drupn=config.get('DRLoginCred','upn')
        return drupn