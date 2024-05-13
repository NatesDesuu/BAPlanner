// Initialize containers
const studentsList = document.getElementById("studentsContainer")
const studentInfoModal = document.getElementById('studentInfoModal')
const studentAddModal = document.getElementById('studentAddModal')

// Initialize modal body
const modalBody = studentInfoModal.querySelector('.modal-body')
const studentModalImg = studentInfoModal.querySelector('#studentModalImg img')

// Initialize modal table - row 1
const studentModalID = studentInfoModal.querySelector('#studentModalID')
const studentModalName = studentInfoModal.querySelector('#studentModalName')
const studentModalCurrentLevel = studentInfoModal.querySelector('#level_current')
const studentModalTargetLevel = studentInfoModal.querySelector('#level_target')
const studentModalCurrentBond = studentInfoModal.querySelector('#bond_current')
const studentModalTargetBond = studentInfoModal.querySelector('#bond_target')

// Initialize modal table - row 2
const studentModalType = studentInfoModal.querySelector('#studentModalType')
const studentModalRole = studentInfoModal.querySelector('#studentModalRole span')
const studentModalRoleImg = studentInfoModal.querySelector('#studentModalRole img')
const studentModalPosition = studentInfoModal.querySelector('#studentModalPosition')
const studentModalAtkType = studentInfoModal.querySelector('#studentModalAtkType')
const studentModalDefType = studentInfoModal.querySelector('#studentModalDefType')
const studentModalMood1 = studentInfoModal.querySelector('#studentModalMood1')
const studentModalMood2 = studentInfoModal.querySelector('#studentModalMood2')
const studentModalMood3 = studentInfoModal.querySelector('#studentModalMood3')

// Initialize modal table - row 3
const studentModalEx = studentInfoModal.querySelector('#studentModalEx img')
const studentModalBasic = studentInfoModal.querySelector('#studentModalBasic img')
const studentModalEnhanced = studentInfoModal.querySelector('#studentModalEnhanced img')
const studentModalSub = studentInfoModal.querySelector('#studentModalSub img')
const studentModalCurrentEx = studentInfoModal.querySelector('#ex_current')
const studentModalTargetEx = studentInfoModal.querySelector('#ex_target')
const studentModalCurrentBasic = studentInfoModal.querySelector('#basic_current')
const studentModalTargetBasic = studentInfoModal.querySelector('#basic_target')
const studentModalCurrentEnhanced = studentInfoModal.querySelector('#enhanced_current')
const studentModalTargetEnhanced = studentInfoModal.querySelector('#enhanced_target')
const studentModalCurrentSub = studentInfoModal.querySelector('#sub_current')
const studentModalTargetSub = studentInfoModal.querySelector('#sub_target')

// Initialize modal table - row 4
const studentModalWeaponType = studentInfoModal.querySelector('#studentModalWeaponType span')
const studentModalCover = studentInfoModal.querySelector('#studentModalWeaponType img')
const studentModalWeapon = studentInfoModal.querySelector('#studentModalUE img')
const studentModalWeaponName = studentInfoModal.querySelector('#studentModalUE span')
const studentModalCurrentUELevel = studentInfoModal.querySelector('#ue_level_current')
const studentModalTargetUELevel = studentInfoModal.querySelector('#ue_level_target')

// Initialize modal table - row 5
const studentModalGear1 = studentInfoModal.querySelector('#studentModalGear1')
const studentModalGear2 = studentInfoModal.querySelector('#studentModalGear2')
const studentModalGear3 = studentInfoModal.querySelector('#studentModalGear3')
const studentModalCurrentGear1 = studentInfoModal.querySelector('#gear1_current')
const studentModalTargetGear1 = studentInfoModal.querySelector('#gear1_target')
const studentModalCurrentGear2 = studentInfoModal.querySelector('#gear2_current')
const studentModalTargetGear2 = studentInfoModal.querySelector('#gear2_target')
const studentModalCurrentGear3 = studentInfoModal.querySelector('#gear3_current')
const studentModalTargetGear3 = studentInfoModal.querySelector('#gear3_target')

