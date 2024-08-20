import sys
print('This is an error message', file=sys.stderr)

# class A:
#     def sayhello(self):
#         print("Hello")
#
#
# class B(A):
#     def saygoodbye(self):
#         print("Goodbye")
#
#
# valed = A()
# farzand = B()

# ------------------------------------------------------------------------------------------

# class Father:
#     def __init__(self, fname, eyecolor, city, job):
#         self.familyname = fname
#         self.eyecolor = eyecolor
#         self.city = city
#         self.job = job
#
#     def sayhello(self):
#         print("Hello")
#
#
# class Child(Father):
#     def __init__(self, fname, eyecolor, city, job, studentid, fieldofstudy):
#         # --- Inherited ---
#         super().__init__(fname, eyecolor, city, job)
#
#         # --- Not Inherited ---
#         self.studentid = studentid
#         self.fieldofstudy = fieldofstudy
#
#     def saygoodbye(self):
#         print("Goodbye")
#
#
# ahmad = Father("mohammadi", "black", "arak", "teacher")
# ali = Child("mohammad", "brown", "tehran", "engineer", "11001", "computer engineering")
#
# print(ali.fieldofstudy)
# ------------------------------------------------------------------------------------------