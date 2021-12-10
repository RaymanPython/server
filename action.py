# Строку выше удалять не следует. 
# Это специальный комментарий, который запустит python

import cgi, cgitb
import random


form = cgi.FieldStorage()
# включаем вывод ошибок
cgitb.enable()
res = 0
n = 5
ans = []
for i in range(n):
    ans.append(random.randint(0, 1))
answers = ["Yes", "NO"]
for i in ans:
    print(answers[i])
for i in range(1, n + 1):
    if form.getvalue(str(i)) == answers[ans[i - 1]]:
        res += 1

# добавляем заголовок, чтобы браузер понял 
# как показывать то, что мы ему прислали.
# Мы будем передавать текст HTML
print("Content-type: text/html")
# Выводим пустую строку - разделитель
# между заголовком и содержимым HTML
print("")
lol = f"""{form.getvalue("name", "")} {form.getvalue("surname", "")} {form.getvalue("patronymic", "")}, проживающий в стране {form.getvalue("country")} имеет коефициент везения {res * 100 // (n - 1)}% \n"""

# получаем доступ к форме
f = open('input.txt', 'w')
f.write(lol)
f.close()

print(f"""<html>
<head>
    <meta charset="UTF-8">
</head>
<body>
    ФИО: {form.getvalue("name", "")} {form.getvalue("surname", "")} {form.getvalue("patronymic", "")}, 
    Страна: {form.getvalue("country")}
    <p>У вас биполярка на {res * 100 // (n - 1)}</p>
</body>
</html>""")