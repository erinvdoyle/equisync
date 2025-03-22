document.addEventListener("DOMContentLoaded", function () {
    // ---------- Modal Logic (Exercise Details) ----------
    const exerciseModal = document.getElementById("exerciseModal");
    const closeModalButton = document.querySelector(".exercise-close");

    if (exerciseModal && closeModalButton) {
        closeModalButton.addEventListener("click", () => {
            exerciseModal.style.display = 'none';
        });

        window.addEventListener("click", event => {
            if (event.target === exerciseModal) {
                exerciseModal.style.display = 'none';
            }
        });
    }

    document.querySelectorAll(".details-link").forEach(link => {
        link.addEventListener("click", function () {
            const scheduleId = this.dataset.scheduleId;
            const horseName = this.dataset.horseName;
            const date = this.dataset.date;

            if (scheduleId) {
                fetch(`/exercise_schedule/details/${scheduleId}/`)
                    .then(response => response.text())
                    .then(html => {
                        document.querySelector("#exerciseModal .modal-title").textContent = `${horseName}'s Schedule, ${date}`;
                        document.getElementById("exercise-modal-details").innerHTML = html;
                        exerciseModal.style.display = 'block';
                    });
            } else {
                fetch(`/exercise_schedule/appointments/${horseName}/${date}/`)
                    .then(response => response.text())
                    .then(html => {
                        document.querySelector("#exerciseModal .modal-title").textContent = `${horseName}'s Appointments, ${date}`;
                        document.getElementById("exercise-modal-details").innerHTML = html;
                        exerciseModal.style.display = 'block';
                    });
            }
        });
    });

    // ---------- Add Exercise/Appointment Buttons ----------
    const exerciseBtn = document.getElementById("add-exercise-button");
    const appointmentBtn = document.getElementById("add-appointment-button");

    if (exerciseBtn) {
        const url = exerciseBtn.dataset.url;
        exerciseBtn.addEventListener("click", () => window.location.href = url);
    }

    if (appointmentBtn) {
        const url = appointmentBtn.dataset.url;
        appointmentBtn.addEventListener("click", () => window.location.href = url);
    }

    // ---------- Chart & Time Breakdown (Horse Detail Page) ----------
    const chartCanvas = document.getElementById('exerciseChart');
    if (chartCanvas) {
        const ctx = chartCanvas.getContext('2d');
        const labels = JSON.parse(chartCanvas.dataset.labels);
        const data = JSON.parse(chartCanvas.dataset.data);

        new Chart(ctx, {
            type: 'pie',
            data: {
                labels: labels,
                datasets: [{
                    label: 'Exercise Breakdown',
                    data: data,
                    backgroundColor: [
                        'rgba(255, 99, 132, 0.2)',
                        'rgba(54, 162, 235, 0.2)',
                        'rgba(255, 206, 86, 0.2)',
                        'rgba(75, 192, 192, 0.2)',
                        'rgba(153, 102, 255, 0.2)',
                        'rgba(255, 159, 64, 0.2)'
                    ],
                    borderColor: [
                        'rgba(255, 99, 132, 1)',
                        'rgba(54, 162, 235, 1)',
                        'rgba(255, 206, 86, 1)',
                        'rgba(75, 192, 192, 1)',
                        'rgba(153, 102, 255, 1)',
                        'rgba(255, 159, 64, 1)'
                    ],
                    borderWidth: 1
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: { position: 'top' },
                    title: {
                        display: true,
                        text: 'Exercise Breakdown',
                        padding: 10,
                        font: { size: 16 }
                    }
                }
            }
        });
    }

    // ---------- Weekly Schedule Dropdown (Horse Detail Page) ----------
    const weekSelect = document.getElementById('week-select');
    const updateButton = document.getElementById('update-button');
    const prevWeekButton = document.getElementById('prev-week');
    const nextWeekButton = document.getElementById('next-week');

    function updateWeeklySchedule(horseId) {
        const selectedWeek = weekSelect.value;
        fetch(`/exercise_schedule/weekly/${horseId}/?start_date=${selectedWeek}`)
            .then(response => response.json())
            .then(data => {
                const tableBody = document.querySelector('table tbody');
                tableBody.innerHTML = '';

                Object.entries(data.weekly_schedule_items).forEach(([day, items]) => {
                    const row = document.createElement('tr');
                    row.innerHTML += `<td>${new Date(day).toLocaleDateString()}</td>`;

                    const types = items.map(i => `<div>${i.exercise_type}</div>`).join('') || 'No Schedule';
                    const durations = items.map(i => `<div>${i.duration}</div>`).join('') || 'No Schedule';

                    row.innerHTML += `<td>${types}</td><td>${durations}</td><td></td>`;
                    tableBody.appendChild(row);
                });

                const today = new Date();
                const selected = new Date(selectedWeek);
                const startOfWeek = new Date(today.setDate(today.getDate() - today.getDay()));

                nextWeekButton.style.display = selected >= startOfWeek ? 'none' : 'inline-block';
            });
    }

    if (updateButton && weekSelect && updateButton.dataset.horseId) {
        const horseId = updateButton.dataset.horseId;

        updateButton.addEventListener("click", () => updateWeeklySchedule(horseId));

        prevWeekButton?.addEventListener("click", () => {
            const date = new Date(weekSelect.value);
            date.setDate(date.getDate() - 7);
            weekSelect.value = date.toISOString().split('T')[0];
            updateWeeklySchedule(horseId);
        });

        nextWeekButton?.addEventListener("click", () => {
            const date = new Date(weekSelect.value);
            date.setDate(date.getDate() + 7);
            weekSelect.value = date.toISOString().split('T')[0];
            updateWeeklySchedule(horseId);
        });

        // Initial load
        updateWeeklySchedule(horseId);
    }

    // ---------- Dynamic Horse Select (Daily Form) ----------
    const horseSelect = document.getElementById("id_horse");
    const scheduleForm = document.getElementById("schedule-form");

    if (horseSelect && scheduleForm) {
        const date = horseSelect.dataset.date;
        horseSelect.addEventListener("change", function () {
            const horseId = this.value;
            fetch(`/exercise_schedule/daily/?horse_id=${horseId}&date=${date}`)
                .then(response => response.text())
                .then(html => {
                    const parser = new DOMParser();
                    const doc = parser.parseFromString(html, 'text/html');
                    const newForm = doc.getElementById("schedule-form");
                    scheduleForm.innerHTML = newForm.innerHTML;
                });
        });
    }
});

