import mysql.connector

con=mysql.connector.connect(
    user="root",
    password="betty520",
    host="localhost",
    database="website"
)
cursor=con.cursor()

# cursor.execute("CREATE DATABASE website")
# cursor.execute(
#     """CREATE TABLE member (
#             id BIGINT PRIMARY KEY AUTO_INCREMENT,
#             name VARCHAR(255) NOT NULL,
#             username VARCHAR(255) NOT NULL,
#             password VARCHAR(255) NOT NULL,
#             follower_count INT UNSIGNED NOT NULL DEFAULT 0,
#             time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
#             UNIQUE(id)
#             )""")
# cursor.execute("INSERT INTO member(name, username, password, follower_count) VALUES('test','test','test',7)")

# cursor.execute("SELECT * FROM member")

# cursor.execute("SELECT * FROM member ORDER BY time DESC LIMIT 1, 3")

# cursor.execute("SELECT * FROM member WHERE name='test' ")

# cursor.execute("SELECT * FROM member WHERE name LIKE '%es%' ")

# cursor.execute("SELECT * FROM member WHERE name='test' AND password='test' ")

# data=cursor.fetchall()
# print(data)

# cursor.execute("UPDATE member SET username='test2' WHERE username='test' ")

# cursor.execute("SELECT COUNT(*) FROM member")

# cursor.execute("SELECT SUM(follower_count) FROM member")

# cursor.execute("SELECT AVG(follower_count) FROM member")

# cursor.execute("SELECT AVG(follower_count) FROM(SELECT follower_count FROM member ORDER BY follower_count DESC LIMIT 2) AS subquery")


# data=cursor.fetchone()
# print(data[0])
# cursor.execute("""
#         CREATE TABLE message(
#             id BIGINT PRIMARY KEY AUTO_INCREMENT,
#             member_id BIGINT NOT NULL,
#             content VARCHAR(255) NOT NULL,
#             like_count INT UNSIGNED NOT NULL DEFAULT 0,
#             time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
#             FOREIGN KEY(member_id) REFERENCES member(id),
#             UNIQUE(id)
#            )
#         """)
# cursor.execute("""
#                SELECT message.*,member.name AS sender_names 
#                FROM message 
#                JOIN member 
#                ON member.id=message.member_id
#               """)
cursor.execute("""
            SELECT * FROM (
                SELECT message.*,member.name AS sender_names 
                FROM message 
                JOIN member 
                ON member.id=message.member_id
                WHERE member.username='test'
                )AS subquery 
            """)
# cursor.execute("""
#             SELECT AVG(like_count) FROM (
#                 SELECT message.*,member.name AS sender_names 
#                 FROM message 
#                 JOIN member 
#                 ON member.id=message.member_id
#                 ) AS sender_names WHERE sender_names='test'
#             """)
# cursor.execute("""
#             SELECT sender_names, AVG(like_count) FROM (
#                 SELECT message.*,member.name AS sender_names 
#                 FROM message 
#                 JOIN member 
#                 ON member.id=message.member_id
#                 ) AS sender_names GROUP BY sender_names
#             """)
                
# cursor.execute("INSERT INTO message(member_id, content, like_count) VALUES(5,'LIKE ME?',2)")
# cursor.execute("SELECT * FROM message")
# cursor.execute("UPDATE member SET name='test' WHERE name='test2' ")

data=cursor.fetchall()
print(data)
con.commit()
con.close()
