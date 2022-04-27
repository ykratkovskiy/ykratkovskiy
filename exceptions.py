from codecs import lookup_error
from pydantic import PathError


s = 'hello'
try:
    s[7]
except:
    print ('fignya')
else:
    print ('all ok')