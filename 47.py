people = [
    {"name": "farhad", "job": "front-end dev", "age": 31},
    {"name": "arian", "job": "back-end dev", "age": 29},
    {"name": "kiana", "job": "front-end dev", "age": 24},
    {"name": "mehran", "job": "database admin", "age": 40},
    {"name": "soraya", "job": "human resource", "age": 35},
]

html = """<!DOCTYPE html>
<html>
<head>
<style>

body {
    background-color:black;
    color:white;
    font-family: Consolas, Helvetica, sans-serif;
}

h1 {
    text-align: center;
}

#customers {
  border-collapse: collapse;
  width: 100%;
}

#customers td, #customers th {
  border: 1px solid #ddd;
  padding: 8px;
}

#customers tr:nth-child(even){background-color: gray;}

#customers tr:hover {background-color: #4b4b4b;}

#customers th {
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: left;
  background-color: #aa0434;
  color: white;
}
</style>
</head>
<body>

<h1>Employees Table</h1>

<table id="customers">
  <tr>
    <th>Name</th>
    <th>Job</th>
    <th>Age</th>
  </tr>
"""

for i in people:
    html += f"""
  <tr>
    <td>{i['name']}</td>
    <td>{i['job']}</td>
    <td>{i['age']}</td>
  </tr>
    """

html += """
</table>
</body>
</html>
"""

open("Table.html", "w").write(html)
