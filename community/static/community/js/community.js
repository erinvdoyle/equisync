document.addEventListener("DOMContentLoaded", function () {
  console.log("DOM is fully loaded");

  // Weekly Events
  let currentDate = new Date();

  function attachWeeklyEventListeners() {
    const prevBtn = document.getElementById('previous-week-button');
    const nextBtn = document.getElementById('next-week-button');
    const recentWeeksDropdown = document.getElementById('recent-weeks');

    if (prevBtn) {
      prevBtn.addEventListener('click', () => updateWeeklyEvents('previous'));
    }

    if (nextBtn) {
      nextBtn.addEventListener('click', () => updateWeeklyEvents('next'));
    }

    if (recentWeeksDropdown) {
      recentWeeksDropdown.addEventListener('change', function () {
        updateWeeklyEvents('select', this.value);
      });
    }
  }

  function updateWeeklyEvents(direction, selectedDate = null) {
    if (direction === 'previous') {
      currentDate.setDate(currentDate.getDate() - 7);
      document.getElementById('recent-weeks').selectedIndex = 0;
    } else if (direction === 'next') {
      currentDate.setDate(currentDate.getDate() + 7);
      document.getElementById('recent-weeks').selectedIndex = 0;
    } else if (direction === 'select' && selectedDate) {
      currentDate = new Date(selectedDate);
    }

    const year = currentDate.getFullYear();
    const month = currentDate.getMonth() + 1;
    const day = currentDate.getDate();

    const url = `/community/get-weekly-events/${year}/${month}/${day}/`;

    fetch(url)
      .then(response => {
        if (!response.ok) throw new Error('Fetch failed');
        return response.json();
      })
      .then(data => {
        document.getElementById("weekly-events-container").innerHTML = data.html;
        attachWeeklyEventListeners(); 
      })
      .catch(error => console.error('Error fetching weekly events:', error));
  }

  attachWeeklyEventListeners(); 
  updateWeeklyEvents('select', currentDate.toISOString().split('T')[0]);

  // Ad Modal
  window.openModal = function (
    type,
    description,
    imageUrl,
    adTitle = '',
    price = '',
    contactEmail = ''
  ) {
    const adModal = new bootstrap.Modal(document.getElementById('adModal'));
    const modalTitle = document.getElementById('adModalLabel');
    const image = document.getElementById('modalImage');
    const desc = document.getElementById('modalDescription');
    const priceEl = document.getElementById('modalPrice');
    const contactLink = document.getElementById('modalContactLink');

    modalTitle.textContent = adTitle || type;
    desc.innerHTML = description;
    priceEl.textContent = price ? `Price: ${price}` : '';

    if (imageUrl && imageUrl !== "None") {
      if (!imageUrl.startsWith("http")) {
        imageUrl = `https://res.cloudinary.com/dxpbpx72q/image/upload/v1/${imageUrl}`;
      }
      image.src = imageUrl;
      image.style.display = 'block';
    } else {
      image.style.display = 'none';
    }

    if (contactEmail) {
      const subject = encodeURIComponent('Interested in your ad');
      const body = encodeURIComponent(`Hi, I'm interested in your listing: ${adTitle || type}`);
      contactLink.href = `mailto:${contactEmail}?subject=${subject}&body=${body}`;
      contactLink.style.display = 'inline-block';
    } else {
      contactLink.style.display = 'none';
    }

    adModal.show();
  };

  // Announcements Modal
  const announcementModalEl = document.getElementById('announcementModal');
  const announcementModal = announcementModalEl
    ? new bootstrap.Modal(announcementModalEl, { backdrop: true })
    : null;

  window.openAnnouncementModal = function (title, content, imageUrl) {
    if (!announcementModal) return;

    document.getElementById('announcementModalLabel').textContent = title;
    document.getElementById('modalAnnouncementContent').textContent = content;

    const imageElement = document.getElementById('modalAnnouncementImage');

    if (imageUrl) {
      imageElement.src = imageUrl;
      imageElement.style.display = 'block';
    } else {
      imageElement.style.display = 'none';
    }

    announcementModal.show();
  };

  // Edit Ad Form
  window.populateForm = function (selectElement) {
    const selectedOption = selectElement.options[selectElement.selectedIndex];

    if (selectedOption.value) {
      document.getElementById("id_description").value = selectedOption.getAttribute("data-description");
      document.getElementById("id_contact_info").value = selectedOption.getAttribute("data-contact_info");
      document.getElementById("id_category").value = selectedOption.getAttribute("data-category");
      document.getElementById("id_ad_type").value = selectedOption.getAttribute("data-ad_type");
      document.getElementById("id_price").value = selectedOption.getAttribute("data-price");

      const deleteButton = document.getElementById("delete-ad-btn");
      if (deleteButton) {
        deleteButton.style.display = "inline-block";
        deleteButton.setAttribute("data-ad-id", selectedOption.value);
      }
    } else {
      const form = document.getElementById("edit-form");
      if (form) form.reset();

      const deleteButton = document.getElementById("delete-ad-btn");
      if (deleteButton) deleteButton.style.display = "none";
    }
  };

  window.confirmDelete = function () {
    const deleteButton = document.getElementById("delete-ad-btn");
    const adId = deleteButton ? deleteButton.getAttribute("data-ad-id") : null;
    if (adId && confirm("Are you sure you want to delete this ad?")) {
      window.location.href = `/community/ads/delete/${adId}/`;
    }
  };

  // Edit Announcement Form
  window.populateAnnouncementForm = function (selectElement) {
    const selectedOption = selectElement.options[selectElement.selectedIndex];

    if (selectedOption.value) {
      document.getElementById("id_description").value = selectedOption.getAttribute("data-description");
      document.getElementById("id_contact_info").value = selectedOption.getAttribute("data-contact_info");
      document.getElementById("announcement-id-hidden").value = selectedOption.value;

      const deleteForm = document.getElementById("delete-form");
      if (deleteForm) {
        deleteForm.action = `/community/announcements/delete/${selectedOption.value}/`;
        deleteForm.style.display = "inline-block";
      }
    } else {
      const form = document.getElementById("edit-form");
      if (form) form.reset();

      const deleteForm = document.getElementById("delete-form");
      if (deleteForm) deleteForm.style.display = "none";
    }
  };
});
