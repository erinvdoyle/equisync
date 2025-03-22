// Intro modal on index.html
document.addEventListener("DOMContentLoaded", function () {
    let introModal = new bootstrap.Modal(document.getElementById("introModal"), {
        backdrop: "static", 
        keyboard: false     
    });
    introModal.show();
});

// Fading Alert Messages
window.addEventListener('DOMContentLoaded', () => {
    const messages = document.querySelectorAll('.fade-out');
    if (messages.length) {
        setTimeout(() => {
            messages.forEach(msg => {
                msg.classList.add('fade');
                setTimeout(() => msg.remove(), 1000);
            });
        }, 3000);
    }
});

