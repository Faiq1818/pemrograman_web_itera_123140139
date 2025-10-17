export default function Add() {
  const button = document.getElementById("addBtn");
  const assignmentNameInput = document.getElementById("assignmentNameInput");
  const classNameInput = document.getElementById("classNameInput");
  const deadlineInput = document.getElementById("deadlineInput");

  button.addEventListener("click", () => {
    let data = JSON.parse(localStorage.getItem("tasks")) || [];

    // input form validation
    if (
      assignmentNameInput.value === "" ||
      classNameInput.value === "" ||
      deadlineInput.value === ""
    ) {
      alert("data tidak boleh kosong");
    } else {
      data.push({
        namaTugas: assignmentNameInput.value,
        mataKuliah: classNameInput.value,
        deadline: deadlineInput.value,
        done: false,
      });
      // save to local storage
      localStorage.setItem("tasks", JSON.stringify(data));
    }
  });
}
