document.addEventListener('DOMContentLoaded', function () {
    const emojiButtons = document.querySelectorAll('.emoji-btn');
    const stored = localStorage.getItem('emojiClickCounts');
    const emojiClickCounts = stored ? JSON.parse(stored) : {};

    function updateMostClickedEmoji(announcementId) {
        const container = document.querySelector(`.most-clicked[data-announcement-id="${announcementId}"]`);
        const counts = emojiClickCounts[announcementId] || {};

        let maxEmoji = null;
        let maxCount = -1;

        for (const [emoji, count] of Object.entries(counts)) {
            if (count > maxCount) {
                maxCount = count;
                maxEmoji = emoji;
            }
        }

        if (container) {
            if (maxEmoji) {
                container.textContent = `Most Reacted: ${maxEmoji}`;
            } else {
                container.textContent = 'No reactions yet.';
            }
        }
    }

    // Initialize all announcement cards on page load
    document.querySelectorAll('.announcement-card').forEach(card => {
        const id = card.dataset.announcementId;
        updateMostClickedEmoji(id);
    });

    emojiButtons.forEach(button => {
        button.addEventListener('click', function () {
            const announcementId = this.dataset.announcementId;
            const emoji = this.dataset.emoji;

            if (!emojiClickCounts[announcementId]) {
                emojiClickCounts[announcementId] = {};
            }

            const counts = emojiClickCounts[announcementId];
            counts[emoji] = (counts[emoji] || 0) + 1;

            localStorage.setItem('emojiClickCounts', JSON.stringify(emojiClickCounts));
            console.log(`Emoji Click Counts for ${announcementId}:`, emojiClickCounts[announcementId]);

            fetch('/community/react/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'X-CSRFToken': getCookie('csrftoken')
                },
                body: `announcement_id=${announcementId}&emoji=${emoji}`
            })
                .then(res => res.json())
                .then(data => {
                    if (data.status === 'added') {
                        this.classList.add('active');
                    } else if (data.status === 'removed') {
                        this.classList.remove('active');
                    }

                    updateMostClickedEmoji(announcementId);
                })
                .catch(error => console.error('Reaction error:', error));
        });
    });

    function getCookie(name) {
        const cookies = document.cookie.split(';');
        for (let cookie of cookies) {
            cookie = cookie.trim();
            if (cookie.startsWith(name + '=')) {
                return decodeURIComponent(cookie.substring(name.length + 1));
            }
        }
        return null;
    }
});
