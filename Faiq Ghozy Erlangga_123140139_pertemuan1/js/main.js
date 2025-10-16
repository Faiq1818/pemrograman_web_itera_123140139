import Filter from "./filter.js";
import Add from "./add.js";

const deleteAllBtn = document.getElementById("deleteAllBtn");
const ul = document.getElementById('taskList')
const openBtn = document.getElementById('deleteIndex');
const dialog = document.getElementById('myDialog');

// open dialog
openBtn.addEventListener('click', () => dialog.showModal());


// get data from local storage and render it to domtree
let data = JSON.parse(localStorage.getItem("tasks")) || [];
data.forEach((task, index) => {
  const li = document.createElement('li') 
  li.textContent = `${index} ${task.done} ${task.namaTugas} (${task.mataKuliah}) - ${task.deadline}`;
  if (task.done) li.style.textDecoration = 'line-through'
  ul.appendChild(li)
})

deleteAllBtn.addEventListener("click", () => {
  localStorage.clear();
});

Add()
Filter()

console.log(localStorage);
