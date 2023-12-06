$(document).ready(function() {
    // Attach click event to checkboxes
    $(document).on('click', '.form-check-input', function() {
        var bookId = $(this).data("book-id");
        console.log("Checkbox for item " + bookId + " clicked.");

        // AJAX call to the Django backend
        $.ajax({
            url: `/buybooks/selected/${bookId}/`,
            type: 'GET',
            success: function(response) {
                console.log("Processed item " + bookId);
                // You can add code here to update the UI based on the response
            },
            error: function(error) {
                console.log("Error processing item " + bookId);
            }
        });
    });

    // Button click event for checkout
    $("#button_co").click(function() {
        var checkedInputs = $(".form-check-input:checked");
        if(checkedInputs.length == 0){
            alert("Anda tidak men-checkout apapun!");
        } else {
            window.location.href = `/checkoutbook/`;
        }
    });
});
