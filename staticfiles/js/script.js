// Intro modal on index.html
document.addEventListener("DOMContentLoaded", function () {
    let introModal = new bootstrap.Modal(document.getElementById("introModal"), {
        backdrop: "static", 
        keyboard: false     
    });
    introModal.show();
});


const adModal = new bootstrap.Modal(document.getElementById('adModal'), { backdrop: true });
const announcementModal = new bootstrap.Modal(document.getElementById('announcementModal'), { backdrop: true });

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

    adModal.show();
}


// Function to open Announcements Modal
function openAnnouncementModal(title, content) {
    document.getElementById('announcementModalLabel').textContent = title;
    document.getElementById('modalAnnouncementContent').textContent = content;

    announcementModal.show();
}

// // Function for Performance Tracking
// document.addEventListener("DOMContentLoaded", function() {
//     var ctx = document.getElementById("performanceChart").getContext("2d");
//     var performanceChart = new Chart(ctx, {
//         type: "line",
//         data: {
//             labels: performanceData.dates,
//             datasets: [
//                 {
//                     label: "Performance Rating",
//                     data: performanceData.ratings,
//                     borderColor: "#ab68ff",
//                     backgroundColor: "rgba(171, 104, 255, 0.2)",
//                     fill: true,
//                 },
//                 {
//                     label: "Jump Height (cm)",
//                     data: performanceData.jump_heights,
//                     borderColor: "#19c37d",
//                     backgroundColor: "rgba(25, 195, 125, 0.2)",
//                     fill: true,
//                 },
//                 {
//                     label: "Number of Faults",
//                     data: performanceData.faults,
//                     borderColor: "#ef4444",
//                     backgroundColor: "rgba(239, 68, 68, 0.2)",
//                     fill: true,
//                 },
//             ],
//         },
//         options: {
//             responsive: true,
//             maintainAspectRatio: false,
//             scales: {
//                 y: {
//                     beginAtZero: true,
//                     title: {
//                         display: true,
//                         text: "Performance Metrics",
//                     },
//                 },
//                 x: {
//                     title: {
//                         display: true,
//                         text: "Event Date",
//                     },
//                 },
//             },
//         },
//     });
// });
