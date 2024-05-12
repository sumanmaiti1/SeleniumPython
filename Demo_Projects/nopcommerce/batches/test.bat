cd D:\Work\Projects\Python\Selenium\Demo_Projects\nopcommerce
python -m pytest --browser=all --mobileresolution="900-900-100" tests/test_demo.py --html="reports/html_report/report.html" --junit-xml=reports/execution.xml --alluredir reports/allure/allure-results --clean-alluredir -n 4
allure.bat generate --single-file reports/allure/allure-results --clean -o reports/allure/allure-report
pause