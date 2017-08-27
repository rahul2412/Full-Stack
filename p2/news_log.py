#! /usr/bin/env python3
import psycopg2


def databaseOpen(a):
    """connects to news database and returns result of query a"""
    db = psycopg2.connect(database="news")
    cur = db.cursor()
    cur.execute(a)
    return cur.fetchall()
    close()


def query_results(result):
    """Prints a formatted result for the queries of first 2 questions"""
    for i in result:
        print ("\t" + i[0] + " - " + str(i[1]) + " views")


def alt_query(result):
    """Prints a formatted result for the third query"""
    for i in result:
        print ("\t" + i[0] + " - " + str(i[1]) + "% errors")


query1 = ("select title, count(*) as views_no from articles "
          "inner join log on path like concat('%',slug) "
          "group by title order by views_no desc limit 3")

query2 = ("select name, count(*) as total_no from authors inner "
          "join articles on authors.id = author inner join log "
          "on path like CONCAT('%', slug) group by name order by "
          "total_no desc")

query3 = ("select days, per from (select days, "
          "round((sum(requests)/(select count(*) from log where "
          "substring(cast(log.time as text), 0, 11) = days) * 100), 2) "
          "as per from (select substring(cast(log.time as text), 0, 11) "
          "as days,count(*) as requests from log where status like '4%' "
          "group by days) as per_log group by days order by per desc) "
          "as final where per >= 1")

"""questions are asked then psql server is connected for answering them"""
print ("What are the most popular three articles of all time?")
query_results(databaseOpen(query1))

print ("Who are the most popular article authors of all time?")
databaseOpen(query2)
query_results(databaseOpen(query2))

print ("On which days did more than 1% of requests lead to errors?")
alt_query(databaseOpen(query3))
