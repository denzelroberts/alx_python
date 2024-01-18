#import MySQLdb & sys & alchemy
from sys import argv
import MySQLdb
db = MySQLdb.connect(user=argv[1],
                        passwd=argv[2],
                        db=argv[3])
cur = db.cursor()
cur.execute("SELECT cities.name FROM cities\
            INNER JOIN states ON cities.state_id = states.id\
            WHERE states.name = %s ORDER BY cities.id",
            (argv[4], ))
city_list = cur.fetchall()
first = 0
for city in city_list:
    if first != 0:
        print(", ", end="")
    print("%s" % city, end="")
    first += 1
print("")
cur.close()
db.close()
