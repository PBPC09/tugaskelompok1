const dataUrls = document.getElementById("data-urls");
const markNotificationReadUrl = dataUrls.getAttribute("data-mark-notification-read-url");
const deleteNotificationUrl = dataUrls.getAttribute("data-delete-notification-url");

const readNotifButtons = document.querySelectorAll('.btn-info');
  readNotifButtons.forEach((button) => {
      button.addEventListener('click', (event) => {
          const notifId = event.target.dataset.notifId;
          markNotificationAsRead(notifId);
      });
  });

// Fungsi untuk menandai notifikasi sebagai sudah dibaca
function markNotificationAsRead(notifId) {
    fetch(markNotificationReadUrl + notifId + "/", {
        method: 'GET',
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === "success") {
            const notifElement = document.querySelector(`[data-notif-id="${notifId}"]`).parentNode.parentNode;
            notifElement.classList.remove('border-primary');
            updateNotifCount();
        } else {
            console.error('Failed to mark notification as read');
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

// Fungsi untuk menghapus notifikasi
function deleteNotification(notifId) {
    fetch(deleteNotificationUrl + notifId + "/", {
        method: 'DELETE',
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === "success") {
            const notifElement = document.querySelector(`[data-notif-id="${notifId}"]`).parentNode.parentNode;
            notifElement.remove();
            updateNotifCount();
        } else {
            console.error('Failed to delete notification');
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

// Fungsi untuk menandai semua notifikasi sebagai sudah dibaca
function markAllAsRead() {
    const unreadNotifIds = Array.from(document.querySelectorAll('.border-primary .btn-info'))
                                .map(button => button.dataset.notifId);
    
    const promises = unreadNotifIds.map(notifId => {
        return fetch(markNotificationReadUrl + notifId + "/", {
            method: 'GET',
        });
    });

    Promise.all(promises)
    .then(responses => {
        responses.forEach(response => {
            if (response.ok) {
                const notifId = response.url.split('/').slice(-2, -1)[0];
                const notifElement = document.querySelector(`[data-notif-id="${notifId}"]`).parentNode.parentNode;
                notifElement.classList.remove('border-primary');
            }
        });
        updateNotifCount();
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

// Fungsi untuk memperbarui jumlah notifikasi yang belum dibaca
function updateNotifCount() {
    const unreadNotifCount = document.querySelectorAll('.border-primary').length;
    const unReadMessagesCount = document.getElementById('num-of-notif');
    if (unreadNotifCount === 0) {
        unReadMessagesCount.innerText = '';
        unReadMessagesCount.style.display = 'none';
    } else {
        unReadMessagesCount.innerText = unreadNotifCount;
        unReadMessagesCount.style.display = 'block';
    }
}

// Event listener untuk tombol 'Read' dan 'Delete'
document.addEventListener("DOMContentLoaded", function() {
    const readNotifButtons = document.querySelectorAll('.btn-info');
    readNotifButtons.forEach((button) => {
        button.addEventListener('click', (event) => {
            const notifId = event.target.dataset.notifId;
            markNotificationAsRead(notifId);
        });
    });

    const deleteButtons = document.querySelectorAll('.delete-notif-btn');
    deleteButtons.forEach((button) => {
        button.addEventListener('click', (event) => {
            const notifId = event.target.dataset.notifId;
            deleteNotification(notifId);
        });
    });

    const markAll = document.getElementById('mark-as-read');
    markAll.addEventListener('click', markAllAsRead);
});