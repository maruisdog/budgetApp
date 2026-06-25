"""Tests for budget.core."""

from budget.core import add_transaction, filter_by_category, get_balance


def test_add_transaction_increases_length() -> None:
    """Adding a transaction should increase the list length by one."""
    transactions = [
        {
            "date": "2026-01-05",
            "type": "지출",
            "category": "식비",
            "description": "점심식사",
            "amount": -12000,
            "memo": "",
        }
    ]
    transaction = {
        "date": "2026-01-07",
        "type": "수입",
        "category": "급여",
        "description": "월급",
        "amount": 3500000,
        "memo": "1월급여",
    }

    result = add_transaction(transactions, transaction)

    assert len(result) == 2
    assert result[-1] == transaction


def test_add_transaction_preserves_negative_amount_expense() -> None:
    """Expense transactions should keep a negative amount."""
    transactions = []
    transaction = {
        "date": "2026-01-10",
        "type": "지출",
        "category": "교통",
        "description": "지하철",
        "amount": -1500,
        "memo": "",
    }

    result = add_transaction(transactions, transaction)

    assert result[-1]["amount"] == -1500
    assert result[-1]["type"] == "지출"


def test_add_transaction_preserves_positive_amount_income() -> None:
    """Income transactions should keep a positive amount."""
    transactions = []
    transaction = {
        "date": "2026-01-07",
        "type": "수입",
        "category": "급여",
        "description": "월급",
        "amount": 3500000,
        "memo": "1월급여",
    }

    result = add_transaction(transactions, transaction)

    assert result[-1]["amount"] == 3500000
    assert result[-1]["type"] == "수입"


def test_add_transaction_allows_empty_description() -> None:
    """Transactions with an empty description should be stored as-is."""
    transactions = []
    transaction = {
        "date": "2026-01-28",
        "type": "기타수입",
        "category": "기타수입",
        "description": "",
        "amount": 25000,
        "memo": "중고마켓",
    }

    result = add_transaction(transactions, transaction)

    assert result[-1]["description"] == ""


def test_get_balance_returns_total_amount() -> None:
    """Balance should equal the sum of income and expense amounts."""
    transactions = [
        {
            "date": "2026-01-04",
            "type": "지출",
            "category": "여행",
            "description": "항공권",
            "amount": -979796,
            "memo": "메모_3",
        },
        {
            "date": "2026-01-15",
            "type": "수입",
            "category": "기타수입",
            "description": "중고 판매",
            "amount": 135541,
            "memo": "",
        },
        {
            "date": "2026-02-01",
            "type": "수입",
            "category": "급여",
            "description": "월급",
            "amount": 4358625,
            "memo": "",
        },
    ]

    assert get_balance(transactions) == 3514370


def test_get_balance_returns_zero_for_empty_list() -> None:
    """Balance should be zero when there are no transactions."""
    assert get_balance([]) == 0.0


def test_filter_by_category_returns_matching_transactions() -> None:
    """Category filtering should return only matching transactions."""
    transactions = [
        {
            "date": "2026-01-04",
            "type": "지출",
            "category": "여행",
            "description": "항공권",
            "amount": -979796,
            "memo": "메모_3",
        },
        {
            "date": "2026-01-15",
            "type": "수입",
            "category": "기타수입",
            "description": "중고 판매",
            "amount": 135541,
            "memo": "",
        },
        {
            "date": "2026-02-01",
            "type": "수입",
            "category": "급여",
            "description": "월급",
            "amount": 4358625,
            "memo": "",
        },
    ]

    result = filter_by_category(transactions, "여행")

    assert result == [transactions[0]]


def test_filter_by_category_returns_empty_list_for_missing_category() -> None:
    """Missing categories should return an empty list."""
    transactions = [
        {
            "date": "2026-01-04",
            "type": "지출",
            "category": "여행",
            "description": "항공권",
            "amount": -979796,
            "memo": "메모_3",
        }
    ]

    result = filter_by_category(transactions, "외식")

    assert result == []


def test_filter_by_category_returns_independent_results() -> None:
    """Filtered results should be independent from the original list."""
    transactions = [
        {
            "date": "2026-01-04",
            "type": "지출",
            "category": "식비",
            "description": "항공권",
            "amount": -979796,
            "memo": "메모_3",
        },
        {
            "date": "2026-01-29",
            "type": "지출",
            "category": "식비",
            "description": "편의점",
            "amount": -33021,
            "memo": "",
        },
        {
            "date": "2026-02-01",
            "type": "수입",
            "category": "급여",
            "description": "월급",
            "amount": 4358625,
            "memo": "",
        },
    ]

    result = filter_by_category(transactions, "식비")
    result[0]["description"] = "변경됨"

    assert transactions[0]["description"] == "항공권"
