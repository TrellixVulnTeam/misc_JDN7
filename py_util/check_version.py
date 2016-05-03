# two methods to check python version:
# put either of them at top of main.py before import anything else.
# put it in __init__.py if using package.

import sys
# print (sys.version)
# print (sys.version_info)
# print (sys.hexversion)
print("test")

# method 1:
import sys
PY_VERS = (3, 2)
assert (sys.version_info >= PY_VERS), "Sorry, this program requires Python " \
    "{}+, not Python {}.".format('.'.join(map(str, PY_VERS)), sys.version[:5])

# VERSION_ERROR = "Sorry, this program requires Python 3.2+, not Python {}.".format(sys.version[:5])
# assert (sys.version_info >= (3, 2)), VERSION_ERROR
# assert (sys.version_info >= (3,2)), "Sorry, this program requires Python 3.2+, not Python {}.".format(sys.version_info)
# assert (sys.version_info >= (3,2)), "Sorry, this program requires Python 3.2+, not Python "+ str(sys.version_info)

# method 2:
import sys
if sys.version_info < (3, 2):
    sys.stdout.write("Error: Sorry, requires Python 3.2+, not Python 2.x\n")
    sys.exit(1)

if __name__ == "__main__":
    print("this is main")
