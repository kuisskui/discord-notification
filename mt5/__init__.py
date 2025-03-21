import os
import MetaTrader5 as mt5
from dotenv import load_dotenv
load_dotenv()

ACCOUNT = int(os.environ.get("ACCOUNT"))
PASSWORD = os.environ.get("PASSWORD")
SERVER = os.environ.get("SERVER")


def initialize():
    # establish connection to the MetaTrader 5 terminal
    mt5.initialize()
    if not mt5.initialize():
        print("initialize() failed, error code =", mt5.last_error())
        quit()


def shutdown():
    mt5.shutdown()
