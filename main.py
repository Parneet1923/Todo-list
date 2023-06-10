from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        data = request.form
        with open('task.txt', mode='a') as write_data:
            write_data.write(f"{data['task']}\n")
    with open('task.txt') as read_data:
        tasks = read_data.readlines()
    return render_template("index.html", tasks=tasks)


@app.route("/delete/<task>")
def delete(task):
    with open("task.txt", mode='r') as del_data:
        tasks = del_data.readlines()
    tasks.remove(task)
    with open("task.txt", mode='w') as wri_data:
            wri_data.writelines(tasks)
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)

