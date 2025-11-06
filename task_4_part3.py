orders = {
    101: {
        "customer_name": "Ahmed Ali",
        "email": "ahmed@example.com",
        "items": {
            "notebook": {"price": 20.0, "quantity": 2},
            "pen": {"price": 2.5, "quantity": 5},
        },
        "status": "Processing"
    },
    102: {
        "customer_name": "Sara Mohamed",
        "email": "sara@example.com",
        "items": {
            "mug": {"price": 10.0, "quantity": 1},
            "t-shirt": {"price": 25.0, "quantity": 2},
        },
        "status": "Pending"
    }
}


print("\n----- All Orders -----")
for order_id, order in orders.items():
    print(f"Order ID: {order_id}")
    print(f"  Customer: {order['customer_name']}")
    print(f"  Email: {order['email']}")
    print(f"  Status: {order['status']}")
    print("  Items:")
    for item, info in order["items"].items():
        print(f"    - {item}: {info['quantity']} × {info['price']}")
    print()


for order_id, order in orders.items():
    total = sum(info["price"] * info["quantity"] for info in order["items"].values())
    print(f"Total for order {order_id}: {total}")


orders[101]["status"] = "Delivered"


orders[103] = {
    "customer_name": "Mona Saleh",
    "email": "mona@example.com",
    "items": {
        "keyboard": {"price": 45.0, "quantity": 1},
        "mouse": {"price": 15.0, "quantity": 1}
    },
    "status": "Processing"
}


print("\nUpdated Orders:")
for order_id, order in orders.items():
    print(f"{order_id}: {order['customer_name']} - {order['status']}")
