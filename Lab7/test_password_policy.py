from hypothesis import given, strategies as st
from password_policy import first_character_type, split_credentials, digit_ratio

@given(st.text() | st.none())
def test_first_character_type_no_crash(s):
    try:
        first_character_type(s)
    except Exception as e:
        assert False, f"first_character_type crashed with: {e!r}"

@given(st.text() | st.none())
def test_split_credentials_no_crash(s):
    try:
        split_credentials(s)
    except Exception as e:
        assert False, f"split_credentials crashed with: {e!r}"

@given(st.text() | st.none())
def test_digit_ratio_no_crash(s):
    try:
        digit_ratio(s)
    except Exception as e:
        assert False, f"digit_ratio crashed with: {e!r}"
