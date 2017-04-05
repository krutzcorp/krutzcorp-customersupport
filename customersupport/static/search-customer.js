$(document).ready(function () {
    $("#searchCustomerButton").click(function () {
        $.get("/api/customer/search", $('#searchCustomerForm').serializeArray())
            .done(function (data) {
                $("#matchingCustomers").find("option").remove(); // Remove all <option> child tags.
                $.each(data, function (index, item) { // Iterates through a collection
                    $("#matchingCustomers").append( // Append an object to the inside of the select box
                        $("<option></option>") // Yes you can do this.
                            .text(`${item.first_name} ${item.last_name}, ${item.email}, ${item.phone}`)
                            .val(item.id)
                    );
                });
            });
    });

    $("#selectCustomer").click(function () {
        $("#customer").val($("#matchingCustomers").val());
        $('#searchCustomerModal').modal('hide')
    });
});
