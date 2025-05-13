const modalOverlay = document.getElementById('modalOverlay');
const modalText = document.getElementById('modalText');
const saveLogBtn = document.getElementById('saveLogBtn');
const calendarGrid = document.getElementById('calendarGrid');
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

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let cookie of cookies) {
      cookie = cookie.trim();
      if (cookie.startsWith(name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
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
  fetch('/api/logs/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': getCookie('csrftoken'),
    },
    body: JSON.stringify({
      day: activeDay,
      month: 'May',
      year: 2025,
      log_text: text,
    }),
  });
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

document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') hideModal();
});