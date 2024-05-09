from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, ForeignKey

app = Flask(__name__)
app.config['SECRET_KEY'] = 'HeEhEe'
Bootstrap5(app)


class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


class Student(db.Model):
    __tablename__ = "students"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    detail_id = mapped_column(Integer, ForeignKey("student_details.id"))
    detail = relationship("StudentDetail", foreign_keys=[detail_id])
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


class StudentDetail(db.Model):
    __tablename__ = "student_details"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    school: Mapped[str] = mapped_column(String, nullable=False)
    bg: Mapped[str] = mapped_column(String, nullable=False)
    type: Mapped[str] = mapped_column(String, nullable=False)
    role: Mapped[str] = mapped_column(String, nullable=False)
    position: Mapped[str] = mapped_column(String, nullable=False)
    atk_type: Mapped[str] = mapped_column(String, nullable=False)
    def_type: Mapped[str] = mapped_column(String, nullable=False)
    mood1: Mapped[str] = mapped_column(String, nullable=False)
    mood2: Mapped[str] = mapped_column(String, nullable=False)
    mood3: Mapped[str] = mapped_column(String, nullable=False)
    ex: Mapped[str] = mapped_column(String, nullable=False)
    basic: Mapped[str] = mapped_column(String, nullable=False)
    enhanced: Mapped[str] = mapped_column(String, nullable=False)
    sub: Mapped[str] = mapped_column(String, nullable=False)
    cover: Mapped[str] = mapped_column(String, nullable=False)
    weapon_type: Mapped[str] = mapped_column(String, nullable=False)
    weapon_img: Mapped[int] = mapped_column(Integer, nullable=False)
    weapon_name: Mapped[str] = mapped_column(String, nullable=False)
    gear1: Mapped[str] = mapped_column(String, nullable=False)
    gear2: Mapped[str] = mapped_column(String, nullable=False)
    gear3: Mapped[str] = mapped_column(String, nullable=False)

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
        id=1059,
        name="Mashiro (Swimsuit)",
        detail_id=1059,
        current_level=85,
        current_bond=24,
        current_star=5,
        current_ue=1,
        current_ue_level=30,
        current_ex=5,
        current_basic=7,
        current_enhanced=8,
        current_sub=10,
        current_gear1=8,
        current_gear2=8,
        current_gear3=7,
        target_level=87,
        target_bond=30,
        target_star=5,
        target_ue=1,
        target_ue_level=30,
        target_ex=5,
        target_basic=7,
        target_enhanced=8,
        target_sub=10,
        target_gear1=8,
        target_gear2=8,
        target_gear3=8
    )
    db.session.add(new_student)
    db.session.commit()


def add_student_details():
    new_student_detail = StudentDetail(
        id=1059,
        school="Trinity",
        bg="beach",
        type="special",
        role="Dealer",
        position="back",
        atk_type="Mystic",
        def_type="Light",
        mood1="neutral",
        mood2="outstanding",
        mood3="terrible",
        ex="target",
        basic="weapon-buff",
        enhanced="weapon-buff",
        sub="weapon-buff",
        cover="false",
        weapon_type="sr",
        weapon_img=1046,
        weapon_name="Revelation of Justice",
        gear1="hat",
        gear2="hairpin",
        gear3="watch"
    )
    db.session.add(new_student_detail)
    db.session.commit()


@app.route('/')
def home():
    result = (db.session.query(Student).join(Student.detail, full=True)
              .order_by(Student.current_level.desc(), Student.current_bond.desc()))
    all_students = result.all()
    return render_template("index.html", students=all_students)


@app.route("/basic-filter", methods=['POST'])
def basic_filter():
    selected_basic_filter = request.get_data(as_text=True)
    result = (db.session.query(Student).join(Student.detail, full=True)
              .order_by(Student.current_level.desc()), Student.current_bond.desc())
    if selected_basic_filter:
        result = (db.session.query(Student).join(Student.detail, full=True)
                  .filter(StudentDetail.type == selected_basic_filter)
                  .order_by(Student.current_level.desc(), Student.current_bond.desc()))
    basic_filtered_students = result.all()
    return render_template("student-list.html", students=basic_filtered_students)




if __name__ == "__main__":
    app.run(debug=True)
