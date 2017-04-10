/**
 * Created by mxl75 on 4/2/2017.
 */

$(document).ready(function () {

    $("#searchOrderButton").click(function () {
        $.get("/api/order/search", $('#searchOrderForm').serializeArray())
            .done(function (data) {
                $("#matchingOrders").find("option").remove();
                $.each(data, function (index, item) { // Iterates through a collection
                    $("#matchingOrders").append( // Append an object to the inside of the select box
                        $("<option></option>")
                            .text(`${item.first_name} ${item.last_name}, ${item.zipcode}, ${item.state}, ${item.street_address}, ${item.customer_id}`)
                            .val(item.id)
                    );
                });
            });
    })

    // When the user selects a order, populate the new-call form and close the modal.
    $("#selectOrder").click(function () {
        $("#order").val($("#matchingOrders").val());
        $('#searchOrderModal').modal('hide')
    });
});