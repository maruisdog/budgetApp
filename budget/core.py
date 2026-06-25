"""Core business logic for the budget CLI app."""

from __future__ import annotations

from typing import Any, Dict, List


def add_transaction(transactions: List[Dict[str, Any]], transaction: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Add a transaction to the list and return the updated list."""
    transactions.append(transaction)
    return transactions


def get_balance(transactions: List[Dict[str, Any]]) -> float:
    """Calculate the balance from a list of transactions."""
    return float(sum(transaction["amount"] for transaction in transactions))


def filter_by_category(transactions: List[Dict[str, Any]], category: str) -> List[Dict[str, Any]]:
    """Return transactions that match the given category."""
    pass


def load_transactions_from_csv(file_path: str) -> List[Dict[str, Any]]:
    """Load transactions from a CSV file."""
    pass


def monthly_summary(transactions: List[Dict[str, Any]]) -> Dict[str, Dict[str, Any]]:
    """Summarize transactions by month."""
    pass
