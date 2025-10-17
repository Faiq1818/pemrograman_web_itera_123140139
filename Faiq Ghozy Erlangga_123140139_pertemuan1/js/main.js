import FilterNameClass from "./filter.js";
import Add from "./add.js";
import TaskTable from "./taskTable.js";
import CheckUndone from "./checkUndone.js";

const deleteAllBtn = document.getElementById("deleteAllBtn");

deleteAllBtn.addEventListener("click", () => {
  localStorage.clear();

  location.reload();
});

FilterNameClass();
Add();
TaskTable();
CheckUndone();

console.log(localStorage);
