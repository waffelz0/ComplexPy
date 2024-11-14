
# ComplexPy Library
ComplexPy is a Python library for storing and doing arithmetic with complex numbers.

This library allows you to perform elementary, trigonometric, logarithmic, and comparative operations with complex numbers.

## Functions

\-  ``toString``

\-  ``add`` / ``sum``

\-  ``sub`` / ``subtract`` / ``difference``

\-  ``mul`` / ``multiply`` / ``product`` / ``scale``

\-  ``div`` / ``divide`` / ``quotient``

\-  ``pow`` / ``exponentiate``

\-  ``sqrt`` / ``square_root``

\-  ``nroot`` / ``nth_root``

\-  ``abs`` / ``absolute_value`` / ``mod`` / ``modulus``

\-  ``conj`` / ``conjugate``

\-  ``arg`` / ``argument``

\-  ``ln`` / ``natural_log`` / ``natural_logarithm``

\-  ``log`` / ``logarithm`` / ``general_log``

\-  ``eq`` / ``equals``

\-  ``le`` / ``less`` / ``less_than``

\-  ``gr`` / ``greater`` / ``greater_than``

\-  ``leeq`` / ``less_than_or_equals``

\-  ``greq`` / ``greater_than_or_equals``

\-  ``sin`` / ``sine``

\-  ``cos`` / ``cosine``

\-  ``tan`` / ``tangent``

## Usage Examples
```py
from ComplexPy import *

number = complexNumber(3, 7)
number2 = complexNumber(8, 4)

print(number.toString()) # Will print "3 + 7 i"
print(number.add(number2).toString()) # Will print "11 + 11 i"
print(number.pow(complexNumber(3, 0)).toString()) # Will print "-414.00000000000006 - 154.0 i"
print(number.sine().toString()) # Will print "77.37850442046603 - 542.8288478055589 i"
print(number.sqrt().toString()) # Will print "2.3038850997677716 + 1.5191729832155236 i"
print(number.sqrt(1).toString()) # Will print "-2.3038850997677716 - 1.5191729832155234 i"
```
## Installation

You can install this library by running the command below in a command prompt or powershell terminal.

```bash
pip install ComplexPy
```

## Version history
### v1.0.0
\- Initial release.
