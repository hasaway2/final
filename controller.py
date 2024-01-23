import flask as f
app = f.Flask(__name__)

@app.route("/")
def 목록():
  pass

@app.route("/read")
def 읽기():
  pass

@app.route("/write")
def 쓰기_화면():
  pass

@app.route("/write", methods=['post'])
def 쓰기():
  pass

app.run(debug=True)