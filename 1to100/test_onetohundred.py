import sys
from contextlib import contextmanager
from io import StringIO

from onetohundred import print_1_to_100


@contextmanager
def captured_output():
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err


def generate_expected_output():
    expected_output = ''
    for i in range(1, 100):

        if i%3 == 0 and i%5 == 0:
            i = 'ThreeFive'
        elif i%3 == 0:
            i = 'Three'
        elif i%5 == 0:
            i = 'Five'

        if i == 1:
            expected_output += f'{i}'
        else:
            expected_output += f'\n{i}'
    return expected_output


def test_1to100_output():
    expected_output = generate_expected_output()
    
    with captured_output() as (out, err):
        print_1_to_100()

    output = out.getvalue().strip()
    assert expected_output == output
