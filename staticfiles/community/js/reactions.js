document.addEventListener('DOMContentLoaded', function() {
    const emojiButtons = document.querySelectorAll('.emoji-btn');
    const emojiClickCounts = JSON.parse(localStorage.getItem('emojiClickCounts')) || {};

    // Function to update most clicked emoji on page load
    function updateMostClickedEmojiOnLoad(announcementId) {
        const mostClickedDiv = document.querySelector(`.announcement-card[data-announcement-id="${announcementId}"] .most-clicked`);
        if (mostClickedDiv) {
            let maxCount = 0;
            let mostClickedEmoji = null;

            // Calculate most clicked emoji from local storage
            for (const [emoji, count] of Object.entries(emojiClickCounts)) {
                if (count > maxCount) {
                    maxCount = count;
                    mostClickedEmoji = emoji;
                }
            }

            // Display result
            if (mostClickedEmoji) {
                mostClickedDiv.textContent = `Most Reacted: ${mostClickedEmoji}`;
            } else {
                mostClickedDiv.textContent = 'No reactions yet.';
            }
        }
    }

    // Function to update most clicked emoji after a reaction
    function updateMostClickedEmoji(announcementId) {
        const mostClickedDiv = document.querySelector(`.announcement-card[data-announcement-id="${announcementId}"] .most-clicked`);
        // Logic to calculate and display the most clicked emoji can be similar to above or adapted as needed.
        let maxCount = 0;
        let mostClickedEmoji = null;

        for (const [emoji, count] of Object.entries(emojiClickCounts)) {
            if (count > maxCount) {
                maxCount = count;
                mostClickedEmoji = emoji;
            }
        }

        if (mostClickedDiv) {
            if (mostClickedEmoji) {
                mostClickedDiv.textContent = `Most Reacted: ${mostClickedEmoji}`;
            } else {
                mostClickedDiv.textContent = 'No reactions yet.';
            }
        }
    }

    // Call this function for each announcement card on page load
    document.querySelectorAll('.announcement-card').forEach(card => {
        const announcementId = card.dataset.announcementId;
        updateMostClickedEmojiOnLoad(announcementId);
    });

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

                // Update most clicked emoji after reaction
                updateMostClickedEmoji(announcementId);
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

