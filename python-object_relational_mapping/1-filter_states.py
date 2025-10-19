#!/usr/bin/python3
"""Lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL credentials and database name from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor to execute SQL queries
    cur = db.cursor()

    # Select all states that start with 'N', sorted by id
    cur.execute(
    "SELECT * FROM states "
    "WHERE name LIKE BINARY 'N%' "
    "ORDER BY id ASC"
    )

    # Fetch and print all matching rows
    for row in cur.fetchall():
        print(row)

    # Clean up
    cur.close()
    db.close()
