class Commission:
    def __init__(self):
        self.symbol = None
        self.long_swap = None
        self.short_swap = None
        self.type = None

    def set_symbol(self, symbol):
        self.symbol = symbol

    def set_swap_long(self, long_swap):
        self.long_swap = long_swap

    def set_swap_short(self, short_swap):
        self.short_swap = short_swap

    def set_type(self, type):
        self.type = type

    def __repr__(self):
        return (f"Commission(symbol={self.symbol!r}, "
                f"long_swap={self.long_swap!r}, short_swap={self.short_swap!r}, "
                f"type={self.type!r})")
