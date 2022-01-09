import pytest
from test import get_ctry_nm


@pytest.mark.parametrize("ctry_cd, ctry_nm", [("KR", "대한민국"), ("US", "미국")])
def test_get_ctry_nm(ctry_cd, ctry_nm):
    assert get_ctry_nm(ctry_cd) == ctry_nm
