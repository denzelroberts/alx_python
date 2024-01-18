#import MySQLdb & sys & alchemy
#import sqlalchemy
import MySQLdb
from sys import argv

#connecting to mysqldb
db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])

#getting a cursor 
cur = db.cursor()

cur.execute("SELECT cities.name FROM cities\
                INNER JOIN states ON cities.state_id = states.id\
                WHERE states.name = %s ORDER BY cities.id",
                (argv[4], ))

myresult = cur.fetchall()
first = 0

for city in myresult:
    if first != 0:
        print(", ", end="")
        print("%s" % city, end="")
        first += 1

print("")
# Close all cursors
cur.close()
# Close all databases
db.close()