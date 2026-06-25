"""Core business logic for the budget CLI app."""

from __future__ import annotations

import csv
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
    target = category.casefold()
    return [
        dict(transaction)
        for transaction in transactions
        if str(transaction.get("category", "")).casefold() == target
    ]


def load_transactions_from_csv(file_path: str) -> List[Dict[str, Any]]:
    """Load transactions from a CSV file."""
    with open(file_path, encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        return [
            {
                "date": row["date"],
                "type": row["type"],
                "category": row["category"],
                "description": row["description"],
                "amount": int(row["amount"]),
                "memo": row["memo"],
            }
            for row in reader
        ]


def monthly_summary(transactions: List[Dict[str, Any]]) -> Dict[str, Dict[str, Any]]:
    """Summarize transactions by month."""
    pass
