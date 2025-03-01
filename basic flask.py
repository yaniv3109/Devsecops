from flask import Flask

app = Flask(__name__)

@app.get('/len/<name>')
def len_name(name):
    return f"{len(name)}"


if __name__ == '__main__':
    app.run(port=5050)

