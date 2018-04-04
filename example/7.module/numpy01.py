import os
import sys
for p in sys.path:
    if os.path.exists(os.path.join(p, 'numpy')):
        print (p)
    else:
        print( "Numpy not found")
