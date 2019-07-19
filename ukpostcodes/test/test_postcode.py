from ukpostcodes.outward import OutwardCode
from ukpostcodes.inward import InwardCode
from ukpostcodes.postcode import PostCode

# Format tests - Example: 'AB1 0AA'

def test_outward_format():
    outward = OutwardCode('AB', '1')
    assert outward.format == 'AB1'


def test_inward_format():
    inward = InwardCode('0', 'AA')
    assert inward.format == '0AA'


def test_postcode_format():
    postcode = PostCode('AB', '1', '0', 'AA')
    assert postcode.format == 'AB1 0AA'


def test_postcode_format_without_space():
    postcode = PostCode('AB', '1', '0', 'AA')
    postcode.with_space = False
    assert postcode.format == 'AB10AA'


def test_postcode_validate():
    postcode = PostCode('AB', '1', '0', 'AA')
    assert postcode.validate()


def test_postcode_failed_validation():
    postcode = PostCode('AB', '1', 'tests', 0)
    assert not postcode.validate()
