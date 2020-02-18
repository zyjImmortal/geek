def pytest_report_header(config):
    if config.getoption('nice'):
        return 'Hello Pytest'


def pytest_report_teststatus(report, config):
    if report.when == 'call' and report.failed and config.getoption('nice'):
        return (report.outcome, 'O', '继续努力')


def pytest_addoption(parser):
    group = parser.getgroup('nice')
    group.addoption('--nice', action='store_true', help='nice: refactor failures')