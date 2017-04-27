$(document).ready(function () {

    // Takes the drop down selection creates a modal with the ticket type and order number.
    $("#createTicket").click(function (){

        // Grab Type of Ticket and Order Number to create new ticket modal
        var ticketType = $('#ticketType').val();
        var orderID = $('#order').val();
        $(".modal-body #titleForm").val('['+ ticketType + '] Order '+ orderID);
        //var getInfo= [ticketType, orderID];

        // Get Table DOM element
        var table = $("#newTicketTable")
        // Remove all table rows that may be there already
        table.find("tr:gt(0)").remove();
        // Init the ticket type to new
        $("#status option[value='open']").prop('selected', 'selected').change();

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

    $("#saveTicketChanges").click(function(){
        var ticketBar = $("#ticketProgress");
        ticketBar.css("width","0%");
        ticketBar.css("visibility", "visible");
        ticketBar.animate({
            width: "20%"
        }, 500);
        // TODO call the api endpoint
        $.post("/sales/refund",{'use_mock':true}, function(res,status){
            ticketBar.animate({
                    width: "100%"
            }, 2500);
            // Change ticket status to pass
            $("#status option[value='pass']").prop('selected', 'selected').change();
            ticketBar.css("visibility", "hidden");
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
