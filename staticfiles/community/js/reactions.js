document.addEventListener('DOMContentLoaded', function() {
    const emojiButtons = document.querySelectorAll('.emoji-btn');

    emojiButtons.forEach(button => {
        button.addEventListener('click', function() {
            console.log('Emoji button clicked!');
            const announcementId = this.dataset.announcementId;
            const emoji = this.dataset.emoji;
            const btn = this;

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
                    btn.classList.add('active');
                } else if (data.status === 'removed') {
                    btn.classList.remove('active');
                } else {
                    alert('Error: ' + data.message);
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
