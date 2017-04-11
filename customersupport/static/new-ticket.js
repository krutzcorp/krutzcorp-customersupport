$(document).ready(function () {

    // Takes the drop down selection creates a modal with the ticket type and order number.
    $("#createTicket").click(function (){

        // Grab Type of Ticket and Order Number to create new ticket modal
        var ticketType = $('#ticketType').val();
        var orderID = $('#order').val();
        $(".modal-body #titleForm").val('['+ ticketType + '] Order '+ orderID);
        //var getInfo= [ticketType, orderID];

        // Search for items within an order to add to the form
        $.get("/api/ordersearch", {'order_id':orderID})
            .done(function (data) {
                $("#matchingReturnOrders").find("option").remove();
                $.each(data, function (index, item) { // Iterates through a collection
                    $("#matchingReturnOrders").append( // Append an object to the inside of the select box
                        $("<option></option>")
                            .text(`${item.serialId}, ${item.status}`)
                            .val(item.serialId)
                    );
                });
            });
     });



});
