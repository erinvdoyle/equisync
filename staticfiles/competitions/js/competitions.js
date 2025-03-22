document.addEventListener("DOMContentLoaded", function () {
    const messages = document.querySelectorAll(".fade-message");
  
    messages.forEach((msg) => {
      setTimeout(() => {
        msg.style.opacity = "0";
      }, 4000);
  
      setTimeout(() => {
        msg.style.display = "none";
      }, 5000);
    });
  });
  
  document.addEventListener('DOMContentLoaded', function () {
    const startInput = document.getElementById("start_time");
    const endInput = document.getElementById("end_time");

    const errorDiv = document.createElement("div");
    errorDiv.className = "invalid-feedback d-block mt-1";
    errorDiv.style.display = "none";
    errorDiv.innerText = "End time must be after start time.";

    endInput.parentNode.appendChild(errorDiv);

    function validateTimes() {
        const start = new Date(startInput.value);
        const end = new Date(endInput.value);

        if (startInput.value && endInput.value && end <= start) {
            endInput.classList.add("is-invalid");
            errorDiv.style.display = "block";
            return false;
        } else {
            endInput.classList.remove("is-invalid");
            errorDiv.style.display = "none";
            return true;
        }
    }

    startInput.addEventListener("change", validateTimes);
    endInput.addEventListener("change", validateTimes);

    const form = document.querySelector("form.event-form");
    form.addEventListener("submit", function (e) {
        if (!validateTimes()) {
            e.preventDefault();
        }
    });
});

function updateEventFields(eventData) {
    document.getElementById('title').value = eventData.title || '';
    document.getElementById('description').value = eventData.description || '';
    document.getElementById('start_time').value = eventData.start_time || '';
    document.getElementById('end_time').value = eventData.end_time || '';
}

function fetchEventDetails(eventId) {
    if (!eventId) return;
    
    fetch(`/competitions/get_event_details/${eventId}/`)
        .then(response => response.json())
        .then(data => {
            updateEventFields(data);
        })
        .catch(error => console.error('Error fetching event details:', error));
}

// JavaScript to toggle visibility of the add horse details container
document.getElementById("toggleAddHorseDetails").addEventListener("click", function() {
    var container = document.getElementById("addHorseDetailsContainer");
    container.style.display = (container.style.display === "none") ? "block" : "none";
});

// JavaScript to add more class detail fields
document.getElementById("addAnotherClass").addEventListener("click", function() {
    var classDetailsContainer = document.getElementById("classDetailsContainer");
    var newClassDiv = document.createElement("div");
    newClassDiv.classList.add("class-detail-field");
    
    newClassDiv.innerHTML = `
        <label>Class Details:</label>
        <input type="text" name="class_details[]">
        <label>Notes:</label>
        <textarea name="notes[]"></textarea>`;
    
    classDetailsContainer.appendChild(newClassDiv);
});