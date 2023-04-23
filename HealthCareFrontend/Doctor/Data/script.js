document.addEventListener("DOMContentLoaded", function () {
    const addButton = document.querySelector(".add-row-button");
    if (addButton) {
      addButton.addEventListener("click", addRow);
    }
  });
  
  function addRow() {
    const table = document.querySelector("table tbody");
    if (!table) {
      return;
    }
  
    const newRow = document.createElement("tr");
  
    for (let i = 0; i < 2; i++) {
      const newCell = document.createElement("td");
      newCell.textContent = "New Data ";
      newRow.appendChild(newCell);
    }
  
    table.appendChild(newRow);
  }
  