# Scurri
Scurri Code Test

## Enviroment
First create a python virtual enviroment and install the dependencies listed in requirements.txt.

Example:
```
pip install -r requirements.txt
```

To Run tests:
```
make tests
```

## 1 to 100
![Test Coverage](coverage_1to100.svg)

A program that prints the numbers from 1 to 100.

To Run 1 to 100:
```
make run1to100
```

## Uk Post Codes API
![Test Coverage](coverage_pc.svg)

### OutwardCode
OutwardCode class represents the first part of a post code. To create an instance of an OutwardCode, it is necessary a *area* and a *district*. OutwardCode has a property *format* that format the OutwardCode information into a single String.

```python
OutwardCode:
    def __init__(self, area, district, *args, **kwargs):

    @property
    def format(self):
```

Example:
```python
In [1]: from ukpostcodes.outward import OutwardCode
In [2]: outward = OutwardCode('AB', '1')
In [3]: outward.format
Out[3]: 'AB1'
```

### InwardCode
InwardCode class represents the second part of a post code. To create an instance of an InwardCode, it is necessary a *sector* and an *unit*. InwardCode has a property *format* that format the InwardCode information into a single String.

```python
InwardCode:
    def __init__(self, sector, unit, *args, **kwargs):

    @property
    def format(self):
```

Example:
```python
In [1]: from ukpostcodes.inward import InwardCode
In [2]: inward = InwardCode('0', 'AA')
In [3]: inward.format           
Out[3]: '0AA'
```

### PostCode
PostCode class represents a UK post code. To create an instance of a PostCode, it is necessary a *area*, *district*, *sector* and an *unit*. PostCode has a property *format* that format the PostCode information into a single String. It also has a validate method that validates if the formated Postcode is one of the allowed formats. The PostCode class has an attribute *with_space* that is *True* by Default, this attribute is used in the *format* property to generate the string with or without a space.

```python
PostCode:
    def __init__(self, area, district, sector, unit, *args, **kwargs):

    @property
    def format(self):

    def validate(self, without_space=False):
```

Example:
```python
In [1]: from ukpostcodes.postcode import PostCode

In [2]: postcode = PostCode('AB', '1', '0', 'AA')
In [3]: postcode.format       
Out[3]: 'AB1 0AA'
In [4]: postcode.validate()
Out[4]: True

In [5]: postcode = PostCode('AB', '1', 'test', 0)
In [6]: postcode.validate()           
Out[6]: False
```

### validate_postcode
The *validate_postcode* method validates if a raw string is in one of the allowed formats. If the *without_space* is True, the method allows postcodes without a string between the OutwardCode and the InwardCode.

```python
def validate_postcode(postcode, without_space=False):
```

Example:
```python
In [1]: from ukpostcodes.validate import validate_postcode

In [2]: validate_postcode('AB1 0AA')       
Out[2]: True

In [3]: validate_postcode('AB10AA')
Out[3]: False

In [4]: validate_postcode('AB10AA', without_space=True)
Out[4]: True
