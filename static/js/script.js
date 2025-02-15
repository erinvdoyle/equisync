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

//js for exercise chart
// document.addEventListener('DOMContentLoaded', function () {
//     console.log("Script.js is running!");
//     try {
//         const ctx = document.getElementById('exerciseChart').getContext('2d');
//         const labels = JSON.parse(document.getElementById('chartLabels').textContent);
//         const data = JSON.parse(document.getElementById('chartData').textContent);

//         console.log("Labels:", labels);
//         console.log("Data:", data);

//         const myChart = new Chart(ctx, {
//             type: 'pie',
//             data: {
//                 labels: labels,
//                 datasets: [{
//                     label: 'Exercise Breakdown',
//                     data: data,
//                     backgroundColor: [
//                         'rgba(255, 99, 132, 0.2)',
//                         'rgba(54, 162, 235, 0.2)',
//                         'rgba(255, 206, 86, 0.2)',
//                         'rgba(75, 192, 192, 0.2)',
//                         'rgba(153, 102, 255, 0.2)',
//                         'rgba(255, 159, 64, 0.2)'
//                     ],
//                     borderColor: [
//                         'rgba(255, 99, 132, 1)',
//                         'rgba(54, 162, 235, 1)',
//                         'rgba(255, 206, 86, 1)',
//                         'rgba(75, 192, 192, 1)',
//                         'rgba(153, 102, 255, 1)',
//                         'rgba(255, 159, 64, 1)'
//                     ],
//                     borderWidth: 1
//                 }]
//             },
//             options: {
//                 responsive: true,
//                 maintainAspectRatio: false,
//                 plugins: {
//                     legend: {
//                         position: 'top',
//                     },
//                     title: {
//                         display: true,
//                         text: 'Exercise Breakdown',
//                         padding: 10,
//                         font: {
//                             size: 16
//                         }
//                     }
//                 }
//             }
//         });
//     } catch (error) {
//         console.error("Error creating chart:", error);
//     }
// });
