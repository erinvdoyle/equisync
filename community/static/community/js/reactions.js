document.addEventListener('DOMContentLoaded', function() {
    const emojiButtons = document.querySelectorAll('.emoji-btn');
    const emojiClickCounts = JSON.parse(localStorage.getItem('emojiClickCounts')) || {};

    emojiButtons.forEach(button => {
        button.addEventListener('click', function() {
            console.log('Emoji button clicked!');
            const announcementId = this.dataset.announcementId;
            const emoji = this.dataset.emoji;
            const btn = this;

            // Update click count
            if (emojiClickCounts[emoji]) {
                emojiClickCounts[emoji]++;
            } else {
                emojiClickCounts[emoji] = 1;
            }

            // Save click counts to local storage
            localStorage.setItem('emojiClickCounts', JSON.stringify(emojiClickCounts));

            console.log("Emoji Click Counts:", emojiClickCounts); 

            fetch('/community/react/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'X-CSRFToken': getCookie('csrftoken')
                },
                body: `announcement_id=${announcementId}&emoji=${emoji}`
            })
            .then(response => response.json())
            .then(data => {
                if (data.status === 'added') {
                    btn.classList.add("active");
                } else if (data.status === 'removed') {
                    btn.classList.remove("active");
                } else {
                    alert('Error: ' + data.message);
                    return; 
                }

                // Update most clicked emoji
                const mostClickedDiv = document.querySelector(`.announcement-card[data-announcement-id="${announcementId}"] .most-clicked`);
                if (mostClickedDiv) {
                    if (data.most_clicked_emoji) {
                        mostClickedDiv.textContent = `Most Reacted: ${data.most_clicked_emoji}`;
                    } else {
                        mostClickedDiv.textContent = '';
                    }
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
        });
    });

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                let cookie = cookies[i].trim();

                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});

