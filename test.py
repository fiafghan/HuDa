from huda.mysql import open_mysql

df = open_mysql("Select * from users", host="localhost", port=3306, 
                        user="root", password="", database="iumsdb")

print (df)