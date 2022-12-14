import pytest
import datetime

def run_full_suite():
    report_path = f"./reports/{datetime.datetime.now().isoformat(sep='_', timespec='seconds')}_junit_report.xml"
    return_code = pytest.main(["tests", f"--junitxml={report_path}", "-n", "auto"])
    print(return_code)

if __name__ == "__main__":
    pytest.main(["-n 8"])