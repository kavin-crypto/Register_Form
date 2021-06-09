import pytest
import inspect
import logging


from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("browser")
class Bass:

    def selecttag(self,locator,text):
        tg = Select(locator)
        tg.select_by_visible_text(text)

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)  # in run time it automatically catches the filename
        filelocation = logging.FileHandler("/Users/kavin/Documents/FProject/Reports/logfile.log")  # FileHandler is used to create a file to save all logs
        format = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        filelocation.setFormatter(format)
        logger.addHandler(filelocation)

        logger.setLevel(logging.DEBUG)
        return logger