import pytest


def run_full_suite():
    report_path = "./reports/junit_report.xml"
    return_code = pytest.main(["tests/", f"--junitxml={report_path}", "-n", "auto"])
    print(return_code)

if __name__ == "__main__":
    run_full_suite()
