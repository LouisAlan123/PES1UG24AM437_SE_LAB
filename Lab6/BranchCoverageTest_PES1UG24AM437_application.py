import pytest
from password_policy import check_password, strength, suggest_fix

# Example test cases (provided):
def test_valid_password_has_no_issues():
    assert check_password("Abcdef1!") == []

def test_valid_password_is_good():
    assert strength("Abcdef1!") == "good"

# --- Additional test cases for code (line) coverage ---

def test_too_short_password():
    assert "too short" in check_password("Ab1!")

def test_too_long_password():
    pw = "Aa1!" * 20  # 80 chars, > 64
    assert "too long" in check_password(pw)

def test_common_password():
    assert "common" in check_password("password")

def test_missing_all_character_categories():
    issues = check_password("aaaaaaaa")
    assert "no uppercase" in issues
    assert "no digit" in issues
    assert "no special" in issues

def test_empty_password_issues():
    issues = check_password("")
    assert "too short" in issues
    assert "no uppercase" in issues
    assert "no lowercase" in issues
    assert "no digit" in issues
    assert "no special" in issues

def test_strength_strong():
    assert strength("Aabcdefgh1234!") == "strong"

def test_strength_weak():
    assert strength("abcdefgh1!") == "weak"

def test_strength_very_weak():
    assert strength("") == "very weak"

def test_suggest_fix_none_needed():
    assert suggest_fix([]) == "none needed"

def test_suggest_fix_too_short():
    assert suggest_fix(["too short"]) == "add more characters"

def test_suggest_fix_common():
    assert suggest_fix(["common"]) == "avoid common passwords"

def test_suggest_fix_missing_category():
    assert suggest_fix(["no uppercase"]) == "add uppercase"

def test_suggest_fix_other():
    assert suggest_fix(["too long"]) == "shorten it"
