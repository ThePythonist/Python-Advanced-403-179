from random import randint

comments = []


class User:
    def __init__(
            self,
            username,
            password,
            email,
            phonenumber
    ):
        self.username = username
        self.password = password
        self.email = email
        self.phonenumber = phonenumber

    def leave_comment(self, text):
        comments.append({"01": {self.username: text}})

    def login(self, username, password):
        if username == self.username and password == self.password:
            print("Successfully logged in")
        else:
            print("Incorrect Credentials")
