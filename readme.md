# Blogv3

## setup

    virtualenv ~/.virtualenv/blogv3
    source ~/.virtualenv/blogv3/bin/activate/
    pip install -r requirements.txt
    ./manage.py migrate
    ./manage.py runserver

## Model Design

Post

* title
* author
* likes
* content

User

* name
* age

Comments

* foreign key to post
* text field

Likes

* foreign key to post
* foreign key to user

## Agenda

* DRF
* Basic AUTH Scheme
* View: Add, owner, update, delete, permissions
* django auth user
* create post
* create comments
* create likes
* viewing posts of author with all its comments

## End Points

    POST /posts/
    {title, body} -> {id, author}

    GET /posts/{id}/
    {author, title, body, comments:[{body}, {body}]}

    POST /comments/
    {body, post:id} -> {id:}

    POST /likes/
    {post:} -> {id:}

## Goal

* display posts liked by user

    GET /users/{id}/
    -> {posts_liked:[{title:}, {title:}]}
