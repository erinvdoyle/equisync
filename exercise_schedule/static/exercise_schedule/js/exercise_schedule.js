document.addEventListener("DOMContentLoaded", function () {

    //  Horse Select Change

    const horseSelect = document.getElementById("id_horse");
    const scheduleForm = document.getElementById("schedule-form");
  
    if (horseSelect && scheduleForm) {
      horseSelect.addEventListener("change", function () {
        const horseId = horseSelect.value;
        const selectedDate = document.getElementById("id_date")?.value;
  
        if (horseId) {
          fetch(`/exercise_schedule/daily_schedule/?horse_id=${horseId}&date=${selectedDate}`)
            .then((response) => response.text())
            .then((html) => {
              const parser = new DOMParser();
              const doc = parser.parseFromString(html, "text/html");
              const newForm = doc.getElementById("schedule-form");
  
              if (newForm) {
                scheduleForm.innerHTML = newForm.innerHTML;
                const restoredHorseSelect = document.getElementById("id_horse");
                if (restoredHorseSelect) restoredHorseSelect.value = horseId;
                const restoredDateInput = document.getElementById("id_date");
                if (restoredDateInput && selectedDate) restoredDateInput.value = selectedDate;
              }
            })
            .catch((error) => console.error("Error fetching schedule details:", error));
        }
      });
    }
  
    // Chart.js Setup

    if (document.getElementById("exerciseChart")) {
      const ctx = document.getElementById("exerciseChart").getContext("2d");
      const form = document.getElementById("timeframe-form");
      const radioButtons = form?.querySelectorAll('input[name="timeframe"]') || [];
      const minutesSection = document.getElementById("time-breakdown-minutes");
      const averageSection = document.getElementById("average-exercise-time");
      const weekSelect = document.getElementById("week-select");
      const updateButton = document.getElementById("update-button");
      const prevWeekButton = document.getElementById("prev-week");
      const nextWeekButton = document.getElementById("next-week");
  
      let myChart = new Chart(ctx, {
        type: "pie",
        data: {
          labels: [],
          datasets: [{
            label: "Exercise Breakdown",
            data: [],
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
  
      function updateChart() {
        const timeframe = form.querySelector('input[name="timeframe"]:checked')?.value;
        const startDate = form.start_date.value;
        const endDate = form.end_date.value;
  
        let url = `/exercise_schedule/horse_schedule/?`;
        if (timeframe === "custom") {
          url += `start_date=${startDate}&end_date=${endDate}`;
        } else {
          url += `timeframe=${timeframe}`;
        }
  
        fetch(url)
          .then(response => response.json())
          .then(data => {
            myChart.data.labels = data.labels;
            myChart.data.datasets[0].data = data.data;
            myChart.update();
  
            if (minutesSection) minutesSection.innerHTML = data.exercise_breakdown_minutes_html;
            if (timeframe !== "day" && averageSection) {
              averageSection.innerHTML = data.average_exercise_time_html;
            }
          });
      }
  
      function updateWeeklySchedule() {
        const selectedWeek = weekSelect?.value;
        if (!selectedWeek) return;
  
        fetch(`/exercise_schedule/weekly_schedule/?start_date=${selectedWeek}`)
          .then(res => res.json())
          .then(data => {
            const tableBody = document.querySelector("table tbody");
            if (!tableBody) return;
            tableBody.innerHTML = "";
  
            Object.entries(data.weekly_schedule_items).forEach(([day, items]) => {
              const row = document.createElement("tr");
              const dateCell = document.createElement("td");
              dateCell.textContent = new Date(day).toLocaleDateString("en-US", {
                weekday: "long", month: "short", day: "numeric", year: "numeric"
              });
              row.appendChild(dateCell);
  
              const exerciseTypeCell = document.createElement("td");
              const durationCell = document.createElement("td");
              const notesCell = document.createElement("td");
  
              if (items.length > 0) {
                items.forEach(item => {
                  const exDiv = document.createElement("div");
                  exDiv.textContent = item.exercise_type;
                  exerciseTypeCell.appendChild(exDiv);
  
                  const durDiv = document.createElement("div");
                  durDiv.textContent = item.duration;
                  durationCell.appendChild(durDiv);
                });
              } else {
                exerciseTypeCell.textContent = durationCell.textContent = notesCell.textContent = "No Schedule";
              }
  
              row.appendChild(exerciseTypeCell);
              row.appendChild(durationCell);
              row.appendChild(notesCell);
              tableBody.appendChild(row);
            });
  
            const today = new Date();
            const selectedWeekStart = new Date(selectedWeek);
            const currentWeekStart = new Date(today.setDate(today.getDate() - today.getDay()));
  
            if (selectedWeekStart.getTime() >= currentWeekStart.getTime()) {
              nextWeekButton.style.display = "none";
            } else {
              nextWeekButton.style.display = "inline-block";
            }
          });
      }
  
      radioButtons.forEach(rb => rb.addEventListener("change", updateChart));
      form.start_date.addEventListener("change", updateChart);
      form.end_date.addEventListener("change", updateChart);
      updateButton?.addEventListener("click", updateWeeklySchedule);
  
      prevWeekButton?.addEventListener("click", () => {
        const selected = weekSelect.value;
        const [y, m, d] = selected.split("-").map(Number);
        const prev = new Date(y, m - 1, d - 7);
        weekSelect.value = prev.toISOString().split("T")[0];
        updateWeeklySchedule();
      });
  
      nextWeekButton?.addEventListener("click", () => {
        const selected = weekSelect.value;
        const [y, m, d] = selected.split("-").map(Number);
        const next = new Date(y, m - 1, d + 7);
        weekSelect.value = next.toISOString().split("T")[0];
        updateWeeklySchedule();
      });
  
      updateWeeklySchedule();
    }
  
    // Exercise Modal Logic

    const modalOverlay = document.getElementById("exerciseModal");
    const modalClose = document.querySelector(".main-ex-modal-close");
    const modalTitle = document.querySelector(".modal-title");
    const modalDetails = document.getElementById("exercise-modal-details");
  
    function openModalWithSchedule(scheduleId, horseName, date) {
      modalTitle.textContent = `${horseName}'s Schedule, ${date}`;
      modalDetails.innerHTML = "Loading...";
  
      fetch(`/exercise_schedule/details/${scheduleId}/`)
        .then(res => res.text())
        .then(html => {
          modalDetails.innerHTML = html;
          modalOverlay.style.display = "flex";
        });
    }
  
    function openModalWithAppointment(horseName, date) {
      modalTitle.textContent = `${horseName}'s Appointments, ${date}`;
      modalDetails.innerHTML = "Loading...";
  
      fetch(`/exercise_schedule/appointments/${horseName}/${date}/`)
        .then(res => res.text())
        .then(html => {
          modalDetails.innerHTML = html;
          modalOverlay.style.display = "flex";
        });
    }
  
    modalClose?.addEventListener("click", () => {
      modalOverlay.style.display = "none";
    });
  
    window.addEventListener("click", (event) => {
      if (event.target === modalOverlay) {
        modalOverlay.style.display = "none";
      }
    });
  
    document.querySelectorAll(".details-link").forEach(link => {
      link.addEventListener("click", function () {
        const scheduleId = this.getAttribute("data-schedule-id");
        const horseName = this.getAttribute("data-horse-name");
        const date = this.getAttribute("data-date");
  
        if (scheduleId) {
          openModalWithSchedule(scheduleId, horseName, date);
        } else {
          openModalWithAppointment(horseName, date);
        }
      });
    });
  
    // Add Button Redirects
 
    const addExerciseBtn = document.getElementById("add-exercise-button");
    if (addExerciseBtn) {
    addExerciseBtn.addEventListener("click", () => {
        window.location.href = "/exercise_schedule/daily/";
    });
    }

  
    const addAppointmentBtn = document.getElementById("add-appointment-button");
    if (addAppointmentBtn) {
      addAppointmentBtn.addEventListener("click", () => {
        window.location.href = "/exercise_schedule/add_appointment/";
      });
    }
  });
  