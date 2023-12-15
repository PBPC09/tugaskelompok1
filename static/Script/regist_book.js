const dataUrls = document.getElementById("data-urls");
const addBookAjaxUrl = dataUrls.getAttribute("data-add-book-ajax-url");
const deleteBookAjaxUrl = dataUrls.getAttribute("data-delete-book-ajax-url");
const logoutUrl = dataUrls.getAttribute("data-logout-url");
const getBookJsonUrl = dataUrls.getAttribute("data-get-book-json-url");

$(document).ready(function() {
    $(".show-detail-text").click(function() {
        var bookId = $(this).data("book-id");
        $(".book-details[data-book-id='" + bookId + "']").slideToggle();
    });

    $(".add-to-cart-button").click(function() {
        var bookId = $(this).data("book-id");
        $("#id_book_id").val(bookId);
        $("#cartModal").modal("show");
    });
});

async function getBooks() {
    const ratingFilter = document.getElementById("ratingFilter").value;
    const url = `${getBookJsonUrl}?rating_filter=${ratingFilter}`;
    return fetch(url).then((res) => res.json());
}

async function refreshBooks() {
    const container = document.getElementById("product_table");
    container.innerHTML = "";

    const books = await getBooks();

    books.forEach((book) => {
        const card = `
            <div class="col-md-4 mb-4">
                <div class="accordion" id="accordionExample-${book.pk}">
                    <div class="book-card">
                        <div class="accordion-item">
                            <h3 class="accordion-header">
                                <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapse${book.pk}" aria-expanded="false" aria-controls="collapse${book.pk}">
                                    ${book.fields.title}
                                </button>
                            </h3>
                            <div id="collapse${book.pk}" class="accordion-collapse collapse" data-bs-parent="#accordionExample-${book.pk}">
                                <div class="accordion-body">
                                    <strong>Author:</strong> ${book.fields.author} <br/>
                                    <strong>Rating:</strong> ${book.fields.rating} <br/>
                                    <strong>Voters:</strong> ${book.fields.voters} <br/>
                                    <strong>Price:</strong> ${book.fields.price} ${book.fields.currency} <br/>
                                    <strong>Publisher:</strong> ${book.fields.publisher} <br/>
                                    <strong>Page Count:</strong> ${book.fields.page_count} <br/>
                                    <strong>Genres:</strong> ${book.fields.genres} <br/>
                                    <div class="float-end mb-2">
                                        <button class="btn btn-info btn-sm mt-2" data-description="${book.fields.description.replace(/"/g, '&quot;')}" onclick="event.stopPropagation(); showBookDescriptionFromData(this);">Details</button>
                                        <button class="btn btn-danger btn-sm mt-2 ml-2" onclick="event.stopPropagation(); removeItem(${book.pk})">Delete</button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        `;

        container.innerHTML += card;
    });
}

function addBook() {
    fetch(addBookAjaxUrl, {
        method: "POST",
        body: new FormData(document.querySelector('#form'))
    }).then(refreshBooks)

    document.getElementById("form").reset()
    return false
}

// Implementasi AJAX DELETE
function removeItem(bookId) {
    if (confirm("Are you sure you want to delete this item?")) {
        fetch(`${deleteBookAjaxUrl}${bookId}/`, {
            method: "DELETE",
        }).then(refreshBooks)
    }
    return false;
}

function showBookDescriptionFromData(buttonElement) {
    const description = buttonElement.getAttribute("data-description");
    document.getElementById("bookDescriptionContent").innerText = description;
    const bookDetailModal = new bootstrap.Modal(document.getElementById('bookDetailModal'));
    bookDetailModal.show();
}

refreshBooks();
document.getElementById("button_add").onclick = addBook
document.getElementById("ratingFilter").addEventListener("change", refreshBooks);
// document.getElementById("logout-button").addEventListener("click", function() {
//     window.location.href = logoutUrl;
// });