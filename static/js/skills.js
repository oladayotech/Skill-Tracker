const addEntryBtn = document.getElementById('addEntry');
  const entryInput = document.getElementById('entryInput');
  const calendarGrid = document.getElementById('calendarGrid');
  const heatmap = document.getElementById('heatmap');
  const logDisplay = document.getElementById('logDisplay');

  // Optional general log area
  addEntryBtn.addEventListener('click', () => {
    const entry = entryInput.value.trim();
    if (entry) {
      const log = document.createElement('div');
      log.className = 'log-entry';
      log.textContent = `• ${entry}`;
      logDisplay.prepend(log);
      entryInput.value = '';
    }
  });

  const dayLogs = {}; // Store logs for each day

  function generateCalendar() {
    calendarGrid.innerHTML = '';
    const daysInMay = 31;
    const startDay = 3; // May 1 is Wednesday

    for (let i = 0; i < startDay; i++) {
      const emptyCell = document.createElement('div');
      emptyCell.className = 'calendar-cell empty';
      calendarGrid.appendChild(emptyCell);
    }

    for (let day = 1; day <= daysInMay; day++) {
      const cell = document.createElement('div');
      cell.className = 'calendar-cell filled';
      cell.innerHTML = `<strong>${day}</strong><div class="log-list" id="log-${day}"></div>`;

      // On click, prompt for log input
      cell.addEventListener('click', () => {
        const entry = prompt(`Add log for May ${day}:`);
        if (entry) {
          if (!dayLogs[day]) dayLogs[day] = [];
          dayLogs[day].push(entry);
          updateDayLogs(day);
        }
      });

      calendarGrid.appendChild(cell);
    }
  }

  function updateDayLogs(day) {
    const logContainer = document.getElementById(`log-${day}`);
    if (!logContainer) return;
    logContainer.innerHTML = '';
    dayLogs[day].forEach(log => {
      const item = document.createElement('div');
      item.textContent = log;
      logContainer.appendChild(item);
    });
  }

  function generateHeatmap() {
    heatmap.innerHTML = '';
    const cells = 42;
    for (let i = 0; i < cells; i++) {
      const cell = document.createElement('div');
      const intensity = Math.floor(Math.random() * 5);
      cell.className = `heat-cell level-${intensity}`;
      heatmap.appendChild(cell);
    }
  }

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

  generateCalendar();
  generateHeatmap();
  generatePieChart();