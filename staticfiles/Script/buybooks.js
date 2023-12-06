/* JavaScript function for buybooks/buybooks.html*/
const bookDataElement = document.getElementById('my-data');
const bookUrl = bookDataElement.getAttribute('data-book-url');
const bookLtUrl = bookDataElement.getAttribute('data-book-lt-url');
const bookGteUrl = bookDataElement.getAttribute('data-book-gte-url');

async function getBookAll() {
    return fetch(bookUrl).then((res) => res.json())
}
async function getBookLt() {
    return fetch(bookLtUrl).then((res) => res.json())
}
async function getBookGte() {
    return fetch(bookGteUrl).then((res) => res.json())
}

var dropdown = document.getElementById("myDropdown");

dropdown.addEventListener("change", function() {
    var selectedOption = dropdown.value;

    // Lakukan sesuatu berdasarkan nilai yang dipilih
    if (selectedOption === "all") {
        show_book(getBookAll());
    } else if (selectedOption === "lt") {
        show_book(getBookLt());
    } else if (selectedOption === "gte") {
        show_book(getBookGte());
    }
});

async function show_book(getBook) {
    const items = await getBook
    let htmlString = `<div class="row card-container align-items-stretch">
        `
    items.forEach((item) => {
        console.log(item)
        htmlString += 
        `<div class="col-md-4 mb-4">
            <div class="accordion" id="accordionExample-${item.pk}">
                <div class="book-card">
                    <div class="accordion-item">
                        <h2 class="accordion-header">
                            <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapse${item.pk}" aria-expanded="false" aria-controls="collapse${item.pk}">
                                ${item.fields.title}
                            </button>
                        </h2>
                        <div id="collapse${item.pk}" class="accordion-collapse collapse" data-bs-parent="#accordionExample-${item.pk}">
                            <div class="accordion-body">
                                <p class="card-text">
                                    <strong>Genres:</strong> ${item.fields.genres}
                                    <strong>Rating:</strong> ${item.fields.rating}
                                    <strong>Voters:</strong> ${item.fields.voters}
                                    <strong>Page Count:</strong> ${item.fields.page_count}
                                </p>
                                <p class="card-text"><strong>Publisher:</strong> ${item.fields.publisher}</p>
                                <button class="btn btn-primary add-to-cart-button" data-book-id="${item.pk}">Add to Cart</button>        
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>`
    })
    document.getElementById("card-book-here").innerHTML = htmlString
}

show_book(getBookAll())

var bookId
$('body').on('click', '.add-to-cart-button', function() {
    bookId = $(this).data("book-id");
    $("#id_book_id").val(bookId);
    $("#cartModal").modal("show");
});

function addToCart() {
    fetch(`/buybooks/create/${bookId}/`, {
        method: "POST",
        headers: {
            'x-csrf-token' : document.getElementsByName("csrfmiddlewaretoken")[0].value },
        body: new FormData(document.querySelector('#form'))
    })

    document.getElementById("form").reset()
    $('#cartModal').modal('hide');
    return false
}

document.getElementById("button_co").onclick = addToCart

$(document).ready(function(){
    $(".show-detail-text").click(function(){
        var bookId = $(this).data("book-id");
        $(".book-details[data-book-id='" + bookId + "']").slideToggle();
    });
    $("#to_cart").click(function() {
            window.location.href = `cart/`;
    });
});