
class OutwardCode:
    area = None
    district = None

    def __init__(self, area, district, *args, **kwargs):
        self.area = area
        self.district = district

    @property
    def format(self):
        return f'{self.area}{self.district}'
