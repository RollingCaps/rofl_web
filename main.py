from flask import Flask, render_template
import mysql.connector
import secret_config

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


# тест соединения
cnx = mysql.connector.connect(user=secret_config.user, password=secret_config.password,
                              host=secret_config.host)
cnx.close()
app.run(debug=True)
