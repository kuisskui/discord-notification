import os

from utils import create_report
import requests
import mt5
from dotenv import load_dotenv

load_dotenv()

WEBHOOK_URL = os.environ.get('WEBHOOK_URL')
symbols = ["AUDUSD", "DXY", "EURUSD", "GBPUSD", "NZDUSD", "USDCAD", "USDCHF", "USDCHF"]


def main():
    try:
        mt5.initialize()
        commissions = mt5.get_commission(symbols)
        report = create_report(commissions)
        print(report)

        data = {"content": report}

        requests.post(WEBHOOK_URL, json=data)
    except Exception as e:
        print(e)
    finally:
        mt5.shutdown()


main()
