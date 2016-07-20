# import modules
import math # import math module from the standard library
print('8! =', math.factorial(8))

from math import factorial # import a particular function from math module 
print('10! =', factorial(10))

from math import factorial as fac # import a particular module using aslias
print('5! =', fac(5))

# integer division
print('float division by default!', fac(10) / 5)
print(fac(10) // 5)

# large number calculation capability
print('100! has', len(str(fac(100))), 'digits!')

import sys
print(sys.version_info)


