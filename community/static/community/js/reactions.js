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

                // Update most clicked emoji based on local storage counts
                updateMostClickedEmoji(announcementId);
            })
            .catch(error => {
                console.error('Error:', error);
            });
        });
    });

    function updateMostClickedEmoji(announcementId) {
        // Find the most clicked emoji
        let maxCount = 0;
        let mostClickedEmoji = null;

        for (const [emoji, count] of Object.entries(emojiClickCounts)) {
            if (count > maxCount) {
                maxCount = count;
                mostClickedEmoji = emoji;
            }
        }

        // Update the display
        const mostClickedDiv = document.querySelector(`.announcement-card[data-announcement-id="${announcementId}"] .most-clicked`);
        if (mostClickedDiv) {
            if (mostClickedEmoji) {
                mostClickedDiv.textContent = `Most Reacted: ${mostClickedEmoji}`;
            } else {
                mostClickedDiv.textContent = 'No reactions yet.';
            }
        }
    }

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
