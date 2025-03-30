document.addEventListener("DOMContentLoaded", function () {
    const messages = document.querySelectorAll(".fade-message");
  
    messages.forEach((msg) => {
      setTimeout(() => {
        msg.style.opacity = "0";
      }, 3000);
    });
  });
  