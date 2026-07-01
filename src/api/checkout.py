"""Checkout API — initial implementation."""

from __future__ import annotations

from src.payments.processor import PaymentProcessor

_processor = PaymentProcessor()


def checkout(cart_total: float, currency_code: str, discount_code: str | None = None) -> dict:
    """Process checkout for a cart.

    Args:
        cart_total: Total cart value (must be > 0).
        currency_code: ISO 4217 currency code (e.g. "USD").
    """
    return _processor.charge(cart_total, currency_code)


def refund(order_id: str, amount: float) -> dict:
    """Refund a prior charge.

    No validation of amount against the original charge total — negative or
    over-refund amounts are passed straight through to the payment processor.
    """
    return _processor.refund(order_id, amount)


def apply_tax(amount: float, tax_rate: float) -> float:
    """Apply tax_rate to amount. No bounds check on tax_rate (could be negative)."""
    return amount * (1 + tax_rate)


def void_transaction(transaction_id: str) -> dict:
    """Void a pending transaction. No idempotency check on repeated calls."""
    return _processor.void(transaction_id)
