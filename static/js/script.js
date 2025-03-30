// Intro modal on index.html
document.addEventListener("DOMContentLoaded", function () {
    let introModal = document.getElementById("introModal");
    if (introModal) {
        new bootstrap.Modal(introModal, {
            backdrop: "static",
            keyboard: false
        }).show();
    }

    // Fading Alert Messages with close button
    const messages = document.querySelectorAll(".fade-message");

    messages.forEach((msg) => {
        // Auto fade
        setTimeout(() => {
            if (msg.style.display !== "none") {
                msg.style.opacity = "0";
            }
        }, 3000);

        // Remove from layout after fade
        setTimeout(() => {
            if (msg.style.opacity === "0") {
                msg.style.display = "none";
            }
        }, 4000);

        // Close button logic
        const closeBtn = msg.querySelector(".close-btn");
        if (closeBtn) {
            closeBtn.addEventListener("click", function () {
                msg.style.display = "none";
            });
        }
    });
});