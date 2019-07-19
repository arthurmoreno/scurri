
class InwardCode:
    sector = None
    unit = None

    def __init__(self, sector, unit, *args, **kwargs):
        self.sector = sector
        self.unit = unit

    @property
    def format(self):
        return f'{self.sector}{self.unit}'
