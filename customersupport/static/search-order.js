$(document).ready(function () {


    $("#searchOrderButton").click(function () {
        $.get("/api/order/search", $('#searchOrderForm').serializeArray())
            .done(function (data) {
                $("#matchingOrders").find("option").remove();
                $.each(data, function (index, item) { // Iterates through a collection
                    var phones = [];
                    $.each(item.items, function(index, items) {
                   phones.push(`Model Id: ${items.modelId}, Refund Deadline: ${items.refundDeadline.substring(0,10)} Replace Deadline: ${items.replaceDeadline.substring(0,10)}, Serial Id: ${items.serialId} `);
                    });
                    $("#matchingOrders").append( // Append an object to the inside of the select box
                        $("<option></option>")
                        .text(`Order Id: ${item.id}, Order Date: ${item.orderDate.substring(0,10)}, Phones Purchased: ${phones}`)
                        .val(item.id)
                    )

                });
                });
    });

    $("#searchOrderIdButton").click(function () {
        $.get("/api/orderid/search", $('#searchOrderIdForm').serializeArray())
            .done(function (data) {
                $("#matchingOrders").find("option").remove();
                $.each(data, function (index, item) { // Iterates through a collection
                    var phones = [];
                    $.each(item.items, function(index, items) {
                   phones.push(`Model Id: ${items.modelId}, Refund Deadline: ${items.refundDeadline.substring(0,10)} Replace Deadline: ${items.replaceDeadline.substring(0,10)}, Serial Id: ${items.serialId} `);
                    });
                    $("#matchingOrders").append( // Append an object to the inside of the select box
                        $("<option></option>")
                        .text(`Order Id: ${item.id}, Order Date: ${item.orderDate.substring(0,10)}, Phones Purchased: ${phones}`)
                        .val(item.id)
                    )

                });
                });
            });

    // When the user selects a order, populate the new-call form and close the modal.
    $("#selectOrder").click(function () {
        $("#order").val($("#matchingOrders").val());
        $('#searchOrderModal').modal('hide')
    });
});