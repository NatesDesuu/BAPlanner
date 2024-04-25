from flask import Flask, abort, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from data import student_data, atk_bg, def_bg

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class Base(DeclarativeBase):
    pass


@app.route('/')
def home():
    return render_template("index.html", student_data=student_data, atk_bg=atk_bg, def_bg=def_bg)


if __name__ == "__main__":
    app.run(debug=True)
