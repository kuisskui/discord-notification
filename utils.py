from datetime import datetime, timezone


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
