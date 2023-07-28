import sqlite3
import json
from models import Order, Metal, Size, Style


def get_all_orders():
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
            SELECT
                o.id,
                o.metal_id,
                o.size_id,
                o.style_id,
                m.metal metal_name,
                m.price metal_price,
                z.carets size_carets,
                z.price size_price,
                s.style style_name,
                s.price style_price     
            FROM `Order` o
            JOIN Metal m 
                ON m.id = o.metal_id
            JOIN Size z
                ON z.id = o.size_id
            JOIN Style s
                ON s.id = o.style_id
            """)

        # Initialize an empty list to hold all order representations
        orders = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an animal instance from the current row
            order = Order(row['id'], row['metal_id'],
                          row['size_id'], row['style_id'])

            metal = Metal(row['id'], row['metal_name'], row['metal_price'])

            size = Size(row['id'], row['size_carets'], row['size_price'])

            style = Style(row['id'], row['style_name'], row['style_price'])

            # Add the dictionary representation of the animal to the list
            order.metal = metal.__dict__

            order.size = size.__dict__

            order.style = style.__dict__

            orders.append(order.__dict__)

    return orders


def get_single_order(id):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
            SELECT
                o.id,
                o.metal_id,
                o.size_id,
                o.style_id,
                m.metal metal_name,
                m.price metal_price,
                z.carets size_carets,
                z.price size_price,
                s.style style_name,
                s.price style_price     
            FROM `Order` o
            JOIN Metal m 
                ON m.id = o.metal_id
            JOIN Size z
                ON z.id = o.size_id
            JOIN Style s
                ON s.id = o.style_id
            WHERE o.id = ?
            """, (id, ))

        # Load the single result into memo
        orders = []

        dataset = db_cursor.fetchone()

        for row in dataset:
            # Create an animal instance from the current row
            order = Order(row['id'], row['metal_id'],
                          row['size_id'], row['style_id'])

            metal = Metal(row['id'], row['metal_name'], row['metal_price'])

            size = Size(row['id'], row['size_carets'], row['size_price'])

            style = Style(row['id'], row['style_name'], row['style_price'])

            order.metal = metal.__dict__

            order.size = size.__dict__

            order.style = style.__dict__

            orders.append(order.__dict__)

        return order.__dict__


def create_orders(order):
    # Get the id value of the last animal in the list
    max_id = ORDERS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the animal dictionary
    order["id"] = new_id

    # Add the animal dictionary to the list
    ORDERS.append(order)

    # Return the dictionary with `id` property added
    return order


def delete_order(id):
    delete_index = -1

    for index, order in enumerate(ORDERS):
        if order["id"] == id:
            # Found the animal. Store the current index.
            delete_index = index

    # If the animal was found, use pop(int) to remove it from list
    if delete_index >= 0:
        ORDERS.pop(delete_index)


def update_order(id, new_order):
    # Iterate the ANIMALS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, order in enumerate(ORDERS):
        if order["id"] == id:
            # Found the animal. Update the value.
            ORDERS[index] = new_order
            break
