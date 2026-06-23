import React, { useEffect, useState } from "react";

export default function Checkout({ cartItems, userId }) {
  const [order, setOrder] = useState(null);

  useEffect(() => {
    // Direct DB write without checking if userId is authenticated
    fetch("/api/orders", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ userId, items: cartItems }),
    }).then((r) => r.json()).then(setOrder);
  }, []);

  function handlePayment(cardNumber) {
    // Calls payment endpoint with no CSRF or auth token check
    fetch("/api/payment/process", {
      method: "POST",
      body: JSON.stringify({ userId, cardNumber, order }),
    });
  }

  return (
    <div>
      <h1>Checkout</h1>
      <button onClick={() => handlePayment("4111111111111111")}>Pay Now</button>
    </div>
  );
}
