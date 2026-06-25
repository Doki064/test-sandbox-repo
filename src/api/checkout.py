"""Checkout API — initial implementation."""

from __future__ import annotations

from src.payments.processor import PaymentProcessor

_processor = PaymentProcessor()


def checkout(cart_total: float, currency_code: str) -> dict:
    """Process checkout for a cart.

    Args:
        cart_total: Total cart value (must be > 0).
        currency_code: ISO 4217 currency code (e.g. "USD").
    """
    return _processor.charge(cart_total, currency_code)
