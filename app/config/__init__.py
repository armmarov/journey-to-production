import os
import sys
import app.config.settings

# create settings object corresponding to specified env
FLASK_ENV = os.environ.get('FLASK_ENV', 'Development')
_current = getattr(sys.modules['app.config.settings'], '{0}Config'.format(FLASK_ENV))()

# copy attributes to the module for convenience
for atr in [f for f in dir(_current) if not '__' in f]:
    # environment can override anything
    val = os.environ.get(atr, getattr(_current, atr))
    setattr(sys.modules[__name__], atr, val)


def as_dict():
    res = {}
    for atr in [f for f in dir(settings) if not '__' in f]:
        val = getattr(settings, atr)
        res[atr] = val
    return res