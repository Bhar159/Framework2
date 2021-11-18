import logging

class LogGen:
    @staticmethod
    def log():
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        handler = logging.FileHandler(filename='C:\\Users\\bhara\\PycharmProjects\\Framework\\Logs\\automation.log')
        handler.setFormatter(formatter)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        logger.addHandler(handler)
        return logger



