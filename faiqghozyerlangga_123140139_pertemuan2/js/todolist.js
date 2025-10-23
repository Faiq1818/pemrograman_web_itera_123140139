export default function Todolist() {
  const input = document.getElementById("taskInput");
  const addBtn = document.getElementById("addBtn");
  const list = document.getElementById("taskList");

  const addTask = () => {
    const text = input.value.trim();
    if (!text) return;

    const li = document.createElement("li");
    const checkbox = document.createElement("input");
    checkbox.type = "checkbox";

    const span = document.createElement("span");
    span.textContent = " " + text + " ";

    const delBtn = document.createElement("button");
    delBtn.textContent = "Hapus";

    checkbox.addEventListener("change", () => {
      if (checkbox.checked) {
        span.style.textDecoration = "line-through";
      } else {
        span.style.textDecoration = "none";
      }
    });

    delBtn.addEventListener("click", () => {
      list.removeChild(li);
    });

    li.appendChild(checkbox);
    li.appendChild(span);
    li.appendChild(delBtn);
    list.appendChild(li);

    input.value = "";
    input.focus();
  }

  addBtn.addEventListener("click", addTask);
  input.addEventListener("keydown", (e) => {
    if (e.key === "Enter") addTask();
  });

}
