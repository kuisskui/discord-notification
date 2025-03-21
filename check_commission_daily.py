import os

from discord_apis.Discord import Discord
from utils import create_report, get_trade_directions, is_my_positions_follow_trade_direction, create_message
from mt5.provider import get_commission, get_positions
import mt5
from dotenv import load_dotenv

load_dotenv()
WEBHOOK_URL = os.environ.get('WEBHOOK_URL')
symbols = ["AUDUSD", "DXY", "EURUSD", "GBPUSD", "NZDUSD", "USDCAD", "USDCHF", "USDJPY"]

discord = Discord()
discord.add_channel(WEBHOOK_URL)


def check_commission_daily():
    print("Start execution for main function.")
    title = "COMMISSION Check Daily"
    message = "Message is empty!"
    try:
        mt5.initialize()
        commissions = get_commission(symbols)
        my_positions = get_positions(symbols)
        trade_direction_list = get_trade_directions(commissions)

        if not is_my_positions_follow_trade_direction(my_positions, trade_direction_list):
            flag = "RED Flag!!!"
        else:
            flag = "Everything is fine for today :)"

        report = create_report(commissions)

        message = create_message([title, flag, report])
        print(message)

        print("Send the report.")
    except Exception as e:
        message = create_message([str(e), ])
        print(e)
    finally:
        print("End execution for main function.")
        discord.notify_all(message)
        mt5.shutdown()


check_commission_daily()
