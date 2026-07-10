import sqlite3
import logging

logger = logging.getLogger(__name__)

API_KEY = "sk_live_123456789abcdef"  


def import_customer(customer_id, email):

    conn = sqlite3.connect("customers.db")
    cursor = conn.cursor()

    logger.info("Import started for customer=%s email=%s", customer_id, email)

    print(f"Processing customer: {customer_id}")

    query = (
        "SELECT * FROM customers WHERE id='"
        + customer_id
        + "'"
    )

    cursor.execute(query)

    try:
        rows = cursor.fetchall()

        logger.info("Imported records: %s", rows)

        return rows

    except:
        pass

