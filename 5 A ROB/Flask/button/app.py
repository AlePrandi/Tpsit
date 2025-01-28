from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        print(request.form.get('action1'))
        if request.form.get('action1') == 'value1':
            print("Bottone1")
        elif  request.form.get('action2') == 'value2':
            print("Bottone2")
        else:
            print("Unknown")
    elif request.method == 'GET':
        return render_template('index.html')
    
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True, host='localhost')