from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def duplet():
    main_data = {
        "Город": "Новочебоксарск",
        "Район": "Девятка",
        "Контора": "Шарашкина"
    }
    context = {
        "name": "Xi Jinping",
        "age": "70",
        "spes": "Вождь"
    }
    return render_template("glava.html", main_data = main_data, **context)

@app.route('/contacts/')
def contacts():
    developer_name = "Mao"
    developer_email = "mao@mail.ru"
    return render_template("agu.html", name = developer_name, email = developer_email)

@app.route('/results/')
def results():
    data = ["python", "js", "GO", "C#", "C++", "lua", "React"]
    return render_template("results.html", data = data)


if __name__ == "__main__":
    app.run(debug = True)