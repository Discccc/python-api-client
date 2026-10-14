from config import API_KEY
from api_client import get_data,post_data



headers={
    "Authorization":f"Bearer {API_KEY}"
}
data=get_data(url="https://jsonplaceholder.typicode.com/posts/1",
              headers=headers)
print (data)

data2= {
    "title": "hello",
    "body": "python api test",
    "userId": 1
}
result=post_data(url="https://jsonplaceholder.typicode.com/posts",
                json=data2,
                headers=headers)
print(result)