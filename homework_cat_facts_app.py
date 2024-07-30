import requests
import sqlite3

# Send a GET request to the API and retrieve the data
url='https://catfact.ninja/facts'
#url = "https://cat-fact.herokuapp.com/facts"  url Failed to retrieve data. I changed it because it returned HTTP Status code: 503 error.
response = requests.get(url)
data = response.json()
print(data)  # Print the JSON data
   
# Connect to SQLite database (or create it if it doesn't exist)
# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('cat_facts.db')
cursor = conn.cursor()

# Drop the table if it exists to avoid schema conflicts 
#cursor.execute('DROP TABLE IF EXISTS cat_facts') I have cleaned up the table so that it does not write the same data multiple times due to error corrections.

# Create table with the correct schema
cursor.execute('''
CREATE TABLE cat_facts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fact TEXT,
    length INTEGER
)
''')

# Insert the cat facts into the table
for fact_data in data['data']:
    fact = fact_data['fact']
    length = fact_data['length']
    cursor.execute('INSERT INTO cat_facts (fact, length) VALUES (?, ?)', (fact, length))

# Commit changes and close the connection
conn.commit()

# Retrieve and display the cat facts saved in the database
cursor.execute('SELECT * FROM cat_facts')
saved_facts = cursor.fetchall()

conn.close()

for fact in saved_facts:
    print(fact)
    
print('Finished')    