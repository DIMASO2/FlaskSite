from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def duplet():
    return render_template("duplet.html")

@app.route('/contacts/')
def contacts():
    developer_name = "Mao"
    developer_email = "mao@mail.ru"
    return render_template("agu.html", name = developer_name, email = developer_email)

if __name__ == "__main__":
    app.run(debug = True)