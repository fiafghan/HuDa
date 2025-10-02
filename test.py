from huda.API import api_load


df = api_load("https://jsonplaceholder.typicode.com/posts", {"id":1})
    
print (df)