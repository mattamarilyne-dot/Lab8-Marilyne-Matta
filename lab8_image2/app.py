import sqlite3
from flask import Flask, jsonify

app = Flask(__name__)

def get_users():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM users")
    rows = cursor.fetchall()

    conn.close()

    names = [row[0] for row in rows]
    return names

@app.route("/api/get_users", methods=["GET"])
def api_get_users():
    return jsonify(get_users())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
