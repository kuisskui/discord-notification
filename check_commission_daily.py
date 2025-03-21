import os
import logging

import mt5
from dotenv import load_dotenv

from discord_apis.Discord import Discord
from mt5.provider import get_commission, get_positions
from utils import (
    create_report,
    get_trade_directions,
    is_my_positions_follow_trade_direction,
    create_message,
)

load_dotenv()
WEBHOOK_URL = os.getenv("WEBHOOK_URL")
SYMBOLS = ["AUDUSD", "DXY", "EURUSD", "GBPUSD", "NZDUSD", "USDCAD", "USDCHF", "USDJPY"]

TITLE = "COMMISSION Check Daily"
discord = Discord()
discord.add_channel(WEBHOOK_URL)

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")


def check_commission_daily() -> str:
    """
    Fetch commissions, positions, and trade directions;
    builds and returns the formatted daily report message.
    """
    mt5.initialize()
    try:
        commissions = get_commission(SYMBOLS)
        positions = get_positions(SYMBOLS)
        trade_directions = get_trade_directions(commissions)

        flag = (
            "RED Flag!!!"
            if not is_my_positions_follow_trade_direction(positions, trade_directions)
            else "Everything is fine for today 🙂"
        )

        report = create_report(commissions)
        return create_message([TITLE, flag, report])

    finally:
        mt5.shutdown()


def main():
    logging.info("Starting daily commission check.")
    try:
        message = check_commission_daily()
        logging.info("Report generated; sending to Discord.")
    except Exception as err:
        message = create_message([f"⚠️ Error: {err}"])
        logging.exception("Unhandled exception during commission check.")
    finally:
        discord.notify_all(message)
        logging.info("Execution finished.")


if __name__ == "__main__":
    main()
