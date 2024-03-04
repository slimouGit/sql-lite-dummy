import sqlite3

def main():
    # Establish connection to SQLite database
    conn = sqlite3.connect('example.db')

    # Create a cursor object
    c = conn.cursor()

    # Drop the table if it already exists
    c.execute("DROP TABLE IF EXISTS goods")

    # Create a table
    c.execute('''CREATE TABLE goods
                 (name text, description text, price real)''')

    # Insert data
    c.execute("INSERT INTO goods VALUES ('Chicken Nuggets', 'Delicious chicken nuggets', 35.14)")
    c.execute("INSERT INTO goods VALUES ('Chicken Nuggets', 'Delicious chicken nuggets', 35.14)")

    # Commit the changes
    conn.commit()

    # Fetch all rows
    c.execute('SELECT * FROM goods')
    print(c.fetchall())

    # Close the connection
    conn.close()

if __name__ == '__main__':
    main()