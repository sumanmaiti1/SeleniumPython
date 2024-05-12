import os
import sys
import pytest
import allure
from datetime import datetime as dt
from .utilities.readconfig import ReadConfig
from .utilities.loggen import LogGen
from .utilities.browser import Browser
from .utilities.cleanup import CleanUp
from nopcommerce.configuration import configuration as config


class Conftest:
    log_gen = LogGen.log_gen()
    paramtuple = tuple(eval(ReadConfig.read_config('browser', 'parameterized_browser').strip().upper()))

    @staticmethod
    def set_project_path_in_path():
        sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/../../..'))


# -------------- creating object of ConfTest and setting the projrct directory in system path --------------
conftest = Conftest()
conftest.set_project_path_in_path()
driver = None
strmobile = ""


@pytest.fixture(scope="session", autouse=True)
def do_exceution_cleanup():
    LogGen.log_gen().info('--------- Performing Session Setup -------------\n')
    CleanUp.delete_screenshots_folder_before_execution()
    yield
    LogGen.log_gen().info('--------- Performing Session Teardown -------------')
    CleanUp.archive_report_folder_after_execution()


@pytest.fixture(scope='class', autouse=True, params=conftest.paramtuple)
def setup_teardown(request, get_mobile, get_env, get_browser, get_mobile_resolution, get_mobile_resolution_cdp):
    try:
        global driver
        global strmobile
        strbrowser = request.config.getoption('--browser')
        strenv = request.config.getoption('--env')
        strheadless = request.config.getoption('--headless')
        if get_mobile is not None:
            strmobile = get_mobile
        elif get_mobile_resolution is not None:
            strmobile = get_mobile_resolution

        resolution = get_mobile_resolution_cdp

        LogGen.log_gen().info('---------Performing Class Setup-------------')

        # --------------- Deciding which env to open ---------------
        if (strenv is not None) and ((strenv.strip().upper().__contains__('ADMIN')) or (strenv.strip().upper().__contains__('BACK'))):
            strenv = ReadConfig.read_config('project info', 'admin_url')
            LogGen.log_gen().info('---------invoking Admin/Backend evironment-------------')
        elif (strenv is not None) and ((strenv.strip().upper().__contains__('FRONT'))):
            strenv = ReadConfig.read_config('project info', 'frontend_url')
            LogGen.log_gen().info('---------invoking Frontend evironment-------------')
        else:
            strenv = ReadConfig.read_config('project info', 'default_url')
            LogGen.log_gen().info(f'---------Oops !!! Permitted values are 1) admin or backend 2) frontend. Hence invoking default evironment [{strenv}] mentioned in config.ini -------------')

        # --------------- Deciding execution mode if headless ---------------
        if (strheadless is not None) and ((strheadless.strip().upper().__contains__('T')) or (strheadless.strip().upper().__contains__('Y'))):
            strheadless = "true"
            LogGen.log_gen().info('---------executing with Headless mode-------------')
        elif (strheadless is not None) and ((strheadless.strip().upper().__contains__('F')) or (strheadless.strip().upper().__contains__('N'))):
            strheadless = "false"
        else:
            strheadless = ReadConfig.read_config('browser', 'headless')
            LogGen.log_gen().info(f'---------Oops !!! Permitted values are 1) True or Yes 2) False otr No. Hence executing with Headless=[{strheadless}] mode as mentioned in config.ini -------------')

        # --------------- Deciding which browser to invoke -----------
        if strbrowser is not None:
            if strbrowser.strip().upper().__eq__("CHROME"):
                strbrowser = "CHROME"
            elif strbrowser.strip().upper().__eq__("EDGE"):
                strbrowser = "EDGE"
            elif strbrowser.strip().upper().__eq__("ALL"):
                if request.param.upper() == "CHROME":
                    strbrowser = "CHROME"
                elif request.param.upper() == "EDGE":
                    strbrowser = "EDGE"
            else:
                strbrowser = ReadConfig.read_config('browser', 'default_browser').strip().upper()
        else:
            strbrowser = ReadConfig.read_config('browser', 'default_browser').strip().upper()
            LogGen.log_gen().info(f'---------Oops !!! Permitted values are 1) edge 2) chrome 3) all. Hence invoking default browser [{strbrowser}] mentioned in config.ini -------------')

        driver = Browser.get_driver(strbrowser, headless=strheadless, mobile=strmobile)
        # -------------------- Assigning Driver here for the classes to use --------------
        request.cls.driver = driver
        # ---------------- for Mobile resolution --------------
        if resolution is not None:
            driver.execute_cdp_cmd("Emulation.setDeviceMetricsOverride", resolution)

        driver.get(strenv)
        yield
        LogGen.log_gen().info('---------Performing Class Teardown-------------\n')
        driver.quit()
    except Exception as err:
        LogGen.log_gen().error(f'Runtime exception generated. Err: {err}\n')

