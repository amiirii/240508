from flask import Flask
import sqlite3


app = Flask(__name__)
@app.route("/tables")

def mostrar_info():
    conn = sqlite3.connect("ejemplo.db")
    query = ("select * from sqlite_master where type='table';")
    c = conn.execute(query)
    return (c.fetchone())

@app.route("/tables/<sr>")
def mostrar_tablas(sr):
    conn = sqlite3.connect("ejemplo.db")
    query = ("SELECT * FROM " + sr + ";")
    c = conn.execute(query)
    return (c.fetchone())

if __name__ == "__main":
    app.run()

