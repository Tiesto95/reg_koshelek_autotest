from util.registration import Registrtion


def pytest_sessionfinish(session, exitstatus):
    Registrtion.browse_close()
