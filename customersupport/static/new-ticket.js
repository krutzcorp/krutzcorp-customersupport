$(document).ready(function () {

    // Takes the drop down selection creates a modal with the ticket type and order number.
    $("#createTicket").click(function (){

        // Grab Type of Ticket and Order Number to create new ticket modal
        var ticketType = $('#ticketType').val();
        var orderID = $('#order').val();
        $(".modal-body #titleForm").val('['+ ticketType + '] Order '+ orderID);
        //var getInfo= [ticketType, orderID];

        // Create Table
        var table = $("#newTicketTable")

        // Search for items within an order to add to the form
        $.get("/api/orderitem", {'order_id':orderID})
            .done(function (data) {
                $.each(data, function (index, item) { // Iterates through a collection
                    var serial_id = item.serialId;
                    var model_id = item.modelId;
                    table.append('<tr><td>'+ serial_id +'</td><td> Model: '+ model_id +'</td><td><input type="checkbox"><br></td><td><input type="checkbox"><br></td></tr>');
                  });
            });
     });

     //Hook up a change listener to see if the new tickets button should be active
    $(document.body).on('change','#order',function(){
        if(!$(this).val()){
            $("#createTicket").prop('disabled',true);
        } else {
            $("#createTicket").prop('disabled',false);
        }
    });





});
