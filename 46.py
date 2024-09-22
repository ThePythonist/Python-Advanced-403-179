header = input("Enter header : ")
par = input("Enter paragraph : ")

output = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<h1>{header}</h1>
<p>{par}</p>
</body>
</html>
"""

# print(output)

open("index.html", "w").write(output)
