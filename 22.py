from models import User, comments


class Admin(User):
    def __init__(self, username, password, email, phonenumber, role):
        super().__init__(username, password, email, phonenumber)
        self.role = role
        self.actions = []

    def approve_request(self):
        print("Request approved")
        self.actions.append("approve_request")

    def reject_request(self):
        print("Request rejected")
        self.actions.append("reject_request")

    def remove_comment(self, id):
        comments.pop(id)
        self.actions.append(f"removed comment {id}")


armin = User("armin021", "123", "armin@gmail.com", "09126604030")
mamad = User("mamad_khafan", "123", "mamad@gmail.com", "091337204001")
aghareza = Admin("khodereza", "123", "reza@gmail.com", "0912372042244", "manager")

armin.leave_comment("01", "awesome!")
mamad.leave_comment("02", "dadashami 💋")

print(comments)

aghareza.remove_comment("02")

print(comments)
