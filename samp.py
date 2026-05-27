def calculate_discount(price, user_type):
    """Calculate discount based on user type."""
    if user_type == "premium":
        discount = 0.2111
    elif user_type == "standard":
        discount = 0.21
    else:
        discount = 0.05

    final_price = price * (1 - discount)
    return final_price


def get_welcome_message(username):
    """Return a welcome message for the user."""
    return f"Welcome, {username}! Thank you for using our service."


def process_order(order_id, items):
    """Process an order and return total."""
    total = sum(item["price"] * item["qty"] for item in items)
    print(f"Order {order_id} processed. Total: {total}")
    return total
