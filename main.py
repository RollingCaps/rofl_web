from flask import Flask, render_template
import mysql.connector
import secret_config
from statistics import mean, mode, variance

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    cnx = mysql.connector.connect(user=secret_config.user, password=secret_config.password,
                                  host=secret_config.host, database=secret_config.database)
    cursor = cnx.cursor()
    cursor.execute("SELECT Text FROM Reposts")
    data = []
    cnt_empty = 0
    for (Text) in cursor:
        data.append(len(Text[0]))
        if len(Text[0]) == 0:
            cnt_empty += 1
    cnx.close()
    return render_template("index.html", cnt=len(data), avg_text=mean(data), md_text=mode(data), d_text=variance(data),
                           min_text=min(data), max_text=max(data),
                           with_text=len(data) - cnt_empty, no_text=cnt_empty)


app.run(debug=True)
