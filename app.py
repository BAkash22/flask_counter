from flask import Flask
app = Flask(__name__)

counter = 0

@app.route('/')
def count_visitors():
    global counter
    counter += 1
    return f"Visitor Count: {counter}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
