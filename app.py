from flask import Flask, jsonify, request, session, render_template, redirect
from flask_cors import CORS
import psycopg2 as pgsql
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SEC_KEY")
CORS(app)

passwd = os.getenv("DB_PASSWORD")

@app.route('/')
@app.route("/home")
def home():
    if "user_name" in session:
        print(session)
        return redirect("/dashboard")
    return redirect("/login")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/submit", methods = ["POST"])
def sub():
    data = request.form
    username = data['userName']
    passwd = data['passwd']
    con = pgsql.connect(
        host = 'localhost',
        database = 'zflowcrm',
        user = 'postgres',
        password = passwd
    )
    cur = con.cursor()
    cur.execute("SELECT * FROM zusers where username = %s", (username,))
    sqldata = cur.fetchone()
    if sqldata:
        if passwd == sqldata[-1]:
            num = sqldata[1]
            session["user_name"] = data["userName"]
            session["sender"] = num
            return redirect("/dashboard")
    return redirect("/login")

@app.route("/dashboard")
def dashboard():
    if "user_name" in session and "sender" in session:
        return render_template("index.html", data = session)
    return "You don't have access to this site!"

@app.route("/reset")
def reset():
    session.clear()
    return redirect('/')

@app.route("/getClients")
def get_client():
    if "user_name" not in session:
        return jsonify({"error": "Unauthorized"}), 401
    con = pgsql.connect(
        host = 'localhost',
        database = 'zflowcrm',
        user = 'postgres',
        password = passwd
    )

    cur = con.cursor()
    cur.execute("SELECT number, name FROM chats where sender = %s", (session["sender"],))

    rows = cur.fetchall()[::-1]

    clients = []
    l = []

    l.extend(_ for _ in rows if _ not in l)

    for i in l:
        clients.append({"number": i[0], "name": i[1]})

    cur.close()
    con.close()

    return jsonify(clients)

@app.route("/getChats", methods = ["POST"])
def get_chat():
    if "user_name" not in session:
        return jsonify({"error": "Unauthorized"}), 401
    data = request.json

    number = data["number"][1:]
    sender = session["sender"]

    con = pgsql.connect(
        host = 'localhost',
        database = 'zflowcrm',
        user = 'postgres',
        password = passwd
    )

    cur = con.cursor()
    cur.execute("SELECT chat_text, direction FROM chats WHERE number = %s and sender = %s", (number, sender))

    rows = cur.fetchall()

    chats = []

    for i in rows:
        chats.append({"chat_text": i[0], "dir": i[1]})
    
    cur.close()
    con.close()

    return jsonify(chats)

@app.route("/sendMessage", methods=["POST"])
def receiveMessage():
    if "user_name" not in session:
        return jsonify({"error": "Unauthorized"}), 401
    try:
        data = request.json
        number = data["number"][1:]
        message = data["message"]
        sender = session["sender"]
        name = ""
        client_id = 0

        conn = pgsql.connect(
            host="localhost",
            database="zflowcrm",
            user="postgres",
            password=passwd
        )

        cur = conn.cursor()

        cur.execute("SELECT client_id, name FROM users WHERE number = %s", (number,))
        client_data = cur.fetchone()

        name = client_data[1]
        client_id = client_data[0]

        print(number, message, sender, name, client_id)

        cur.execute(
            """
            INSERT INTO chats
            (number, chat_text, direction, sender, name, client_id)
            VALUES (%s, %s, %s, %s, %s, %s)
            """,
            (number, message, "out", sender, name, client_id)
        )

        conn.commit()

        cur.close()
        conn.close()

        return jsonify({
            "success": True,
            "message": "Message stored"
        }), 200

    except Exception as e:
        print(e)

        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)