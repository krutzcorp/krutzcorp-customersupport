$(document).ready(function () {

    // When the user searches for a customer, call the API and fill the select box.
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

    // When the user selects a customer, populate the new-call form and close the modal.
    $("#selectCustomer").click(function () {
        $("#customer").val($("#matchingCustomers").val());
        $('#searchCustomerModal').modal('hide')
    });
});
