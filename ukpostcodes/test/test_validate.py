from ukpostcodes.validate import validate_postcode
from ukpostcodes.postcodes_examples import postcodes


def test_validate_AB_area():
    for postcode in postcodes['AB']['AB1']:
        result = validate_postcode(postcode)
        assert result

def test_validate_AB_area_without_space():
    result = validate_postcode('AB10AA', without_space=False)
    assert not result

    result = validate_postcode('AB10AA', without_space=True)
    assert result
