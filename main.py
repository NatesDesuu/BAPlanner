from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, ForeignKey, select

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
    student_name: Mapped[str] = mapped_column(String, nullable=False)
    rarity: Mapped[str] = mapped_column(Integer, nullable=False)
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


def add_student_data(student_id, student_name, student_rarity):
    new_student = Student(
        id=student_id,
        name=student_name,
        detail_id=student_id,
        current_level=1,
        current_bond=1,
        current_star=student_rarity,
        current_ue=0,
        current_ue_level=0,
        current_ex=1,
        current_basic=1,
        current_enhanced=0,
        current_sub=0,
        current_gear1=0,
        current_gear2=0,
        current_gear3=0,
        target_level=1,
        target_bond=1,
        target_star=student_rarity,
        target_ue=0,
        target_ue_level=0,
        target_ex=1,
        target_basic=1,
        target_enhanced=0,
        target_sub=0,
        target_gear1=0,
        target_gear2=0,
        target_gear3=0
    )
    db.session.add(new_student)
    db.session.commit()


def add_student_details():
    new_student_detail = StudentDetail(
        id=1164,
        student_name="Kikyou",
        rarity=3,
        school="Hyakkiyako",
        bg="hyakki",
        type="striker",
        role="Dealer",
        position="back",
        atk_type="Sonic",
        def_type="Heavy",
        mood1="outstanding",
        mood2="neutral",
        mood3="terrible",
        ex="cross",
        basic="bullet-buff",
        enhanced="weapon-buff",
        sub="kikyou-sub",
        cover="true",
        weapon_type="sr",
        weapon_img=1164,
        weapon_name="Hyakkaryouran Rifle - Azure Wisdom",
        gear1="gloves",
        gear2="hairpin",
        gear3="watch"
    )
    db.session.add(new_student_detail)
    db.session.commit()


@app.route('/')
def home():
    result = (db.session.query(Student).join(Student.detail, full=True)
              .order_by(Student.current_level.desc(), Student.current_bond.desc()))
    all_students = [student for student in result.all() if student]
    return render_template("index.html", students=all_students)


@app.route("/display-students", methods=['POST'])
def display_students():
    # Get data from JS fetch
    display_data = request.get_json()
    # Get sorting order first
    if display_data['basic-order'] == "desc":
        result = (db.session.query(Student).join(Student.detail, full=True)
                  .order_by(Student.current_level.desc(), Student.current_bond.desc()))
    else:
        result = (db.session.query(Student).join(Student.detail, full=True)
                  .order_by(Student.current_level.asc(), Student.current_bond.asc()))
    # If the basic filter selected was not 'All'
    if display_data['basic-filter']:
        result = result.filter(StudentDetail.type == display_data['basic-filter'])
    # Return ordered list of students
    all_students = [student for student in result.all() if student]
    return render_template("partials/student-list.html", students=all_students)


@app.route('/display-unowned-students', methods=['POST'])
def display_unowned_students():
    # Get list of owned students by id
    students_owned = db.session.execute(select(Student.id).select_from(Student)).scalars()
    # Get list of unowned students (id, name, starting rarity)
    students_not_owned = db.session.execute(select(StudentDetail.id, StudentDetail.student_name, StudentDetail.rarity)
                                            .select_from(StudentDetail).where(StudentDetail.id.not_in(students_owned))
                                            .order_by(StudentDetail.student_name)).all()
    return render_template("partials/modals/student-add.html", students=students_not_owned)


@app.route('/add-student', methods=['POST'])
def add_student():
    # Get data from JS fetch
    students = request.get_json()
    # Add students
    for student in students:
        add_student_data(student.split(", ")[0], student.split(", ")[1], student.split(", ")[2])
    return '', 204


@app.route('/update-student', methods=['POST'])
def update_student():
    # Get data from JS fetch
    student_data = request.get_json()
    # Get the id of the student to be updated
    student = db.get_or_404(Student, student_data['student_id'])
    student.current_level = student_data['current_level']
    student.current_bond = student_data['current_bond']
    student.current_ue_level = student_data['current_ue_level']
    student.current_ex = student_data['current_ex']
    student.current_basic = student_data['current_basic']
    student.current_enhanced = student_data['current_enhanced']
    student.current_sub = student_data['current_sub']
    student.current_gear1 = student_data['current_gear1']
    student.current_gear2 = student_data['current_gear2']
    student.current_gear3 = student_data['current_gear3']
    student.target_level = student_data['target_level']
    student.target_bond = student_data['target_bond']
    student.target_ue_level = student_data['target_ue_level']
    student.target_ex = student_data['target_ex']
    student.target_basic = student_data['target_basic']
    student.target_enhanced = student_data['target_enhanced']
    student.target_sub = student_data['target_sub']
    student.target_gear1 = student_data['target_gear1']
    student.target_gear2 = student_data['target_gear2']
    student.target_gear3 = student_data['target_gear3']
    db.session.commit()
    return '', 204


@app.route('/delete-student', methods=['POST'])
def delete_student():
    # Get data from JS fetch
    student_id = request.get_data(as_text=True)
    # Get the id of the student to be deleted
    student_to_delete = db.get_or_404(Student, student_id)
    db.session.delete(student_to_delete)
    db.session.commit()
    return '', 204


if __name__ == "__main__":
    app.run(debug=True)
