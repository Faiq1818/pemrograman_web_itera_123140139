import CheckUndone from "./checkUndone.js";

export default function TaskTable() {
  const table = document.getElementById("taskTable");

  // get data from local storage and render it to domtree
  let data = JSON.parse(localStorage.getItem("tasks")) || [];

  data.forEach((task, index) => {
    const tr = document.createElement("tr");
    tr.classList.add("border-b", "hover:bg-gray-800");

    const tdIndex = document.createElement("td");
    tdIndex.textContent = index + 1;
    tdIndex.classList.add("border", "px-4", "py-2", "text-center");

    const tdNama = document.createElement("td");
    tdNama.textContent = task.namaTugas;
    tdNama.classList.add("border", "px-4", "py-2");

    const tdMatkul = document.createElement("td");
    tdMatkul.textContent = task.mataKuliah;
    tdMatkul.classList.add("border", "px-4", "py-2");

    const tdDeadline = document.createElement("td");
    tdDeadline.textContent = task.deadline;
    tdDeadline.classList.add("border", "px-4", "py-2");

    const tdDone = document.createElement("td");
    tdDone.textContent = task.done;
    if (task.done === true) {
      tdDone.textContent = "Selesai";
      tdDone.classList.add(
        "border",
        "border-[#cdd6f4]",
        "px-4",
        "py-2",
        "text-[#a6e3a1]",
        "hover:bg-[#89b4fa]",
        "hover:text-[#1e1e2e]",
        "cursor-pointer",
      );
    } else {
      tdDone.textContent = "Belum selesai";
      tdDone.classList.add(
        "border",
        "border-[#cdd6f4]",
        "px-4",
        "py-2",
        "text-[#f38ba8]",
        "hover:bg-[#89b4fa]",
        "hover:text-[#1e1e2e]",
        "cursor-pointer",
      );
    }

    tdDone.addEventListener("click", () => {
      if (task.done === true) {
        data[index].done = false;
      } else {
        data[index].done = true;
      }

      localStorage.setItem("tasks", JSON.stringify(data));
      console.log("Index:", index);
      location.reload();
    });

    const tdDelete = document.createElement("td");
    tdDelete.textContent = "Hapus";
    tdDelete.classList.add(
      "border",
      "px-4",
      "py-2",
      "text-center",
      "text-[#f38ba8]",
      "border-[#cdd6f4]",
      "font-bold",
      "hover:bg-[#f5c2e7]",
      "cursor-pointer",
    );

    // even listener to get index to delete particular data
    tdDelete.addEventListener("click", () => {
      data.splice(index, 1);

      localStorage.setItem("tasks", JSON.stringify(data));
      console.log("Index:", index);
      CheckUndone();
      location.reload();
    });

    tr.append(tdIndex, tdNama, tdMatkul, tdDeadline, tdDone, tdDelete);
    table.appendChild(tr);
  });
}
