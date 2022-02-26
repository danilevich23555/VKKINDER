from tkinter import *
from tkinter import messagebox
import psycopg2

def display_full_name():
    database1 = database.get()
    user1 = user.get()
    password1 = password.get()
    host1 = host.get()
    port1 = port.get()
    con = psycopg2.connect(
        database=database1,
        user=user1,
        password=password1,
        host=host1,
        port=port1
    )
    cur = con.cursor()
    print("Database opened successfully")
    postgres_insert_query = """create table vkkinder (id_user integer, id_user_find integer, url_profile varchar(300), 
    url_foto_1 varchar(300), url_foto_2 varchar(300), url_foto_3 varchar(300));"""
    cur.execute(postgres_insert_query)
    con.commit()
    messagebox.showinfo('1', 'Данные занесены, таблица vkkinder создана.')
    with open('connection_db\\connection_db.txt', 'w')as param_con:
        param_con.write(f"{database1}\n")
        param_con.write(f"{user1}\n")
        param_con.write(f"{password1}\n")
        param_con.write(f"{host1}\n")
        param_con.write(f"{port1}")



window = Tk()
window.geometry('600x350')
window.title("Создание базы данных Postgressql")
label1 = Label(text="Для работы приложения необходимо:"
                    "\n1. Заполнить ключи доступа(tokens) файлов vk_tokens.txt(обычный токен для выгрузки фото)\n и "
                    "vk_token_communities.txt(токен сообщества, куда будут вводится команды по подбору пар),"
                    "\nфайлы лежат в папке tokens."
                    "\n2. Для работы необходимо устоновить postgresql на локальный компьютер и ввести необходимые \n"
                    "данные для создания создания таблицы, таблица будет создана в БД postgres с пользователем postgres."
                    "", fg="#ddd", bg="#000")
label1.place(x=10,y=5)
database = StringVar()
user = StringVar()
password = StringVar()
host = StringVar()
port = StringVar()


database_label = Label(text="Введите имя схемы БД (postgres): ")
user_label = Label(text="Введите имя пользователя(postgres): ")
password_label = Label(text="Введите пароль: ")
host_label = Label(text="Введите адрес хоста(localhost): ")
port_label = Label(text="Введите номер порта(5432):")


database_label.place(x=10,y=120)
user_label.place(x=10,y=150)
password_label.place(x=10,y=180)
host_label.place(x=10,y=210)
port_label.place(x=10,y=240)



database_entry = Entry(textvariable=database)
user_entry = Entry(textvariable=user)
password_entry = Entry(textvariable=password)
host_entry = Entry(textvariable=host)
port_entry = Entry(textvariable=port)



database_entry.place(x=220,y=120)
user_entry.place(x=220,y=150)
password_entry.place(x=220,y=180)
host_entry.place(x=220,y=210)
port_entry.place(x=220,y=240)


button1 = Button(window, text="Apply", height=1, width=5, command=display_full_name)
button1.place(x=250, y=320)
button2 = Button(window, text="Chanel", height=1, width=5)
button2.place(x=300, y=320)

window.mainloop()

