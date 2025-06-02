import os

import mt5
from dotenv import load_dotenv
from settings import settings
from discord_apis.Discord import Discord
from mt5.provider import get_commission, get_positions
from utils import (
    create_report,
    get_trade_directions,
    is_my_positions_follow_trade_direction,
    create_message,
)

WEBHOOK_URL = settings.WEBHOOK_URL
SYMBOLS = settings.SYMBOLS

TITLE = "COMMISSION Check Daily"
discord = Discord()
discord.add_channel(WEBHOOK_URL)


def check_commission_daily() -> str:
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
    try:
        message = check_commission_daily()
    except Exception as err:
        message = create_message([f"⚠️ Error: {err}"])
    finally:
        discord.notify_all(message)


if __name__ == "__main__":
    main()
