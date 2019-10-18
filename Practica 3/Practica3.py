from flask import Flask, Response
import sqlite3
import json

app = Flask(__name__)
@app.route("/tables")

def mostrar_nombres():
    conn = sqlite3.connect("ejemplo.db")
    query = ("select * from sqlite_master where type='table';")
    c = conn.execute(query)
    res = c.fetchall()
    r = Response(json.dumps([row[1] for row in res]))
    r.headers["Content-Type"] = "application/json"
    return r

@app.route("/tables/<sr>")
def mostrar_tablas(sr):
    conn = sqlite3.connect("ejemplo.db")
    query = ("SELECT * FROM " + sr + ";")
    c = conn.execute(query)
    res = c.fetchall()
    conn.close()

    r = Response(json.dumps(list(res)))
    r.headers["Content-Type"] = "application/json"
    return r

@app.route("/tables/<sr>/info")
def mostrar_info(sr):
    conn = sqlite3.connect("ejemplo.db")
    query = ("SELECT * FROM " + sr + ";")
    c = conn.execute(query)
    res = c.fetchall()

    query2 = ("SELECT count( * ) FROM " + sr + ";")
    c2 = conn.execute(query2)
    res2 = c2.fetchall()
    resultado_final = [description[0] for description in c.description] + list(res2)
    r = Response(json.dumps(resultado_final))	
    r.headers["Content-Type"] = "application/json"
    conn.close()
    return r
	

	
	

if __name__ == "__main__":
    app.run()
