/* JavaScript function for checkoutbook/checkout.html*/

function checkout() {
    const checkoutDataElement = document.getElementById('my-data');
    const checkoutUrl = checkoutDataElement.getAttribute('data-checkout-url');

    var alamatInput = document.querySelector('#alamat');
    var metodePembayaranInput = document.querySelector('input[name="metode_pembayaran"]:checked');

    if (!alamatInput.value) {
        alert("Alamat harus diisi.");
        return false;
    }

    if (!metodePembayaranInput) {
        alert("Pilih metode pembayaran.");
        return false;
    }

    fetch(checkoutUrl, {
        method: "POST",
        body: new FormData(document.querySelector('#checkout-form'))
    }).then(response => {
        successful();
    }).catch(error => {
        console.error('Error:', error);
    });

    document.getElementById('checkout-form').reset();
    return false;
}

document.getElementById("button_checkout").onclick = checkout;

function successful() {
    window.location.href = `/buybooks/cart/`;
}