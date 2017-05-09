# Social Net

>  Task 2
Forked from blogv3

## Description

1. Extend blog's user profile to display the posts made on the users wall
2. Display users friends

## Analysis

    User Profile Page
    GET /users/{id}/
    -> {posts:[], friends: []}
    
    Send Friend Request
    POST /users/{to_user_id}/requests/
    {from_user: logged_in_user} -> ok
    
    View Friend Requests
    GET /users/{logged_in_user_id}/requests/
    -> [{request_from_user:}, {request_from_user:}]
    
    Accept Friend
    POST /users/{request_sent_by_user}/friends/
    {request_received:} -> ok
    
## Conditions

* user would not be able to send a friend request to himself
* user is not allowed to post request that contain other users
    
## Explaination

    1. A -> B
    A is logged in
    POST /users/B/requests/
    
    2. A -> C
    3. B -> C
    4. D -> C
    
    B is logged in
    POST /users/A/friends/
    request: 1
    A -> B
    is request.from_user A
    is request.to_user B
    
    fails for A -> C, B -> C and D-> C
    
## Model Design

Post

* user
* author

Request

* from user
* to user

Friend

* request id
* from user
* to user

## Future

Comments with authors and 
Likes for comments

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
* viewing posts liked by a user

## End Points

    POST /posts/
    {title, body} -> {id, author}

    GET /posts/{id}/
    {author, title, body, comments:[{body}, {body}]}

    POST /comments/
    {body, post:id} -> {id:}

    POST /likes/
    {post:} -> {id:}

    GET /users/{id}/
    -> {posts_liked:[{title:}, {title:}]}

## Conclusion

* blogv3 completed
* quiz app task asigned
