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

  function markNotificationAsRead(notifId) {
      // Mengirim permintaan ke server untuk menandai notifikasi sebagai 'sudah dibaca'
      fetch(markNotificationReadUrl + notifId + "/", {
          method: 'GET',
      })
      .then(response => {
          if (response.ok) {
              location.reload();  // Refresh halaman setelah memperbarui notifikasi
          } else {
              console.error('Failed to mark notification as read');
          }
      })
      .catch(error => {
          console.error('Error:', error);
      });
  }

  function markAllAsRead() {
    const unreadNotifIds = Array.from(unReadMessages).map(message => message.querySelector('.btn-info').dataset.notifId);
    
    const promises = unreadNotifIds.map(notifId => {
        return fetch(markNotificationReadUrl + notifId + "/", {
            method: 'GET',
        });
    });

    Promise.all(promises)
    .then(responses => {
        const allOk = responses.every(response => response.ok);
        if (allOk) {
            location.reload();
        } else {
            console.error('Some notifications failed to mark as read');
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
  }

  const unReadMessages = document.querySelectorAll('.border-primary')
  const unReadMessagesCount = document.getElementById('num-of-notif')
  const markAll = document.getElementById('mark-as-read')

  updateNotifCount();

  function updateNotifCount() {
    const newUnreadMessages = document.querySelectorAll('.border-primary')
    if (newUnreadMessages.length === 0) {
      unReadMessagesCount.innerText = '';
      unReadMessagesCount.style.display = 'none';
    } else {
      unReadMessagesCount.innerText = newUnreadMessages.length;
      unReadMessagesCount.style.display = 'block';
    }
  }

  unReadMessages.forEach((message) => {
    message.addEventListener('click', () => {
      message.classList.remove('border-primary')
      updateNotifCount();
    })
  })

  markAll.addEventListener('click', markAllAsRead);

  document.addEventListener("DOMContentLoaded", function() {
    const deleteButtons = document.querySelectorAll('.delete-notif-btn');
    
    deleteButtons.forEach((button) => {
        button.addEventListener('click', (event) => {
            const notifId = event.target.dataset.notifId;
            deleteNotification(notifId);
        });
    });
  });

  function deleteNotification(notifId) {
    fetch(deleteNotificationUrl + notifId + "/", {
        method: 'DELETE',
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === "success") {
            location.reload();
        } else {
            console.error('Failed to delete notification');
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
  }