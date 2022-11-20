import sqlite3


def login(login, passw, signal):
    con = sqlite3.connect('auto/users.db')
    cur = con.cursor()

    cur.execute(f'SELECT * FROM users WHERE login="{login}";')
    value = cur.fetchall()

    if value != [] and value[0][2] == passw:
        return 1
    else:
        signal.emit('Проверьте правильность ввода данных!')
        return 0

    cur.close()
    con.close()