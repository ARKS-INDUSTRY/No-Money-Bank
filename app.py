from flask import *
from sqlalchemy import create_engine, text
import os


connect_string = os.environ.get('connection')
engine = create_engine(connect_string,connect_args={
    "ssl": {
      "ssl_ca": "/etc/ssl/cert.pem"
    }
  })
with engine.connect() as conn:
      result = conn.execute(text("select * from bank"))
      data = list()
      for i in result.all():
           data.append(i)

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route("/transaction/")
def transaction():
     return render_template("transaction.html", datas = data)

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)
     
