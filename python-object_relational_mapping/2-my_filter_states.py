#!/usr/bin/python3
"""Displays all values in the states table of hbtn_0e_0_usa
where name matches the argument.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get arguments: username, password, database, and state name
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor to execute queries
    cur = db.cursor()

    # Build the SQL query using format (not safe, but required for this task)
    query = (
        "SELECT * FROM states "
        "WHERE name LIKE BINARY '{}' "
        "ORDER BY id ASC"
    ).format(state_name)
    cur.execute(query)

    # Fetch and print all matching rows
    for row in cur.fetchall():
        print(row)

    # Clean up
    cur.close()
    db.close()
