document.addEventListener("DOMContentLoaded", function () {
    // Fade messages
    const messages = document.querySelectorAll(".fade-message");
    messages.forEach((msg) => {
      setTimeout(() => {
        msg.style.opacity = "0";
      }, 4000);
  
      setTimeout(() => {
        msg.style.display = "none";
      }, 5000);
    });
  
    // Validate start and end times
    const startInput = document.getElementById("start_time");
    const endInput = document.getElementById("end_time");
  
    if (startInput && endInput) {
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
      if (form) {
        form.addEventListener("submit", function (e) {
          if (!validateTimes()) {
            e.preventDefault();
          }
        });
      }
    }
  
    // Toggle horse detail UI
    const toggleAddHorseBtn = document.getElementById("toggleAddHorseDetails");
    if (toggleAddHorseBtn) {
      toggleAddHorseBtn.addEventListener("click", function () {
        const container = document.getElementById("addHorseDetailsContainer");
        if (container) {
          container.style.display =
            container.style.display === "none" ? "block" : "none";
        }
      });
    }
  
    // Add more class detail fields
    const addClassBtn = document.getElementById("addAnotherClass");
    if (addClassBtn) {
      addClassBtn.addEventListener("click", function () {
        const container = document.getElementById("classDetailsContainer");
        if (container) {
          const newDiv = document.createElement("div");
          newDiv.classList.add("class-detail-field");
          newDiv.innerHTML = `
            <label>Class Details:</label>
            <input type="text" name="class_details[]">
            <label>Notes:</label>
            <textarea name="notes[]"></textarea>`;
          container.appendChild(newDiv);
        }
      });
    }
  
    // Toggle search overlay
    window.toggleSearch = function () {
      const overlay = document.querySelector(".search-overlay");
      if (overlay) {
        overlay.classList.toggle("active");
        if (overlay.classList.contains("active")) {
          overlay.querySelector("input")?.focus();
        }
      }
    };
  
    window.closeSearch = function () {
      const overlay = document.querySelector(".search-overlay");
      if (overlay) {
        overlay.classList.remove("active");
      }
    };
  
    // Sort & filter results (horse_results_archive.html)
    const resultsList = document.getElementById("resultsList");
    const sortSelect = document.getElementById("sortResults");
    const filterSelect = document.getElementById("filterMonth");
  
    if (resultsList && sortSelect && filterSelect) {
      function sortResults() {
        const items = Array.from(resultsList.getElementsByClassName("result-item"));
        const sortValue = sortSelect.value;
  
        items.sort((a, b) => {
          const dateA = new Date(a.dataset.date);
          const dateB = new Date(b.dataset.date);
          const titleA = a.dataset.title.toLowerCase();
          const titleB = b.dataset.title.toLowerCase();
          const heightA = parseFloat(a.dataset.height);
          const heightB = parseFloat(b.dataset.height);
  
          switch (sortValue) {
            case "date": return dateB - dateA;
            case "date_asc": return dateA - dateB;
            case "title": return titleA.localeCompare(titleB);
            case "title_desc": return titleB.localeCompare(titleA);
            case "height": return heightB - heightA;
            case "height_asc": return heightA - heightB;
            default: return 0;
          }
        });
  
        resultsList.innerHTML = "";
        items.forEach(item => resultsList.appendChild(item));
      }
  
      function filterResults() {
        const items = Array.from(resultsList.getElementsByClassName("result-item"));
        const filterValue = filterSelect.value;
        const now = new Date();
  
        items.forEach(item => {
          const itemDate = new Date(item.dataset.date);
          let show = true;
  
          if (filterValue === "this_month") {
            show = itemDate.getFullYear() === now.getFullYear() &&
                   itemDate.getMonth() === now.getMonth();
          } else if (filterValue === "this_year") {
            show = itemDate.getFullYear() === now.getFullYear();
          } else if (filterValue === "last_6") {
            const sixMonthsAgo = new Date();
            sixMonthsAgo.setMonth(now.getMonth() - 6);
            show = itemDate >= sixMonthsAgo;
          }
  
          item.style.display = show ? "block" : "none";
        });
      }
  
      sortSelect.addEventListener("change", sortResults);
      filterSelect.addEventListener("change", filterResults);
      sortResults();
    }
  });
  