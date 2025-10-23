export default function Todolist() {
  const input = document.getElementById("taskInput");
  const addBtn = document.getElementById("addBtn");
  const list = document.getElementById("taskList");

  const saveTasks = () => {
    const tasks = [];
    list.querySelectorAll("li").forEach((li) => {
      const text = li.querySelector("span").textContent.trim();
      const completed = li.querySelector("input[type='checkbox']").checked;
      tasks.push({ text, completed });
    });
    localStorage.setItem("tasks", JSON.stringify(tasks));
  };

  const renderTask = (text, completed = false) => {
    const li = document.createElement("li");
    li.className =
      "flex items-center justify-between bg-gray-800 px-4 py-2 rounded-lg";

    const checkbox = document.createElement("input");

    checkbox.type = "checkbox";
    checkbox.checked = completed;

    const span = document.createElement("span");
    span.textContent = " " + text + " ";
    if (completed) span.style.textDecoration = "line-through";

    const delBtn = document.createElement("button");
    delBtn.className =
      "bg-[#f38ba8] hover:bg-[#eba0ac] text-[#1e1e2e] px-2 py-1 rounded transition";
    delBtn.textContent = "Hapus";

    checkbox.addEventListener("change", () => {
      span.style.textDecoration = checkbox.checked ? "line-through" : "none";
      saveTasks();
    });

    delBtn.addEventListener("click", () => {
      list.removeChild(li);
      saveTasks();
    });

    li.appendChild(checkbox);
    li.appendChild(span);
    li.appendChild(delBtn);
    list.appendChild(li);
  };

  function addTask() {
    const text = input.value.trim();
    if (!text) return;
    renderTask(text);
    saveTasks();
    input.value = "";
    input.focus();
  }
  
  // render the data from localstorage first
  const savedTasks = JSON.parse(localStorage.getItem("tasks")) || [];
  savedTasks.forEach((task) => renderTask(task.text, task.completed));

  // render the data when key enter or addBtn clicked
  addBtn.addEventListener("click", addTask);
  input.addEventListener("keydown", (e) => {
    if (e.key === "Enter") addTask();
  });
}
