const app = document.getElementById("app");
const button = document.getElementById("addBtn");
const deleteAllBtn = document.getElementById("deleteAllBtn");
const assignmentNameInput = document.getElementById("assignmentNameInput");
const classNameInput = document.getElementById("classNameInput");
const deadlineInput = document.getElementById("deadlineInput");

// serialize the localStorage

button.addEventListener("click", () => {
  let data = JSON.parse(localStorage.getItem("tasks")) || [];
  console.log(data);
  data.push({
    namaTugas: assignmentNameInput.value,
    mataKuliah: classNameInput.value,
    deadline: deadlineInput.value,
  });
  localStorage.setItem("tasks", JSON.stringify(data));
});

console.log(localStorage);

deleteAllBtn.addEventListener("click", () => {
  localStorage.clear();
});
