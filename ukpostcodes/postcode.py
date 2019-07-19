from ukpostcodes.outward import OutwardCode
from ukpostcodes.inward import InwardCode
from ukpostcodes.validate import validate_postcode


class PostCode:
    outward = None
    inward = None

    with_space = True

    def __init__(self, area, district, sector, unit, *args, **kwargs):
        self.outward = OutwardCode(area, district)
        self.inward = InwardCode(sector, unit)

    @property
    def format(self):
        if self.with_space:
            return f'{self.outward.format} {self.inward.format}'
        else:
            return f'{self.outward.format}{self.inward.format}'

    def validate(self, without_space=False):
        return validate_postcode(self.format, without_space=without_space)
