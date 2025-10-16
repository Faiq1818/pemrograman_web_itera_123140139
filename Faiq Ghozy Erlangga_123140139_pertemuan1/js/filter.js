export default function Filter() {
  const filterInput = document.getElementById("filterInput");
  const ul = document.getElementById('taskList')

  filterInput.addEventListener("input", () => {
    ul.innerHTML = "";
    const keyword = filterInput.value.toLowerCase().trim(); // ambil input

    // get data from local storage and render it to domtree
    let data = JSON.parse(localStorage.getItem("tasks")) || [];
    data.forEach((task, index) => {
      if (
        task.namaTugas.toLowerCase().includes(keyword) ||
        task.mataKuliah.toLowerCase().includes(keyword)
      ) {
        const li = document.createElement('li') 
        li.textContent = `${index} ${task.done} ${task.namaTugas} (${task.mataKuliah}) - ${task.deadline}`;
        if (task.done) li.style.textDecoration = 'line-through'
        ul.appendChild(li)
      }
    })
  })
}
