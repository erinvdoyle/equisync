document.addEventListener("DOMContentLoaded", function () {
    console.log("DOM is fully loaded");

    // Weekly Events
    let currentDate = new Date();

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
            })
            .catch(error => console.error('Error fetching weekly events:', error));
    }

    // Load current week on page load
    updateWeeklyEvents('select', currentDate.toISOString().split('T')[0]);

    // Attach event listeners only if buttons/dropdowns exist
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

    // Ad Modal
    window.openModal = function (type, description, imageUrl, adTitle = '', price = '') {
        if (!adModal) return;
    
        const modalTitle = document.getElementById('adModalLabel');
        const image = document.getElementById('modalImage');
        const desc = document.getElementById('modalDescription');
        const priceEl = document.getElementById('modalPrice');
    
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
    
        adModal.show();
    };
    

    // Announcements Modal
    const announcementModalEl = document.getElementById('announcementModal');
    const announcementModal = announcementModalEl ? new bootstrap.Modal(announcementModalEl, { backdrop: true }) : null;

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
});

