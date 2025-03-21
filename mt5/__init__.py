import os
import MetaTrader5 as mt5

ACCOUNT = os.environ.get("ACCOUNT")
PASSWORD = os.environ.get("PASSWORD")
SERVER = os.environ.get("SERVER")


def initialize():
    # establish connection to the MetaTrader 5 terminal
    if not mt5.initialize():
        print("initialize() failed, error code =", mt5.last_error())
        quit()

    authorized = mt5.login(int(ACCOUNT), password=PASSWORD, server=SERVER)

    if authorized:
        print("successfully logged in at account #{}".format(ACCOUNT))
    else:
        print("failed to connect at account #{}, error code: {}".format(ACCOUNT, mt5.last_error()))


def shutdown():
    mt5.shutdown()
