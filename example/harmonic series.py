# harmonic seires.py
"""2015.03.30"""

import math

an = 0
n = 100

for i in range(1, n+1):
    an = an + (1/i)
    er = (an - math.log(i+1) ) / an
    print("error is %f." %(er*100))


