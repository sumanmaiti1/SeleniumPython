import shutil
import os
import shutil
from datetime import datetime  as dt
from distutils.dir_util import copy_tree
from nopcommerce.utilities.loggen import LogGen
from configuration.configuration import screenshot_path, execution_result_archive_path, report_path


class CleanUp:
    """This class is responsible for cleaning up Job before and after Execution"""


    @staticmethod
    def delete_screenshots_folder_before_execution():
        """This methods deletes the screenshot folder before execution starts"""
        try:
            shutil.rmtree(screenshot_path)
            LogGen.log_gen().info(f"Successfully deleted Screenshots folder.\n")
        except Exception as err:
            LogGen.log_gen().error(f"Runtime Exception Generated at runtime. Exception {err}")


    @staticmethod
    def archive_report_folder_after_execution():
        """This methods archives the execution Results"""
        try:
            struser = str(os.getlogin())
            strdate = dt.now().strftime("%d_%b_%Y")
            strtime = dt.now().strftime("%H_%M_%S")
            # ----------- checking if Execution path exists, if not create it -------------
            if not os.path.exists(execution_result_archive_path):
                os.makedirs(execution_result_archive_path)

            # ----------- checking if Today's Folder path exists, if not create it -------------
            strdatepath = execution_result_archive_path + "\\" + strdate
            if not os.path.exists(strdatepath):
                os.makedirs(strdatepath)

            # ----------- checking if User path exists, if not create it -------------
            struserpath = strdatepath + "\\" + struser
            if not os.path.exists(struserpath):
                os.makedirs(struserpath)

            # ----------- checking if User path exists, if not create it -------------
            strnewreportpath = struserpath + "\\reports_" + strtime
            if not os.path.exists(strnewreportpath):
                os.makedirs(strnewreportpath)

            # ----------- Copy Report Path -----------
            copy_tree(report_path, strnewreportpath)
        except Exception as err:
            LogGen.log_gen().error(f"Runtime Exception Generated at runtime. Exception {err}")