document.addEventListener("DOMContentLoaded", function () {
    // Collapsible Sections
    document.querySelectorAll(".collapsible-header").forEach(header => {
        header.addEventListener("click", function () {
            const content = this.nextElementSibling;
            content.classList.toggle("active");
            content.style.display = content.style.display === "block" ? "none" : "block";
        });
    });

    // Delete horse button
    const deleteBtn = document.querySelector(".delete-horse");
    if (deleteBtn) {
        deleteBtn.addEventListener("click", function () {
            const horseId = this.getAttribute("data-horse-id");
            const csrfToken = this.getAttribute("data-csrf-token");

            if (!horseId) {
                alert("Horse ID missing.");
                return;
            }

            if (confirm("Are you sure you want to remove this horse?")) {
                fetch(`/horses/delete/${horseId}/`, {
                    method: "POST",
                    headers: {
                        "X-CSRFToken": csrfToken,
                        "Content-Type": "application/json"
                    }
                })
                .then(response => {
                    if (response.ok) {
                        alert("Horse removed successfully.");
                        window.location.href = "/horses/";
                    } else {
                        alert("Error: Unable to remove horse.");
                    }
                })
                .catch(error => console.error("Error:", error));
            }
        });
    }
    
    // Image preview
    const imageInput = document.getElementById("imageUpload");
    const imagePreview = document.getElementById("horseImagePreview");
    const defaultThumbnail = document.getElementById("defaultThumbnail");

    if (imageInput) {
        imageInput.addEventListener("change", function () {
            const file = this.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = function (e) {
                    imagePreview.src = e.target.result;
                    imagePreview.style.display = "block";
                    if (defaultThumbnail) defaultThumbnail.style.display = "none";
                };
                reader.readAsDataURL(file);
            }
        });
    }

    // Helper to get CSRF token from cookies
    function getCSRFToken() {
        const name = "csrftoken";
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            if (cookie.startsWith(name + "=")) {
                return decodeURIComponent(cookie.substring(name.length + 1));
            }
        }
        return "";
    }
});
