from huda.API import open_api

df = open_api("https://jsonplaceholder.typicode.com/posts",
{
    "userId":2
})
print(df)