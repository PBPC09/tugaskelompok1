/* JavaScript function for checkoutbook/myorder.html*/
const orderDataElement = document.getElementById('my-data');
const orderUrl = orderDataElement.getAttribute('data-order-url');
const orderCcUrl = orderDataElement.getAttribute('data-order-cc-url');
const orderDcUrl = orderDataElement.getAttribute('data-order-dc-url');
const orderTfUrl = orderDataElement.getAttribute('data-order-tf-url');
const orderEwUrl = orderDataElement.getAttribute('data-order-ew-url');

async function getOrderAll() {
    return fetch(orderUrl).then((res) => res.json())
}
async function getOrderCc() {
    return fetch(orderCcUrl).then((res) => res.json())
}
async function getOrderDc() {
    return fetch(orderDcUrl).then((res) => res.json())
}
async function getOrderTf() {
    return fetch(orderTfUrl).then((res) => res.json())
}
async function getOrderEw() {
    return fetch(orderEwUrl).then((res) => res.json())
}

var dropdown = document.getElementById("myDropdown");
dropdown.addEventListener("change", function() {
    var selectedOption = dropdown.value;

    // Lakukan sesuatu berdasarkan nilai yang dipilih
    if (selectedOption === "all") {
        show_order(getOrderAll());
    } else if (selectedOption === "cc") {
        show_order(getOrderCc());
    } else if (selectedOption === "dc") {
        show_order(getOrderDc());
    } else if (selectedOption === "tf") {
        show_order(getOrderTf());
    } else if (selectedOption === "ew") {
        show_order(getOrderEw());
    }
});

async function show_order(getOrder) {
    const orders = await getOrder
    let htmlString = ""
    orders.forEach((order) => {
        console.log(order)
        htmlString += 
        `<div class="col-md-4 mb-4">
            <div class="card">
                <div class="card-body">
                    <h5 class="card-title">Checkout ${order.pk}</h5>
                    <p class="card-text">Alamat: ${order.fields.alamat}</p>
                    <p class="card-text">Total Harga: SAR ${order.fields.total_price}</p>
                </div>
            </div>
        </div>`   
    })
    document.getElementById("tempatcard").innerHTML = htmlString
}

show_order(getOrderAll())