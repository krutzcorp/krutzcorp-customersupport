function populateMatchingOrders(data) {
    $("#matchingOrders").find("option").remove();
    $.each(data, function (index, item) { // Iterates through a collection
        let phones = [];
        $.each(item.items, function (index, items) {
            phones.push(`Model ID: ${items.modelId}, Refund Deadline: ${items.refundDeadline.substring(0, 10)} Replace Deadline: ${items.replaceDeadline.substring(0, 10)}, Serial ID: ${items.serialId}`);
        });
        $("#matchingOrders").append( // Append an object to the inside of the select box
            $("<option></option>")
                .text(`Order ID: ${item.id}, Order Date: ${item.orderDate.substring(0, 10)}, Phones Purchased: ${phones.join(", ")}`)
                .val(item.id)
        )
    });
}

$(document).ready(function () {

    $("#searchOrderButton").click(function () {
        $.get("/api/order/search", $('#searchOrderForm').serializeArray())
            .done(populateMatchingOrders);
    });

    $("#searchOrderIdButton").click(function () {
        $.get("/api/orderid/search", $('#searchOrderIdForm').serializeArray())
            .done(populateMatchingOrders);
    });

    // When the user selects a order, populate the new-call form and close the modal.
    $("#selectOrder").click(function () {
        $("#order").val($("#matchingOrders").val()).change();
        $('#searchOrderModal').modal('hide')
    });
});
