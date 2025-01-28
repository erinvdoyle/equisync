console.log(document.getElementById('modalTitle')); 
console.log(document.getElementById('detailsModal')); 


// Function to open Ads Modal
function openModal(title, description, imageUrl) {
    document.getElementById('adModalLabel').textContent = title;
    document.getElementById('modalDescription').innerHTML = description;

    const image = document.getElementById('modalImage');
    if (imageUrl) {
        image.src = imageUrl;
        image.style.display = 'block';
    } else {
        image.style.display = 'none';
    }

    const adModal = new bootstrap.Modal(document.getElementById('adModal'));
    adModal.show();
}


// Function to open Announcements Modal
function openAnnouncementModal(title, content) {
    document.getElementById('announcementModalLabel').textContent = title;
    document.getElementById('modalAnnouncementContent').textContent = content;

    const announcementModal = new bootstrap.Modal(document.getElementById('announcementModal'));
    announcementModal.show();
}


