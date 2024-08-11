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
        pass


# Example usage:
# admin = Admin("john", "password", "john@example.com", "09126256040", "editor", 5)
# print(admin.username)  # Output: john
# print(admin.role)  # Output: admin
# print(admin.experience)  # Output: 5
# admin.leave_comment("Hello!")  # Output: Hello!
# admin.login("john", "password")  # Output: Successfully logged in
# admin.approve_request()  # Output: Request approved
# admin.reject_request()  # Output: Request rejected
# admin.add_report("Report 1")
# admin.add_report("Report 2")
# admin.view_reports()  # Output: Reports
