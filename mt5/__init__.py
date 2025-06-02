import MetaTrader5 as mt5
from settings import settings

ACCOUNT = settings.ACCOUNT
PASSWORD = settings.PASSWORD
SERVER = settings.SERVER


def initialize():
    # establish connection to the MetaTrader 5 terminal
    mt5.initialize()
    if not mt5.initialize():
        error_code = mt5.last_error()
        raise ConnectionError(f"Failed to initialize MT5 connection: error code {error_code}")


def shutdown():
    mt5.shutdown()
