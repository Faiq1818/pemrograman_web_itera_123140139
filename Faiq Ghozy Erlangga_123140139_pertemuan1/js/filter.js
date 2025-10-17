export default function Filter() {
  const filterInput = document.getElementById("filterInput");
  const table = document.getElementById("taskTable");

  filterInput.addEventListener("input", () => {
    table.innerHTML = "";
    const keyword = filterInput.value.toLowerCase().trim();

    // get data from local storage and render it to domtree
    let data = JSON.parse(localStorage.getItem("tasks")) || [];
    data.forEach((task, index) => {
      if (
        task.namaTugas.toLowerCase().includes(keyword) ||
        task.mataKuliah.toLowerCase().includes(keyword)
      ) {
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
          );
        } else {
          tdDone.textContent = "Belum selesai";
          tdDone.classList.add(
            "border",
            "border-[#cdd6f4]",
            "px-4",
            "py-2",
            "text-[#f38ba8]",
          );
        }

        tr.append(tdIndex, tdNama, tdMatkul, tdDeadline, tdDone);
        table.appendChild(tr);
      }
    });
  });
}
