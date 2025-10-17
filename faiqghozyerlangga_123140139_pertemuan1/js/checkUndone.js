export default function CheckUndone() {
  const checkUndone = document.getElementById("checkUndone");
  let data = JSON.parse(localStorage.getItem("tasks")) || [];

  let done = 0;
  let undone = 0;

  data.forEach((task) => {
    if (task.done === true) {
      done++;
    } else {
      undone++;
    }
  });

  const pDone = document.createElement("p");
  pDone.textContent = `Sudah selesai: ${done}`;
  const pUndone = document.createElement("p");
  pUndone.textContent = `Belum selesai: ${undone}`;

  checkUndone.append(pDone, pUndone);
}
