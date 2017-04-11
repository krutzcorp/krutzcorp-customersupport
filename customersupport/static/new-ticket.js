$(document).ready(function () {

    // Takes the drop down selection creates a modal with the ticket type and order number.
    $("#createTicket").click(function (){

        // Grab Type of Ticket and Order Number to create new ticket modal
        var e = document.getElementById("ticketType");
        var ticketType = e.options[e.selectedIndex].value;
        var orderID = $('#order').val();
        $(".modal-body #titleForm").val('['+ ticketType + '] Order '+ orderID);
        var getInfo= [ticketType, OrderID];

        // Search for items within an order to add to the form
        $.get("/api/orderinfo/real", $('#order').val())
            .done(function (data) {
                $("#matchingReturnOrders").find("option").remove();
                $.each(data, function (index, item) { // Iterates through a collection of
                    $("#matchingReturnOrders").append( // Append an object to the inside of the select box
                        $("<option></option>")
                            .text(`${item.id}, ${item.status}`)
                            .val(item.id)
                    );
                });
            });
     });



});
