$(document).ready(function() {
    $(".show-detail-text").click(function(){
        var bookId = $(this).data("book-id");
        $(".book-details[data-book-id='" + bookId + "']").slideToggle();
    });

    document.querySelectorAll('.add-to-wishlist-button').forEach(function(element) {
        element.addEventListener('click', function() {
            var bookId = this.getAttribute('data-book-id');
            document.getElementById('id_book_id').value = bookId;
            $('#wishlistModal').modal('show'); 
        });
    });

    document.getElementById('wishlist-form').addEventListener('submit', function(event) {
    event.preventDefault();
    var bookId = document.getElementById('id_book_id').value;
    var url = this.getAttribute('action');
    var data = new FormData(this);
    fetch(url, {
        method: 'POST',
        body: data
    }).then(function(response) {
        return response.json();
    }).then(function(data) {
        var toastElement = document.getElementById('toastMessage');
        var toastBodyElement = toastElement.querySelector('.toast-body');
        if (data.status === 'success') {
            toastBodyElement.textContent = data.message; 
            $('#wishlistModal').modal('hide');
            document.getElementById('wishlist-form').reset();
        } else {
            $('#wishlistModal').modal('hide');
            toastBodyElement.textContent = data.message; 
            document.getElementById('wishlist-form').reset();
        }

        $(toastElement).toast({delay: 5000});
        $(toastElement).toast('show');
    }).catch(function(error) {
        console.error('Error:', error);
    });
});

function filterBooks() {
    var searchInput = document.getElementById('searchInput').value;
    var ratingFilter = document.getElementById('ratingFilter').value;
    var url = "{% url 'wishlist:get_books' %}";

    fetch(url + '?search=' + searchInput + '&rating=' + ratingFilter)
        .then(response => response.json())
        .then(data => {
            var bookCardsContainer = document.querySelector('.card-container');
            bookCardsContainer.innerHTML = '';
            data.forEach(book => {
                var bookCard = document.createElement('div');
                bookCard.className = 'book-card';
                bookCard.innerHTML = `
                    <h5 class="card-title">${book.title}</h5>
                    <p class="show-detail-text" data-book-id="${book.id}">Show Detail</p>
                    <div class="book-details" data-book-id="${book.id}">
                        <p class="card-text"><strong>Author:</strong> ${book.author}</p>
                        <p class="card-text"><strong>Rating:</strong> ${book.rating}</p>
                        <p class="card-text"><strong>Price:</strong> ${book.price} ${book.currency}</p>
                        <button class="btn btn-primary add-to-wishlist-button" data-book-id="${book.id}">Add to Wishlist</button>
                    </div>
                `;
                bookCardsContainer.appendChild(bookCard);
            });
        })
        .catch(error => console.error('Error:', error));
    }
});