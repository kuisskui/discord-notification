import os
import MetaTrader5 as mt5
from models import Commission, Position
from typing import List
from dotenv import load_dotenv

load_dotenv()

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


def get_commission(symbols: List):
    commissions = []
    for symbol in symbols:
        commission = Commission()
        symbol_info = mt5.symbol_info(symbol)
        commission.set_symbol(symbol_info.name)
        commission.set_type("Raw Spread")
        commission.set_swap_long(symbol_info.swap_long)
        commission.set_swap_short(symbol_info.swap_short)
        commissions.append(commission)
    return commissions


def get_positions(symbols: List):
    positions = []
    for symbol in symbols:
        position = Position()
        received_position = mt5.positions_get(symbol=symbol)
        if not received_position:
            continue
        position.set_symbol(received_position[0].symbol)
        position.set_type(received_position[0].type)
        positions.append(position)

    return positions


def shutdown():
    mt5.shutdown()
