import pytest
from test1 import dot_product, InconsistentError

def test_onebvalue():
    with pytest.raises(InconsistentError):
        dot_product([1,6],[2,9]) == 59