if (studentInfoModal) {
  studentInfoModal.addEventListener('show.bs.modal', event => {
    // Initialize data source
    const div = event.relatedTarget
    const student_data = JSON.parse(div.getAttribute('data-bs-data'))
    const student_details = JSON.parse(div.getAttribute('data-bs-details'))

    // Update body
    modalBody.style.backgroundImage = 'url(static/assets/img/ui/bg/'+ student_details['bg'] +'.jpg)';
    modalBody.style.backgroundSize = 'cover';
    studentModalImg.src = 'static/assets/img/char/portrait/' + student_data['id'] + '.png'

    // Update table - row 1
    studentModalID.value = student_data['id']
    studentModalName.textContent = student_details['student_name']
    if (student_data['name'].length > 18) {
        studentModalName.style.fontSize = '16px';
    } else if (student_data['name'].length > 15) {
        studentModalName.style.fontSize = '19px';
    } else {
        studentModalName.style.fontSize = '20px';
    }
    studentModalCurrentLevel.value = student_data['current_level']
    studentModalTargetLevel.value = student_data['target_level']
    studentModalCurrentBond.value = student_data['current_bond']
    studentModalTargetBond.value = student_data['target_bond']

    // Update table - row 2
    studentModalType.textContent = student_details['type'].toUpperCase()
    if (student_details['type'] == "striker") {
        studentModalType.style.color = 'red';
    } else {
        studentModalType.style.color = 'blue';
    }
    studentModalRole.textContent = student_details['role']
    studentModalRoleImg.src = 'static/assets/img/ui/role/' + student_details['role'].toLowerCase() + '.webp'
    studentModalPosition.textContent = student_details['position'].toUpperCase()
    studentModalAtkType.textContent = student_details['atk_type']
    if (student_details['atk_type'] == "Explosive") {
        studentModalAtkType.style.backgroundColor = '#920108';
        studentModalEx.style.backgroundColor = '#920108';
        studentModalBasic.style.backgroundColor = '#920108';
        studentModalEnhanced.style.backgroundColor = '#920108';
        studentModalSub.style.backgroundColor = '#920108';
    } else if (student_details['atk_type'] == "Piercing") {
        studentModalAtkType.style.backgroundColor = '#BE8905';
        studentModalEx.style.backgroundColor = '#BE8905';
        studentModalBasic.style.backgroundColor = '#BE8905';
        studentModalEnhanced.style.backgroundColor = '#BE8905';
        studentModalSub.style.backgroundColor = '#BE8905';
    } else if (student_details['atk_type'] == "Mystic") {
        studentModalAtkType.style.backgroundColor = '#236D9A';
        studentModalEx.style.backgroundColor = '#236D9A';
        studentModalBasic.style.backgroundColor = '#236D9A';
        studentModalEnhanced.style.backgroundColor = '#236D9A';
        studentModalSub.style.backgroundColor = '#236D9A';
    } else {
        studentModalAtkType.style.backgroundColor = '#9745A7';
        studentModalEx.style.backgroundColor = '#9745A7';
        studentModalBasic.style.backgroundColor = '#9745A7';
        studentModalEnhanced.style.backgroundColor = '#9745A7';
        studentModalSub.style.backgroundColor = '#9745A7';
    }
    studentModalDefType.textContent = student_details['def_type']
    if (student_details['def_type'] == "Light") {
        studentModalDefType.style.backgroundColor = '#920108';
    } else if (student_details['def_type'] == "Heavy") {
        studentModalDefType.style.backgroundColor = '#BE8905';
    } else if (student_details['def_type'] == "Special") {
        studentModalDefType.style.backgroundColor = '#236D9A';
    } else {
        studentModalDefType.style.backgroundColor = '#9745A7';
    }
    studentModalMood1.src = 'static/assets/img/ui/mood/' + student_details['mood1'] + '.webp'
    studentModalMood2.src = 'static/assets/img/ui/mood/' + student_details['mood2'] + '.webp'
    studentModalMood3.src = 'static/assets/img/ui/mood/' + student_details['mood3'] + '.webp'

    // Update table - row 3
    studentModalEx.src = 'static/assets/img/char/skill/'+ student_details['ex'] +'.webp'
    studentModalBasic.src = 'static/assets/img/char/skill/'+ student_details['basic'] +'.webp'
    studentModalEnhanced.src = 'static/assets/img/char/skill/'+ student_details['enhanced'] +'.webp'
    studentModalSub.src = 'static/assets/img/char/skill/'+ student_details['sub'] +'.webp'
    studentModalCurrentEx.value = student_data['current_ex']
    studentModalTargetEx.value = student_data['target_ex']
    studentModalCurrentBasic.value = student_data['current_basic']
    studentModalTargetBasic.value = student_data['target_basic']
    studentModalCurrentEnhanced.value = student_data['current_enhanced']
    studentModalTargetEnhanced.value = student_data['target_enhanced']
    studentModalCurrentSub.value = student_data['current_sub']
    studentModalTargetSub.value = student_data['target_sub']

    // Update table - row 4
    studentModalWeaponType.textContent = student_details['weapon_type'].toUpperCase()
    if (student_details['cover'] == "false") {
        studentModalCover.style.display = 'none';
    } else {
        studentModalCover.style.display = 'initial';
    }
    studentModalWeapon.src = 'static/assets/img/char/ue/'+ student_details['weapon_img'] +'.png'
    studentModalWeaponName.textContent = student_details['weapon_name']
    studentModalCurrentUELevel.value = student_data['current_ue_level']
    studentModalTargetUELevel.value = student_data['target_ue_level']

    // Update table - row 5
    studentModalGear1.src = 'static/assets/img/ui/gear/'+ student_details['gear1'] +'-t8.webp'
    studentModalGear2.src = 'static/assets/img/ui/gear/'+ student_details['gear2'] +'-t8.webp'
    studentModalGear3.src = 'static/assets/img/ui/gear/'+ student_details['gear3'] +'-t8.webp'
    studentModalCurrentGear1.value = student_data['current_gear1']
    studentModalTargetGear1.value = student_data['target_gear1']
    studentModalCurrentGear2.value = student_data['current_gear2']
    studentModalTargetGear2.value = student_data['target_gear2']
    studentModalCurrentGear3.value = student_data['current_gear3']
    studentModalTargetGear3.value = student_data['target_gear3']
  })
}

