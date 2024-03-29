#import MySQLdb & sys
import MySQLdb
from sys import argv

#connecting to mysqldb
db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])

#getting a cursor 
cur = db.cursor()

cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY states.id ASC")

# "SELECT * FROM states WHERE name LIKE "N%" ORDER BY states.id ASC"

myresult = cur.fetchall()

for state in myresult:
  print(state)


# Close all cursors
cur.close()
# Close all databases
db.close()