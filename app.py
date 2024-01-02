from flask import Flask, redirect
import random


app = Flask(__name__)


@app.route("/sergei", methods=["GET"])
def sergei_route():
    return "Sergei Fixed It!"


@app.route("/raditya", methods=["GET"])
def raditya_route():
    return "Raditya Is Batman!"


@app.route("/", methods=["GET"])
def root_route():
    return redirect(random.choice(["/raditya", "/sergei"]), code=302)


if __name__ == "__main__":
    app.run()
