# import sqlite3
#
# conn = sqlite3.connect("Example.db")
#
# myCursor = conn.cursor()

# myCursor.execute("""
#             CREATE TABLE users (name text, age integer)
# """)

# myCursor.execute("""
#     INSERT INTO users(name, age) values (:name , :age)
# """, {'name': 'majid', 'age': 40})
#
# conn.commit()
# sql = """
#         INSERT INTO users (name , age) values (:name, :age)
# """
#
# val = [("reza", 34), ("iran",45)]
#
# myCursor.executemany(sql, val)
#
# myCursor.execute("SELECT * FROM users")
#
# result = myCursor.fetchall()
# print(result)
