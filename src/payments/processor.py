"""Payment processor — core domain logic."""

from __future__ import annotations

SUPPORTED_CURRENCIES = {"USD", "EUR", "GBP", "JPY", "AUD", "CAD", "CHF", "SGD"}

# Internal fraud cap: single charge must not exceed this amount in any currency.
# This is a hard backend limit — NOT enforced at the API/frontend layer.
# Callers must split large orders before calling charge().
MAX_CHARGE_AMOUNT = 9999.99


class PaymentError(Exception):
    pass


class PaymentProcessor:
    """Process payments.

    Constraints (all enforced here; callers are responsible):
      - amount: 0 < amount <= MAX_CHARGE_AMOUNT (9999.99). Exceeding the cap
        raises PaymentError — it is NOT silently capped or split.
      - currency: exactly 3 uppercase ASCII letters in SUPPORTED_CURRENCIES.
    """

    def charge(self, amount: float, currency: str) -> dict:
        if amount <= 0:
            raise PaymentError(f"Amount must be positive, got {amount}")

        if amount > MAX_CHARGE_AMOUNT:
            raise PaymentError(
                f"Single charge exceeds fraud cap ({amount} > {MAX_CHARGE_AMOUNT}). "
                "Split the order before calling charge()."
            )

        if not (isinstance(currency, str) and len(currency) == 3 and currency.isupper()):
            raise PaymentError(
                f"Invalid currency '{currency}': must be 3 uppercase ASCII letters (ISO 4217)"
            )

        if currency not in SUPPORTED_CURRENCIES:
            raise PaymentError(
                f"Unsupported currency '{currency}'. Supported: {sorted(SUPPORTED_CURRENCIES)}"
            )

        return {
            "status": "charged",
            "amount": round(amount, 2),
            "currency": currency,
        }
