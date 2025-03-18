class Commission:
    def __init__(self):
        self.symbol = None
        self.long_swap = None
        self.short_swap = None
        self.type = None

    def set_symbol(self, symbol):
        self.symbol = symbol

    def get_symbol(self):
        return self.symbol

    def set_swap_long(self, long_swap):
        self.long_swap = long_swap

    def get_swap_long(self):
        return self.long_swap

    def set_swap_short(self, short_swap):
        self.short_swap = short_swap

    def get_swap_short(self):
        return self.short_swap

    def set_type(self, type):
        self.type = type

    def get_type(self):
        return self.type

    def __repr__(self):
        return (f"Commission(symbol={self.symbol!r}, "
                f"long_swap={self.long_swap!r}, short_swap={self.short_swap!r}, "
                f"type={self.type!r})")


class Position:
    def __init__(self):
        self.symbol = None
        self.type = None

    def set_symbol(self, symbol):
        self.symbol = symbol

    def get_symbol(self):
        return self.symbol

    def set_type(self, type):
        self.type = type

    def get_type(self):
        return self.type

    def __repr__(self):
        return (f"Position(symbol={self.symbol!r}, "
                f"type={self.type!r})")


class TradeDirection:
    def __init__(self):
        self.symbol = None
        self.type = None

    def set_symbol(self, symbol):
        self.symbol = symbol

    def set_type(self, type):
        self.type = type

    def get_symbol(self):
        return self.symbol

    def get_type(self):
        return self.type

    def __repr__(self):
        return (f"TradeDirection(symbol={self.symbol!r}, "
                f"type={self.type!r})")
