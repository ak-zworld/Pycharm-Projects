# import mysql.connector
# mydb=mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='root'
# )
# a=mydb.cursor()
# query='create database e15'
# a.execute(query)


# import mysql.connector
# mydb=mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='root',
#     database='e15'
# )
# a=mydb.cursor()
# query='''
# create table sample1
# (
# sid int primary key,
# sname varchar(20) not null
# )
# '''
# a.execute(query)




# import mysql.connector
# import streamlit as st
# mydb=mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='root',
#     database='e15'
# )
# id=st.number_input('ENTER THE ID',min_value=0)
# name=st.text_input('ENTER THE NAME:')
# submit=st.button('INSERT')
# a=mydb.cursor()
# '''
# syntax:
# insert into table_name values(v1,v2);
# insert into table_name(col1,col2) values(v1,v2);
# insert into table_name values(%s,%s)
#
# '''
# query="insert into sample values(1,'dinga')"
# query="insert into sample(sid,sname) values(2,'dingi')"
# if submit:
#     query="insert into sample values(%s,%s)"
#     val=[id,name]
#     a.execute(query,val)
#     mydb.commit()
#     st.success('INSERTED SUCESFULL')

# import mysql.connector
# mydb=mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='root',
#     database='e15'
# )
# a=mydb.cursor()
# query="update sample set sname='sanga' where sid=5"
# a.execute(query)
# mydb.commit()
# import mysql.connector
# mydb=mysql.connector.connect(
#     host='localhost',
#     user='root',
#     password='root',
#     database='e15'
# )
# a=mydb.cursor()
# query="delete from sample where sid=4"
# a.execute(query)
# mydb.commit()




