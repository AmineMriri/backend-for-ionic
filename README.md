# backend-for-ionic


- virtualenv env
- source env/bin/activate
- pip install requirements.txt
- python3 manage.py makemigrations
- python3 manage.py migrate
- python3 manage.py runserver

# you should find ur api endpoints here : 
    -http://127.0.0.1:8002/api/posts # To get all posts
    -http://127.0.0.1:8002/api/posts/<id> # To get post by id
    -http://127.0.0.1:8002/api/posts/create # to create a post with the schema : 
        {
            "title": "title",
            "content": "Content",
            "author": "author",
            "image": image
        }
    -http://127.0.0.1:8002/api/posts/update/<id> # to update an existing post
    -http://127.0.0.1:8002/api/posts/delete/<id> # to delete an existing post