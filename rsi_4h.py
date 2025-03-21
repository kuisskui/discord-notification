import os
from mt5.indicators import get_rsi
from MetaTrader5 import TIMEFRAME_H4
from discord_apis.Discord import Discord
from utils import get_trade_directions
from mt5.provider import get_commission
from mt5 import initialize


WEBHOOK_URL = os.getenv('WEBHOOK_URL')
SYMBOL = "EURUSD"
TIMEFRAME = TIMEFRAME_H4
discord = Discord()
discord.add_channel(WEBHOOK_URL)


def rsi_4h():
    try:
        print("initializing")
        initialize()
        rsi = get_rsi(SYMBOL, TIMEFRAME)
        commissions = get_commission([SYMBOL])
        direction = get_trade_directions(commissions)

        message = ""
        if direction[0].get_type() == 0 and rsi <= 40:
            message += "BUT Opportunity!"
        if direction[0].get_type() == 1 and rsi >= 60:
            message += "SELL Opportunity!"
        message += "\n"
        message += f"RSI signal: {rsi:.2f}"
        print("Success Execution")
    except Exception as e:
        message = str(e)
    discord.notify_all(message)
    print(message)


rsi_4h()
