from flask import Flask, render_template
import mysql.connector
import secret_config

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    cnx = mysql.connector.connect(user=secret_config.user, password=secret_config.password,
                                  host=secret_config.host, database=secret_config.database)
    cursor = cnx.cursor()
    cursor.execute("SELECT Text FROM Reposts")
    lng = 0
    cnt = 0
    cnt_empty = 0
    for (Text) in cursor:
        lng += len(Text[0])
        if len(Text[0]) == 0:
            cnt_empty += 1
        cnt += 1
    cnx.close()
    return render_template("index.html", avg_text=lng / cnt, with_text=cnt - cnt_empty, no_text=cnt_empty)


app.run(debug=True)
