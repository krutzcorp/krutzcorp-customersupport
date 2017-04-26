$(document).ready(function () {


    $("#searchOrderButton").click(function () {
        $.get("/api/order/search", $('#searchOrderForm').serializeArray())
            .done(function (data) {
                $("#matchingOrders").find("option").remove();
                $.each(data, function (index, item) { // Iterates through a collection
                    $("#matchingOrders").append( // Append an object to the inside of the select box
                        $("<option></option>")
                            .text(`Order Id: ${item.id}, Order Date: ${item.orderDate.substring(0,10)}, Phones Purchased: `)
                            .val(item.id))
                            $.each(item.items, function (index, phone) {
                            $("<option></option>")
                            .text(`Model Id: ${phone.modelId}, Refund Deadline: ${phone.refundDeadline} Replace Deadline: ${phone.replaceDeadline}, Serial Id: ${phone.serialId}`)
                        })
                });
            });
    });

    $("#searchOrderIdButton").click(function () {
        $.get("/api/orderid/search", $('#searchOrderIdForm').serializeArray())
            .done(function (data) {
                $("#matchingOrders").find("option").remove();
                $.each(data, function (index, item) { // Iterates through a collection
                    $("#matchingOrders").append( // Append an object to the inside of the select box
                        $("<option></option>")
                            .text(`Order Id: ${item.id}, Order Date: ${item.orderDate.substring(0,10)}, Phones Purchased: `)
                            .val(item.id),
                        $.each(item.items, function (index, phone) {
                            $("<option></option>")
                            .text(`Model Id: ${phone.modelId}, Refund Deadline: ${phone.refundDeadline} Replace Deadline: ${phone.replaceDeadline}, Serial Id: ${phone.serialId}`)
                        })
                    );
                });
            });

    });

    // When the user selects a order, populate the new-call form and close the modal.
    $("#selectOrder").click(function () {
        $("#order").val($("#matchingOrders").val());
        $('#searchOrderModal').modal('hide')
    });
});