from huda.mysql import open_mysql

df = open_mysql("localhost", 3306, "root", "", "iumsdb", "users")
print(df)