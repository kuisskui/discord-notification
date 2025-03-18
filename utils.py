from datetime import datetime, timezone

import MetaTrader5

import mt5
from models import Commission, TradeDirection, Position


def format_markdown_table(table):
    """
    Given a table as a list of lists (first row is headers),
    returns a string with a markdown formatted table with padded cells.
    """
    # Calculate the maximum width for each column.
    num_cols = len(table[0])
    col_widths = [max(len(str(row[i])) for row in table) for i in range(num_cols)]

    # Build the header row.
    header = "| " + " | ".join(str(table[0][i]).ljust(col_widths[i]) for i in range(num_cols)) + " |"

    # Build the separator row.
    separator = "| " + " | ".join("-" * col_widths[i] for i in range(num_cols)) + " |"

    # Build the data rows.
    data_rows = [
        "| " + " | ".join(str(row[i]).ljust(col_widths[i]) for i in range(num_cols)) + " |"
        for row in table[1:]
    ]

    # Combine all parts.
    return "\n".join([header, separator] + data_rows)


def commissions_to_table(commissions):
    """
    Convert a list of Commission objects to a list of lists,
    with the first row as headers.
    """
    headers = ["Symbol", "Swap Long", "Swap Short", "Type"]
    rows = []
    for c in commissions:
        rows.append([
            c.symbol,
            c.long_swap,
            c.short_swap,
            c.type
        ])
    return [headers] + rows


def create_report(commissions):
    utc_now = datetime.now(timezone.utc)
    table_data = commissions_to_table(commissions)
    detail = format_markdown_table(table_data)

    report = \
        f"""```Scrape Commission: {utc_now.isoformat()}
{detail}
```"""
    return report


def get_trade_direction(commissions: [Commission]):
    trade_direction_list = []
    for commission in commissions:
        trade_direction = TradeDirection()
        trade_direction.set_symbol(commission.get_symbol())
        if commission.get_swap_long() <= commission.get_swap_short():  # the commission is negative
            trade_direction.set_type(0)
        else:
            trade_direction.set_type(1)
        trade_direction_list.append(trade_direction)
    return trade_direction_list


def is_my_positions_follow_trade_direction(positions: list, trade_directions: list) -> bool:
    trade_direction_dict = {td.get_symbol(): td.get_type() for td in trade_directions}

    for position in positions:
        symbol = position.get_symbol()
        if symbol in trade_direction_dict:
            if position.get_type() != trade_direction_dict[symbol]:
                return False
    return True


def create_message(messages: []):
    final_message = ""
    for message in messages:
        final_message += f"\n{message}"
    return final_message
