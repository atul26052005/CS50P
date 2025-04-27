import pytest
from datetime import date, timedelta
from seasons import check_birthdate, calculate_diff

def test_check_birthdate():
    assert check_birthdate(2024, 10, 5) == date(2024, 10, 5)

    with pytest.raises(ValueError):
        check_birthdate(2024, 31, 10)

def test_calculate_diff():
    today = date.today()
    one_day_ago = today - timedelta(days=1)

    assert calculate_diff(one_day_ago) == "1440"

if __name__ == "__main__":
    pytest.main()
