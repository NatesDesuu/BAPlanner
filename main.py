from flask import Flask, abort, render_template, redirect, url_for, flash
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from data import student_data

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///acct_data.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


class Student(db.Model):
    __tablename__ = "students"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    current_level: Mapped[str] = mapped_column(Integer, nullable=False)
    current_bond: Mapped[str] = mapped_column(Integer, nullable=False)
    current_star: Mapped[str] = mapped_column(Integer, nullable=False)
    current_ue: Mapped[str] = mapped_column(Integer, nullable=False)
    current_ue_level: Mapped[str] = mapped_column(Integer, nullable=False)
    current_ex: Mapped[str] = mapped_column(Integer, nullable=False)
    current_basic: Mapped[str] = mapped_column(Integer, nullable=False)
    current_enhanced: Mapped[str] = mapped_column(Integer, nullable=False)
    current_sub: Mapped[str] = mapped_column(Integer, nullable=False)
    current_gear1: Mapped[str] = mapped_column(Integer, nullable=False)
    current_gear2: Mapped[str] = mapped_column(Integer, nullable=False)
    current_gear3: Mapped[str] = mapped_column(Integer, nullable=False)
    target_level: Mapped[str] = mapped_column(Integer, nullable=False)
    target_bond: Mapped[str] = mapped_column(Integer, nullable=False)
    target_star: Mapped[str] = mapped_column(Integer, nullable=False)
    target_ue: Mapped[str] = mapped_column(Integer, nullable=False)
    target_ue_level: Mapped[str] = mapped_column(Integer, nullable=False)
    target_ex: Mapped[str] = mapped_column(Integer, nullable=False)
    target_basic: Mapped[str] = mapped_column(Integer, nullable=False)
    target_enhanced: Mapped[str] = mapped_column(Integer, nullable=False)
    target_sub: Mapped[str] = mapped_column(Integer, nullable=False)
    target_gear1: Mapped[str] = mapped_column(Integer, nullable=False)
    target_gear2: Mapped[str] = mapped_column(Integer, nullable=False)
    target_gear3: Mapped[str] = mapped_column(Integer, nullable=False)

    def to_dict(self):
        dictionary = {}
        for column in self.__table__.columns:
            dictionary[column.name] = getattr(self, column.name)
        return dictionary


# # Create database
# with app.app_context():
#     db.create_all()

def add_student():
    new_student = Student(
        id=1058,
        name="Azusa (Swimsuit)",
        current_level=87,
        current_bond=34,
        current_star=5,
        current_ue=2,
        current_ue_level=40,
        current_ex=5,
        current_basic=10,
        current_enhanced=10,
        current_sub=10,
        current_gear1=8,
        current_gear2=8,
        current_gear3=8,
        target_level=87,
        target_bond=100,
        target_star=5,
        target_ue=3,
        target_ue_level=50,
        target_ex=5,
        target_basic=10,
        target_enhanced=10,
        target_sub=10,
        target_gear1=8,
        target_gear2=8,
        target_gear3=8,
    )
    db.session.add(new_student)
    db.session.commit()


@app.route('/')
def home():
    result = db.session.execute(db.select(Student).order_by(Student.name))
    all_students = result.scalars().all()
    return render_template("index.html", students=all_students, student_data=student_data)


if __name__ == "__main__":
    app.run(debug=True)
