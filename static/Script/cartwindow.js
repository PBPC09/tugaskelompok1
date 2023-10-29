$(document).ready(function() {
    $("#button_co").click(function() {
        var checkedInputs = $(".form-check-input:checked");
        if(checkedInputs.length == 0){
            alert("Anda tidak men-checkout apapun!");
        }
        else{
            checkedInputs.each(function() {
                var bookId = $(this).data("book-id");
                console.log("Item " + bookId + " dicentang.");
                window.location.href = `/buybooks/selected/${bookId}/`;
            });
            window.location.href = `/checkoutbook/`;
        }
    });

});