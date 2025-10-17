export default function FilterNameClass() {
  const filterInput = document.getElementById("filterInput");
  const filterStatus = document.getElementById("filterStatus");
  const table = document.getElementById("taskTable");

  let showDone = true;

  function renderFiltered() {
    table.innerHTML = `
      <tr class="border">
        <th class="border">No</th>
        <th class="border">Tugas</th>
        <th class="border">Mata Kuliah</th>
        <th class="border">Deadline</th>
        <th class="border">Status</th>
        <th class="border">Klik untuk hapus</th>
      </tr>
    `;

    const keyword = filterInput.value.toLowerCase().trim();
    const data = JSON.parse(localStorage.getItem("tasks")) || [];

    // filter data
    const filteredData = data.filter(
      (task) =>
        task.mataKuliah.toLowerCase().includes(keyword) &&
        task.done === showDone,
    );

    filteredData.forEach((task, displayIndex) => {
      const tr = document.createElement("tr");
      tr.classList.add("border-b", "hover:bg-gray-800");

      const tdIndex = document.createElement("td");
      tdIndex.textContent = displayIndex + 1;
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
      tdDone.textContent = task.done ? "Selesai" : "Belum selesai";
      tdDone.classList.add(
        "border",
        "border-[#cdd6f4]",
        "px-4",
        "py-2",
        "cursor-pointer",
        task.done ? "text-[#a6e3a1]" : "text-[#f38ba8]",
        "hover:bg-[#89b4fa]",
        "hover:text-[#1e1e2e]",
      );

      tdDone.addEventListener("click", () => {
        const realIndex = data.findIndex(
          (t) => t.namaTugas === task.namaTugas && t.deadline === task.deadline,
        );
        if (realIndex !== -1) {
          data[realIndex].done = !data[realIndex].done;
          localStorage.setItem("tasks", JSON.stringify(data));
          renderFiltered();
        }
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

      tdDelete.addEventListener("click", () => {
        const realIndex = data.findIndex(
          (t) => t.namaTugas === task.namaTugas && t.deadline === task.deadline,
        );
        if (realIndex !== -1) {
          data.splice(realIndex, 1);
          localStorage.setItem("tasks", JSON.stringify(data));
          renderFiltered();
        }
      });

      tr.append(tdIndex, tdNama, tdMatkul, tdDeadline, tdDone, tdDelete);
      table.appendChild(tr);
    });
  }

  // filter from input
  filterInput.addEventListener("input", renderFiltered);

  // filter from button status
  filterStatus.addEventListener("click", () => {
    showDone = !showDone;
    filterStatus.textContent = showDone ? "Selesai" : "Belum selesai";
    filterStatus.className = showDone
      ? "bg-[#a6e3a1] p-1 text-[#181825] font-bold text-center cursor-pointer"
      : "bg-[#f38ba8] p-1 text-[#181825] font-bold text-center cursor-pointer";
    renderFiltered();
  });
}
