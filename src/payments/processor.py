"""Payment processor — core domain logic."""

from __future__ import annotations

SUPPORTED_CURRENCIES = {"USD", "EUR", "GBP", "JPY", "AUD", "CAD", "CHF", "SGD"}


class PaymentError(Exception):
    pass


class PaymentProcessor:
    """Process payments.

    Currency rules (enforced here, mirrored in DB check constraint):
      - Must be ISO 4217: exactly 3 uppercase ASCII letters.
      - Must be in SUPPORTED_CURRENCIES — any other value raises PaymentError.
    Amount rules:
      - Must be > 0.
      - Rounded to 2 decimal places before processing.
    """

    def charge(self, amount: float, currency: str) -> dict:
        if amount <= 0:
            raise PaymentError(f"Amount must be positive, got {amount}")

        # Currency MUST be exactly 3 uppercase ASCII chars — lowercase input
        # is NOT silently normalised; callers are responsible for uppercasing.
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
