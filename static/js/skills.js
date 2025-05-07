// DOM Elements
const addEntryBtn = document.getElementById('addEntry');
const entryInput = document.getElementById('entryInput');
const calendarGrid = document.getElementById('calendarGrid');
const heatmap = document.getElementById('heatmap');

// Add new log entry (basic mock)
addEntryBtn.addEventListener('click', () => {
  const entry = entryInput.value.trim();
  if (entry) {
    alert(`Entry added: ${entry}`);
    entryInput.value = '';
  }
});

// Generate calendar (May example)
function generateCalendar() {
  const daysInMay = 31;
  const startDay = 3; // May 1st is a Wednesday

  for (let i = 0; i < startDay; i++) {
    const placeholder = document.createElement('div');
    placeholder.className = 'calendar-cell empty';
    calendarGrid.appendChild(placeholder);
  }

  for (let i = 1; i <= daysInMay; i++) {
    const day = document.createElement('div');
    day.className = 'calendar-cell filled';
    day.textContent = i;
    calendarGrid.appendChild(day);
  }
}

// Generate heatmap (mock activity levels)
function generateHeatmap() {
  const cells = 42;
  for (let i = 0; i < cells; i++) {
    const cell = document.createElement('div');
    const intensity = Math.floor(Math.random() * 5); // 0 to 4
    cell.className = `heat-cell level-${intensity}`;
    heatmap.appendChild(cell);
  }
}

// Pie Chart for skills
function generatePieChart() {
  const ctx = document.getElementById('skillChart').getContext('2d');
  new Chart(ctx, {
    type: 'doughnut',
    data: {
      labels: ['Backend', 'Frontend', 'DevOps'],
      datasets: [{
        data: [30, 50, 20],
        backgroundColor: ['#3b82f6', '#10b981', '#f59e0b'],
        borderWidth: 0
      }]
    },
    options: {
      cutout: '70%',
      plugins: {
        legend: {
          position: 'right',
          labels: {
            color: '#ccc',
            boxWidth: 12
          }
        }
      }
    }
  });
}

// Initialize
generateCalendar();
generateHeatmap();
generatePieChart();
