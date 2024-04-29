### Task 2

● Create a new database named website.

● Create a new table named member, in the website database, designed as below:
```python
cursor.execute("CREATE DATABASE website")
cursor.execute(
     """CREATE TABLE member (
             id BIGINT PRIMARY KEY AUTO_INCREMENT,
             name VARCHAR(255) NOT NULL,
             username VARCHAR(255) NOT NULL,
             password VARCHAR(255) NOT NULL,
             follower_count INT UNSIGNED NOT NULL DEFAULT 0,
             time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
             UNIQUE(id)
           )""")
 cursor.execute("INSERT INTO member(name, username, password, follower_count) VALUES('test','test','test',7)")
```

![alt text](<截圖 2024-04-29 下午5.08.37.png>)

![alt text](<截圖 2024-04-29 下午5.08.55.png>)


### Task 3

● INSERT a new row to the member table where name, username and password must be set to test. INSERT additional 4 rows with arbitrary data.

● SELECT all rows from the member table.

```python 
cursor.execute("INSERT INTO member(name, username, password, follower_count) VALUES('test','test','test',7)")
```
![alt text](<截圖 2024-04-29 下午5.09.56.png>)


● SELECT all rows from the member table, in descending order of time.

```python 
cursor.execute("SELECT * FROM member ORDER BY time DESC")
```
![alt text](<截圖 2024-04-29 下午5.36.45.png>)

● SELECT total 3 rows, second to fourth, from the member table, in descending order
of time. Note: it does not mean SELECT rows where id are 2, 3, or 4.

```python
cursor.execute("SELECT * FROM member ORDER BY time DESC LIMIT 1, 3")
```
![alt text](<截圖 2024-04-29 下午5.37.58.png>)
● SELECT rows where username equals to test.

```python
cursor.execute("SELECT * FROM member WHERE name='test' ")
```
![alt text](<截圖 2024-04-29 下午5.39.53.png>)

● SELECT rows where name includes the es keyword.

```python
cursor.execute("SELECT * FROM member WHERE name LIKE '%es%' ")
```
![alt text](<截圖 2024-04-29 下午5.41.12.png>)

● SELECT rows where both username and password equal to test.

```python
cursor.execute("SELECT * FROM member WHERE name='test' AND password='test' ")
```
![alt text](<截圖 2024-04-29 下午5.42.07.png>)

● UPDATE data in name column to test2 where username equals to test.

```python
cursor.execute("UPDATE member SET name='test2' WHERE name='test' ")
```
![alt text](<截圖 2024-04-29 下午5.43.52.png>)

### Task 4

● SELECT how many rows from the member table.

```python
cursor.execute("SELECT COUNT(*) FROM member")
``` 
![alt text](<截圖 2024-04-29 下午5.48.25.png>)

● SELECT the sum of follower_count of all the rows from the member table.

```python
cursor.execute("SELECT SUM(follower_count) FROM member")
```
![alt text](<截圖 2024-04-29 下午5.49.56.png>)

● SELECT the average of follower_count of all the rows from the member table.

```python
cursor.execute("SELECT AVG(follower_count) FROM member")
```
![alt text](<截圖 2024-04-29 下午5.50.22.png>)

● SELECT the average of follower_count of the first 2 rows, in descending order of
follower_count, from the member table.

```python
cursor.execute("SELECT AVG(follower_count) FROM(SELECT follower_count FROM member ORDER BY follower_count DESC LIMIT 2) AS subquery")
```
![alt text](<截圖 2024-04-29 下午5.51.59.png>)

### TASK 5

● Create a new table named message, in the website database. designed as below:

```python
cursor.execute("""
        CREATE TABLE message(
            id BIGINT PRIMARY KEY AUTO_INCREMENT,
            member_id BIGINT NOT NULL,
            content VARCHAR(255) NOT NULL,
            like_count INT UNSIGNED NOT NULL DEFAULT 0,
            time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(member_id) REFERENCES member(id),
            UNIQUE(id)
           )
        """)
```
![alt text](<截圖 2024-04-29 下午6.03.46.png>)

● SELECT all messages, including sender names. We have to JOIN the member table to get that.

```python
cursor.execute("""
               SELECT message.*,member.name AS sender_names 
               FROM message 
               JOIN member 
               ON member.id=message.member_id
              """)
```
![alt text](<截圖 2024-04-29 下午6.04.47.png>)

● SELECT all messages, including sender names, where sender username equals to test. We have to JOIN the member table to filter and get that.

```python
cursor.execute("""
            SELECT * FROM (
                SELECT message.*,member.name AS sender_names 
                FROM message 
                JOIN member 
                ON member.id=message.member_id
                ) AS sender_names WHERE sender_names='test'
            """)
```
![alt text](<截圖 2024-04-29 下午6.07.03.png>)

● Use SELECT, SQL Aggregation Functions with JOIN statement, get the average like count of messages where sender username equals to test.

```python
cursor.execute("""
            SELECT AVG(like_count) FROM (
                SELECT message.*,member.name AS sender_names 
                FROM message 
                JOIN member 
                ON member.id=message.member_id
                ) AS sender_names WHERE sender_names='test'
            """)
```
![alt text](<截圖 2024-04-29 下午6.08.06.png>)

● Use SELECT, SQL Aggregation Functions with JOIN statement, get the average like count of messages GROUP BY sender username.

```python
cursor.execute("""
            SELECT sender_names, AVG(like_count) FROM (
                SELECT message.*,member.name AS sender_names 
                FROM message 
                JOIN member 
                ON member.id=message.member_id
                ) AS sender_names GROUP BY sender_names
            """)
```
![alt text](<截圖 2024-04-29 下午6.09.32.png>)