# --------------- Setting the command line arguments here for runtime ---------------
def pytest_addoption(parser):
    parser.addoption('--browser')
    parser.addoption('--env')
    parser.addoption('--headless')
    parser.addoption('--mobile')
    parser.addoption('--mobileresolution')
    parser.addoption('--mobileresolutioncdp')

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


@pytest.fixture(scope='session')
def get_mobile(request):
    try:
        strmobile = request.config.getoption('--mobile')
        avaibale_mobiles = eval(ReadConfig.read_config('mobile', 'device_names'))
        if strmobile is not None:
            if strmobile in avaibale_mobiles:
                return {"deviceName": strmobile}
            else:
                return None
        else:
            return None
    except Exception as err:
        LogGen.log_gen().error(f' Runtime exception generated. Err: {err}\n')


@pytest.fixture(scope='session')
def get_mobile_resolution(request):
    try:
        strmobile = request.config.getoption('--mobileresolution')
        if strmobile is not None:
            mobile_emulation = {
                "deviceMetrics": {"width": int(strmobile.split('-')[0]), "height": int(strmobile.split('-')[1]),
                                  "deviceScaleFactor": int(strmobile.split('-')[2]),
                                  "pixelRatio": float(strmobile.split('-')[3]), "mobile": True},
                "clientHints": {"platform": "Android", "mobile": True},
                # ------------ below is for chrome android ----------------
                # "userAgent": "Mozilla/5.0 (Linux; Android 14) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6367.171 Mobile Safari/537.36",

                # ------------ below is for Edge android ----------------
                "userAgent": "Mozilla/5.0 (Linux; Android 14; Samsung Galaxy F54 5G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6367.171 Mobile Safari/537.36 EdgA/124.0.2478.71"

                # ------------ below is for chrome IOS ----------------
                # "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_4_1 like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6367.171 Mobile Safari/537.36"

                # ------------ below is for Edge IOS ----------------
                # "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 17_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 EdgiOS/124.2478.89 Mobile/15E148 Safari/605.1.15"

                # ------------ below is for Edge Win 11  ----------------
                # "userAgent": "Mozilla/5.0 (Windows Mobile 10; Android 10.0; Microsoft; Lumia 950XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36 Edge/40.15254.603"
            }
            return mobile_emulation
        else:
            return None
    except Exception as err:
        LogGen.log_gen().error(f' Runtime exception generated. Err: {err}\n')


@pytest.fixture(scope='session')
def get_mobile_resolution_cdp(request):
    try:
        resolution = request.config.getoption('--mobileresolutioncdp')
        if resolution is not None:
            return {'height': int(resolution.split('-')[0]), 'width': int(resolution.split('-')[1]), 'deviceScaleFactor': int(resolution.split('-')[2]), 'mobile': True}
        else:
            return None
    except Exception as err:
        LogGen.log_gen().error(f' Runtime exception generated. Err: {err}\n')

# --------------- Adding Screenshots only for the steps which are failed --------------
# ----------for Allure -  https://github.com/pytest-dev/pytest/issues/230 ---------
# ----------for html-report -  https://github.com/rafitur2/Python-Pytest-Selenium-HTML-report-with-multiple-screenshots/blob/master/conftest.py ---------


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    try:
        global driver
        pytest_html = item.config.pluginmanager.getplugin('html')
        outcome = yield
        rep = outcome.get_result()
        extra = getattr(rep, 'extras', [])

        # ----------- Only Take screenshots when test doesn't pass -----------
        if not rep.passed:
            screenshot_path = config.screenshot_path
            if not os.path.exists(screenshot_path):
                os.makedirs(screenshot_path)
            # file_name = report.nodeid.replace("::", "_") + ".png"
            file_name = screenshot_path + "\\" + "Failure_" + str(dt.now().strftime("%H_%M_%S")) + ".png"
            driver.get_screenshot_as_file(file_name)
            if file_name:
                html_report = f'<div><img src=%s alt="screenshot" style="width:300px; height:200px; " ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html_report))
            rep.extra = extra

        setattr(item, "rep_" + rep.when, rep)
        return rep
    except Exception as err:
        LogGen.log_gen().error(f' Runtime exception generated. Err: {err}\n')


# ------------------- For allure screenshots ------------------
@pytest.fixture(scope='function', autouse=True)
def log_on_failure(request):
    try:
        yield
        item = request.node
        current_timestamp = str(dt.now().strftime("%H_%M_%S"))
        if not item.rep_call.passed:
            allure.attach(request.cls.driver.get_screenshot_as_png(), name='Screenshot_' + current_timestamp, attachment_type=allure.attachment_type.PNG)
    except Exception as err:
        LogGen.log_gen().error(f' Runtime exception generated. Err: {err}\n')

# --------------- for html Report Title ---------------


def pytest_html_report_title(report):
    try:
        report.title = "NopCommerce Automation Execution :- " + str(dt.now().strftime("%d-%b-%Y %H:%M:%S"))
    except Exception as err:
        LogGen.log_gen().error(f' Runtime exception generated. Err: {err}\n')
