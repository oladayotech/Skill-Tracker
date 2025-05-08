const modalOverlay = document.getElementById('modalOverlay');
const modalText = document.getElementById('modalText');
const saveLogBtn = document.getElementById('saveLogBtn');
let activeDay = null;

const dayLogs = JSON.parse(localStorage.getItem('dayLogs')) || {};

// Show modal
function showModal(day) {
  activeDay = day;
  modalOverlay.style.display = 'flex';
  modalText.value = '';
}

// Hide modal
function hideModal() {
  modalOverlay.style.display = 'none';
}

// Save log to memory and localStorage
function saveLog() {
  const text = modalText.value.trim();
  if (!text) return;

  if (!dayLogs[activeDay]) dayLogs[activeDay] = [];
  dayLogs[activeDay].push(text);

  localStorage.setItem('dayLogs', JSON.stringify(dayLogs));
  updateDayLogs(activeDay);
  hideModal();
}

// Update logs shown inside calendar day
function updateDayLogs(day) {
  const logContainer = document.getElementById(`log-${day}`);
  if (!logContainer) return;
  logContainer.innerHTML = '';
  dayLogs[day]?.forEach(log => {
    const item = document.createElement('div');
    item.textContent = log;
    logContainer.appendChild(item);
  });
}

// Generate calendar UI
function generateCalendar() {
  calendarGrid.innerHTML = '';
  const daysInMay = 31;
  const startDay = 3;

  for (let i = 0; i < startDay; i++) {
    const emptyCell = document.createElement('div');
    emptyCell.className = 'calendar-cell empty';
    calendarGrid.appendChild(emptyCell);
  }

  for (let day = 1; day <= daysInMay; day++) {
    const cell = document.createElement('div');
    cell.className = 'calendar-cell filled';
    cell.innerHTML = `<strong>${day}</strong><div class="log-list" id="log-${day}"></div>`;

    cell.addEventListener('click', () => showModal(day));
    calendarGrid.appendChild(cell);

    updateDayLogs(day);
  }
}

// Event listeners
modalOverlay.addEventListener('click', (e) => {
  if (e.target === modalOverlay) hideModal();
});

saveLogBtn.addEventListener('click', saveLog);

generateCalendar();
generateHeatmap();
generatePieChart();
