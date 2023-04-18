from flask import *
from sqlalchemy import create_engine, text
import os


user = "v6c2cnij34cx9hsvkrcb"
password = "pscale_pw_ohNxHwY6MdHZc1Fa80LDe8YsTiOsvpDPxCVRKdC49z9"

connect_string = f"mysql+pymysql://{user}:{password}@aws.connect.psdb.cloud/hello?charset=utf8mb4"
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
     
