import MetaTrader5 as mt5
from models import Commission, Position
from typing import List


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


