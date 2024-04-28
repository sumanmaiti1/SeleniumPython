import pytest
from .utilities.readconfig import ReadConfig
from .utilities.loggen import LogGen
from .utilities.browser import Browser

class Conftest:
    log_gen= LogGen.log_gen()

conftest = Conftest()


@pytest.fixture(scope='class',autouse=True)
def setup_teardown(request):
    driver=None
    strbrowser = request.config.getoption('--browser')
    strenv = request.config.getoption('--env')
    strheadless = request.config.getoption('--headless')

    LogGen.log_gen().info('---------Performing Class Setup-------------')

    # --------------- Deciding which browser to invoke -----------
    if (strbrowser is not None) and (strbrowser.strip().upper().__eq__("CHROME")):
        strbrowser = "CHROME"
        LogGen.log_gen().info('---------invoking chrome browser-------------')
    elif (strbrowser is not None) and (strbrowser.strip().upper().__eq__("EDGE")):
        strbrowser = "EDGE"
        LogGen.log_gen().info('---------invoking edge browser-------------')
    else:
        strbrowser = ReadConfig.read_config('browser','default_browser').strip().upper()
        LogGen.log_gen().info(f'---------Oops !!! Permitted values are 1) edge 2) chrome. Hence invoking default browser [{strbrowser}] mentioned in config.ini -------------')

    # --------------- Deciding which env to open ---------------
    if (strenv is not None) and ((strenv.strip().upper().__contains__('ADMIN')) or (strenv.strip().upper().__contains__('BACK'))):
        strenv = ReadConfig.read_config('project info','admin_url')
        LogGen.log_gen().info('---------invoking Admin/Backend evironment-------------')
    elif (strenv is not None) and ((strenv.strip().upper().__contains__('FRONT'))):
        strenv = ReadConfig.read_config('project info','frontend_url')
        LogGen.log_gen().info('---------invoking Frontend evironment-------------')
    else:
        strenv = ReadConfig.read_config('project info','default_url')
        LogGen.log_gen().info(f'---------Oops !!! Permitted values are 1) admin or backend 2) frontend. Hence invoking default evironment [{strenv}] mentioned in config.ini -------------')

    # --------------- Deciding execution mode if headless ---------------
    if (strheadless is not None) and ((strheadless.strip().upper().__contains__('T')) or (strheadless.strip().upper().__contains__('Y'))):
        strheadless = "true"
        LogGen.log_gen().info('---------executing with Headless mode-------------')
    elif (strheadless is not None) and ((strheadless.strip().upper().__contains__('F')) or (strheadless.strip().upper().__contains__('N'))):
        strheadless = "false"
    else:
        strheadless = ReadConfig.read_config('browser','headless')
        LogGen.log_gen().info(f'---------Oops !!! Permitted values are 1) True or Yes 2) False otr No. Hence executing with Headless=[{strheadless}] mode as mentioned in config.ini -------------')

    # -------------------- Assigning Driver here for the classes to use --------------
    driver = Browser.get_driver(strbrowser,headless=strheadless)
    request.cls.driver = driver
    driver.get(strenv)
    yield
    LogGen.log_gen().info('---------Performing Class Teardown-------------')
    driver.quit()



# --------------- Setting the command line arguments here for runtime ---------------
def pytest_addoption(parser):
    parser.addoption('--browser')
    parser.addoption('--env')
    parser.addoption('--headless')

# ------- getting the value of Browser at runtime -------
@pytest.fixture(scope='session')
def get_browser(request):
    return request.config.getoption('--browser')

# ------- getting the value of Environment to Test at runtime -------
@pytest.fixture(scope='session')
def get_env(request):
    return request.config.getoption('--env')


# ------- getting the value of headless to Test at runtime -------
@pytest.fixture(scope='session')
def get_env(request):
    return request.config.getoption('--headless')