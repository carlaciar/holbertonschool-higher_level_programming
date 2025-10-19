#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL credentials and database name from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL server running on localhost at port 3306
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor object to interact with the database
    cur = db.cursor()

    # Execute the SQL query to select all states ordered by id
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all rows from the result
    rows = cur.fetchall()

    # Display the results as tuples (id, name)
    for row in rows:
        print(row)

    # Close cursor and connection
    cur.close()
    db.close()
