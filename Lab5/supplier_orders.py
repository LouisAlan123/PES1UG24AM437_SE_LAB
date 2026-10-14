"""Supplier purchase order tracker for the stores department."""
import logging
import sqlite3


def create_connection():
    """Create an in-memory database containing the orders table."""
    connection = sqlite3.connect(":memory:")
    connection.execute(
        "CREATE TABLE orders (id INTEGER PRIMARY KEY, supplier TEXT, "
        "item TEXT, quantity INTEGER, received INTEGER)"
    )
    return connection


def place_order(connection, supplier, item, quantity):
    """Insert a new, not yet received order for a supplier."""
    connection.execute(
        "INSERT INTO orders (supplier, item, quantity, received) "
        "VALUES (?, ?, ?, 0)",
        (supplier, item, quantity),
    )


def mark_received(connection, order_id):
    """Mark the order with the given id as received."""
    connection.execute(
        "UPDATE orders SET received = 1 WHERE id = ?", (order_id,)
    )


def notify_warehouse(supplier):
    """Tell the warehouse that a delivery from a supplier arrived."""
    print("notifying warehouse about " + supplier)


def cleanup(connection):
    """Delete orders that have already been received."""
    try:
        connection.execute("DELETE FROM orders WHERE received = 1")
    except sqlite3.Error:
        logging.exception("Cleanup of received orders failed")


def pending_count(connection):
    """Return the number of orders that have not been received yet."""
    query = "SELECT COUNT(*) FROM orders WHERE received = 0"
    return connection.execute(query).fetchone()[0]


def total_quantity(connection):
    """Return the total quantity of all orders currently stored."""
    query = "SELECT COALESCE(SUM(quantity), 0) FROM orders"
    return connection.execute(query).fetchone()[0]


def main():
    """Place sample orders, receive one and report the status."""
    connection = create_connection()
    place_order(connection, "Acme Steel", "rods", 40)
    place_order(connection, "Bolt Co", "bolts", 500)
    order_total = total_quantity(connection)
    mark_received(connection, 1)
    notify_warehouse("Acme")
    print(pending_count(connection), order_total)
    cleanup(connection)


if __name__ == "__main__":
    main()
