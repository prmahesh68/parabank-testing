import logging
class Logsetup:
    @staticmethod
    def getlogreg():
        logging.basicConfig(filename=".\\Logsfolder\\registration.log",format='%(asctime)s: %(levelname)s: %(message)s %(funcName)s %(lineno)d',datefmt='%Y-%m-%d %H:%M:%S')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
    @staticmethod
    def getlogaddlogin():
        logging.basicConfig(filename=".\\Logsfolder\\login.log",format='%(asctime)s: %(levelname)s: %(message)s %(funcName)s %(lineno)d',datefmt='%Y-%m-%d %H:%M:%S')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
    @staticmethod
    def getlogshop():
        logging.basicConfig(filename=".\\Logsfolder\\shopping.log",format='%(asctime)s: %(levelname)s: %(message)s %(funcName)s %(lineno)d',datefmt='%Y-%m-%d %H:%M:%S')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger

    @staticmethod
    def getlogdemoqa():
        logging.basicConfig(filename="..\\Logsfolder\\demoqalog.log",
                            format='%(asctime)s: %(levelname)s: %(message)s %(funcName)s %(lineno)d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger

    @staticmethod
    def getlogparabank():
        logging.basicConfig(filename="Logs\\parademolog.log",
                            format='%(asctime)s: %(levelname)s: %(message)s %(funcName)s %(lineno)d',
                            datefmt='%Y-%m-%d %H:%M:%S')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger