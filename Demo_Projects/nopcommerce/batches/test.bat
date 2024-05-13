cd D:\Work\Projects\Python\Selenium\Demo_Projects\nopcommerce
python -m pytest --browser=all --mobileresolution="900-900-100-1.0" --html="reports/html_report/report.html" --junit-xml=reports/execution.xml --alluredir reports/allure/allure-results --clean-alluredir -n 4
allure.bat generate --single-file reports/allure/allure-results --clean -o reports/allure/allure-report
pause