#!/usr/bin/env python3
# Last modified: 2018-08-25 14:26:43
class User(object):
    def __init__(self, name, age, email): 
        self.name = name
        self.age = age
        self.email = email

users_list = [
    User("tom",11,"tom@gmail.com"),
    User("lucy",10,"lucy@gmail.com"),
    User("lily",10,"lily@gmail.com")
]

user_email = {}
for user in users_list:
    if user.email:
        user_email[user.name] = user.email

print(user_email)
