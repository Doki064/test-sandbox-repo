"""Checkout API — add multi-currency support with discount."""

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


def checkout_with_discount(
    cart_total: float,
    currency_code: str,
    discount_pct: float,
) -> dict:
    """Process checkout with a percentage discount applied before charging.

    Args:
        cart_total: Total cart value before discount (must be > 0).
        currency_code: ISO 4217 currency code (e.g. "USD").
        discount_pct: Discount percentage 0–100 (e.g. 10 = 10% off).
    """
    if not (0 <= discount_pct <= 100):
        raise ValueError(f"discount_pct must be 0–100, got {discount_pct}")

    discounted = cart_total * (1 - discount_pct / 100)
    return _processor.charge(discounted, currency_code.upper())
