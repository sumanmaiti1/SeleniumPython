cd D:\Work\Projects\Python\Selenium\Demo_Projects\nopcommerce
rem python -m pytest --browser=all --mobileresolution="900-900-100" tests/test_demo.py --html="reports/html_report/report.html" --junit-xml=reports/execution.xml --alluredir reports/allure/allure-results --clean-alluredir -n 4
rem python -m pytest --browser=edge --mobile="iPad Air" tests/test_demo.py --html="reports/html_report/report.html" -m "suman" --junit-xml=reports/execution.xml --alluredir reports/allure/allure-results --clean-alluredir
python -m pytest --browser=chrome --mobileresolution="400-700-100-1.0" tests/test_demo.py --html="reports/html_report/report.html" -m "suman" --junit-xml=reports/execution.xml --alluredir reports/allure/allure-results --clean-alluredir
allure.bat generate --single-file reports/allure/allure-results --clean -o reports/allure/allure-report
pause