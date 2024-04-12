import psycopg2

conn = psycopg2.connect(host="localhost", dbname="postgres",
                        user="postgres", password="Critflaw!23", port=5432)

cur = conn.cursor()  # used to execute commands in postgres

# Can be thought of as columns for the table
cur.execute("""CREATE TABLE IF NOT EXISTS members  (
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    email VARCHAR(255),
    phone_number VARCHAR(255),
    username VARCHAR(255),
    password VARCHAR(255)
);
""")

# Assigns values to each of the values above
# Remember: You must delete the table in pgAdmin4 to rerun or you will get an error, otherwise comment out code
# cur.execute("""INSERT INTO members (first_name, last_name, email, phone_number, username, password) VALUES
# ('', '', '', '', '', ''),
# ('Brandon', 'Rasgaitis', 'brasgaitis97@gmail.com', '7073459866', 'bran123', 'YashaApe!2748$'),
# ('Kevin', 'Berberich', 'berberator97@gmail.com', '6073459867', 'kberb123', 'Kev!@#'),
# ('Kyle', 'Kolod', 'kkolod97@gmail.com', '6073459868', 'kkolod123', 'Kolod!@#'),
# ('Zach', 'Shulchz', 'zshulchz97@gmail.com', '7073459869', 'zshulchz123', 'Schulchz!@#'),
# ('Josh', 'Jackson', 'jjackson97@gmail.com', '7073459870', 'jjackson123', 'Jackson!@#'),
# ('Bobby', 'Bobbenson', 'bobby97@gmail.com', '8073459866', 'bobby123', 'Bobby!@#');
# """)

# Select some values
cur.execute("""SELECT * FROM members WHERE first_name = 'Brandon';""")

# cur.fetchone() gives only 1 result
print(cur.fetchone())
print()

# print out individual rows to the terminal
cur.execute("""SELECT * FROM members WHERE starts_with(phone_number, %s);""", "7")
for row in cur.fetchall():
    print(row)
print()

# Can't use built in methods for prepared statements, idk what that means
# Use cur.mogrify() to format in multiple values
# Good for trying to get values based on specific set of criteria
sql = cur.mogrify("""SELECT * FROM members WHERE first_name LIKE 'K%%' AND password LIKE '%%!@#%%';""")
print(sql)
print()
cur.execute(sql)
print(cur.fetchall())

conn.commit()

cur.close()
conn.close()