// Initialize filter objects
const basicOrderCheck = document.getElementById("orderStudents");
const basicOrderCheckLabel = document.getElementById("orderStudentsLabel");

// General display function (for basic order as well)
function displayStudents() {
    let basicFilter = $('input[name="basic-filters"]:checked').val();
    let basicOrder;
    if (basicOrderCheck.checked == true){
        basicOrderCheckLabel.textContent = "☰↑"
        basicOrder = "asc"
    } else {
        basicOrderCheckLabel.textContent = "☰↓"
        basicOrder = "desc"
    }
    let order_data = {
        "basic-order": basicOrder,
        "basic-filter": basicFilter
    }
    fetch("/display-students", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify(order_data)
    })
    .then(response => {
      return response.text();
    })
    .then(html => {
      studentsList.innerHTML = html
    })
}

// Basic filters
$(function () {
    $('input:radio[name="basic-filters"]').change(function() {
        displayStudents();
    });
});

// Update student data
function updateStudent() {
    $("#studentInfoModal").modal("hide");
    let studentData = {
      "student_id": studentModalID.value,
      "current_level": studentModalCurrentLevel.value,
      "current_bond": studentModalCurrentBond.value,
      "current_ue_level": studentModalCurrentUELevel.value,
      "current_ex": studentModalCurrentEx.value,
      "current_basic": studentModalCurrentBasic.value,
      "current_enhanced": studentModalCurrentEnhanced.value,
      "current_sub": studentModalCurrentSub.value,
      "current_gear1": studentModalCurrentGear1.value,
      "current_gear2": studentModalCurrentGear2.value,
      "current_gear3": studentModalCurrentGear3.value,
      "target_level": studentModalTargetLevel.value,
      "target_bond": studentModalTargetBond.value,
      "target_ue_level": studentModalTargetUELevel.value,
      "target_ex": studentModalTargetEx.value,
      "target_basic": studentModalTargetBasic.value,
      "target_enhanced": studentModalTargetEnhanced.value,
      "target_sub": studentModalTargetSub.value,
      "target_gear1": studentModalTargetGear1.value,
      "target_gear2": studentModalTargetGear2.value,
      "target_gear3": studentModalTargetGear3.value
    }
    fetch("/update-student", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify(studentData)
    })
    displayStudents();
}

// Delete student
function deleteStudent() {
    $("#studentInfoModal").modal("hide");
    fetch("/delete-student", {
      method: "POST",
      type: "text/plain",
      body: studentModalID.value
    })
    displayStudents();
}

function addStudent() {
    fetch("/add-student", {
      method: "POST"
    })
    .then(response => {
      return response.text();
    })
    .then(html => {
      studentAddModal.innerHTML = html
    })
}