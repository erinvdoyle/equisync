// Get CSRF token from cookie
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        const cookies = document.cookie.split(";");
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.startsWith(name + "=")) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

document.addEventListener("DOMContentLoaded", function () {
    console.log("DOM loaded");

    // Sidebar Toggle
    const sidebar = document.querySelector(".sidebar");
    const caretToggle = document.querySelector(".sidebar-toggle-caret");

    function toggleSidebar() {
        if (window.innerWidth < 768) {
            sidebar.classList.toggle("sidebar-hidden");
            caretToggle.style.display = sidebar.classList.contains("sidebar-hidden") ? "block" : "none";
        }
    }

    caretToggle.addEventListener("click", function (event) {
        event.stopPropagation();
        toggleSidebar();
    });

    window.addEventListener("resize", function () {
        if (window.innerWidth >= 768) {
            sidebar.classList.remove("sidebar-hidden");
            sidebar.style.transform = "none";
            caretToggle.style.display = "none";
        } else {
            caretToggle.style.display = "block";
        }
    });

    // Navbar Toggle
    const navbarToggler = document.querySelector(".navbar-toggler");
    const navbarMenu = document.querySelector(".navbar-collapse");
    const profileDropdown = document.querySelector("#userDropdown");
    const profileMenu = profileDropdown?.nextElementSibling;
    const bsNavbar = new bootstrap.Collapse(navbarMenu, { toggle: false });

    navbarToggler.addEventListener("click", function (event) {
        event.stopPropagation();
        if (navbarMenu.classList.contains("show")) {
            bsNavbar.hide();
        } else {
            bsNavbar.show();
        }
    });

    profileDropdown?.addEventListener("click", function (event) {
        event.stopPropagation();
        let isDropdownOpen = profileMenu.classList.contains("show");
        document.querySelectorAll(".navbar .dropdown-menu.show").forEach(menu => {
            menu.classList.remove("show");
        });
        if (!isDropdownOpen) {
            profileMenu.classList.add("show");
        }
    });

    document.addEventListener("click", function (event) {
        if (!navbarMenu.contains(event.target) && !navbarToggler.contains(event.target)) {
            bsNavbar.hide();
        }
        if (!profileDropdown.contains(event.target) && !profileMenu.contains(event.target)) {
            profileMenu.classList.remove("show");
        }
    });

    document.querySelectorAll(".navbar .dropdown-toggle").forEach(function (dropdown) {
        dropdown.addEventListener("click", function (event) {
            event.stopPropagation();
            const dropdownMenu = this.nextElementSibling;
            document.querySelectorAll(".navbar .dropdown-menu.show").forEach(menu => {
                if (menu !== dropdownMenu) menu.classList.remove("show");
            });
            dropdownMenu.classList.toggle("show");
        });
    });

    // Sidebar menu scrolling
    document.querySelectorAll(".sidebar-menu a").forEach(link => {
        link.addEventListener("click", function (event) {
            event.preventDefault();
            const targetId = this.getAttribute("href").substring(1);
            document.getElementById(targetId).scrollIntoView({ behavior: "smooth" });
        });
    });

    // const messages = document.querySelectorAll(".fade-message");
    // messages.forEach(msg => {
    //     setTimeout(() => {
    //         msg.style.opacity = "0";
    //     }, 3500);
    // });

    // Fade out elements with .fade-message
    const fadeMessages = document.querySelectorAll(".fade-message");
    fadeMessages.forEach(msg => {
        setTimeout(() => {
            msg.style.opacity = "0";
        }, 3500);
    });

    // Fade out and remove .fade-out messages
    const fadeOuts = document.querySelectorAll(".fade-out");
    if (fadeOuts.length) {
        setTimeout(() => {
            fadeOuts.forEach(msg => {
                msg.classList.add("fade");
                setTimeout(() => msg.remove(), 1000); // remove after fade animation
            });
        }, 3000);
    }


    updateNavbarNotificationBadge();
});

// Notifications
function markNotificationAsRead(button, type) {
    const notificationId = button.getAttribute("data-notification-id");
    fetch(`/notifications/mark-as-read/${notificationId}/`, {
        method: "POST",
        headers: { "X-CSRFToken": getCookie("csrftoken") }
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            const listItem = document.getElementById(`${type}-notification-${notificationId}`);
            if (listItem) {
                listItem.remove();
            }
            updateNavbarNotificationBadge();
        }
    })
    .catch(error => console.error("Error:", error));
}

function updateNavbarNotificationBadge() {
    const unreadCount = document.querySelectorAll('.notification-bell').length;
    const badge = document.querySelector('.navbar-nav .badge');
    if (badge) {
        badge.textContent = unreadCount > 0 ? unreadCount : "";
        badge.style.display = unreadCount > 0 ? "block" : "none";
    }
}
