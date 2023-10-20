from flask import Flask, send_file, render_template
import api_generate

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    return render_template('pages/initialPage/index.html')

@app.route('/get_clients')
def get_clients():
    result = api_generate.exampleCustomer()
    return f"<p>{result}</p>"

if __name__ == '__main__':
    app.run()
