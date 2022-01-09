from _pytest.compat import STRING_TYPES
import pandas as pd


def get_ctry_nm(ctry_cd: STRING_TYPES) -> STRING_TYPES:
    ctry_df = pd.read_html(
        "https://ko.wikipedia.org/wiki/%EA%B5%AD%EA%B0%80%EB%B3%84_%EA%B5%AD%EA%B0%80_%EC%BD%94%EB%93%9C_%EB%AA%A9%EB%A1%9D"
    )[0]
    return ctry_df[ctry_df["2자리"] == ctry_cd]["국명"].values[0]


# print(get_ctry_nm("KR"))
# print(get_ctry_nm("US"))
