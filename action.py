#!/usr/bin/env python
# Строку выше удалять не следует.
# Это специальный комментарий, который запустит python

import cgi, cgitb

# включаем вывод ошибок
cgitb.enable()

# добавляем заголовок, чтобы браузер понял
# как показывать то, что мы ему прислали.
# Мы будем передавать текст HTML
print("Content-type: text/html")
print("")

# получаем доступ к форме
form = cgi.FieldStorage()
print("""<html>
<head>
    <style>
    .color {
      background: lightblue;
      width: 300px;
      text-alight: center;
      }
    </style>
    <meta charset="UTF-8">
</head>
<body>
<p>
    Здравствуйте, """ + str(form.getvalue("name")) + "! Ваше письмо получит " + str(
    form.getvalue("olimp")) + ". В этом году вы попросили " + str(form.getvalue("olimp_name")) + " (" + str(
    form.getvalue("count")) + """). С Наступающим Новым Годом!!!
    """)


name = form.getvalue("name")
olimp = form.getvalue("olimp")
olimp_name = form.getvalue("olimp_name")
olimp_name = form.getvalue("olimp_name")
count = form.getvalue("count")

# открываем файл для чтения в кодировке UTF-8
f = open('all.txt', "a", encoding="UTF-8")
f.write(name)
f.write("\n")
f.write(olimp)
f.write("\n")
f.write(olimp_name)
f.write("\n")
f.write(count)
f.write("\n")
f.write("\n")
f.close()
lines = 0
num = 1

f = open('all.txt', "r", encoding="UTF-8")
line = []
q = 0
a = []
for i in f:
    if q == 4:
        q = 0
        line.append(a)
        a = []
    else:
        a.append(i)
        q += 1
    lines += 1

for i in line:
    print("""
    <div class="color">

       <p> №""" + str(num) + """
       <p> ник: """ + str(i[0]) + """
       <p> Олимпиада: """ + str(i[2]) + """
       <p> Результат: """ + str(i[1]) + " (" + str(i[3]) + """) </p>
    </div>""")

    num += 1
print("""</body>
    </html>""")

