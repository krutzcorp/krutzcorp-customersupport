$(document).ready(function () {

    // Takes the drop down selection creates a modal with the ticket type and order number.
    $("#createTicket").click(function (){

        // Grab Type of Ticket and Order Number to create new ticket modal
        var ticketType = $('#ticketType').val();
        var orderID = $('#order').val();
        $(".modal-body #titleForm").val('['+ ticketType + '] Order '+ orderID);
        //Set hidden value for 'replace' boolean
        if(ticketType=="Replace"){
            $(".modal-body #replaceTicket").val("true")
        }else{
            $(".modal-body #replaceTicket").val("false")
        }

        // Get Table DOM element
        var table = $("#newTicketTable")
        // Remove all table rows that may be there already
        table.find("tr:gt(0)").remove();
        // Init the ticket type to new
        $("#status option[value='open']").prop('selected', 'selected').change();

        // Search for items within an order to add to the form
        $.get("/api/orderitem", {'order_id':orderID, 'mocked':true})
            .done(function (data) {
                $.each(data, function (index, item) { // Iterates through a collection
                    var serial_id = item.serialId;
                    var model_id = item.modelId;
                    table.append('<tr><td>'+ serial_id +'</td><td> Model: '+ model_id +'</td><td><input class="order-item-box" serialId='+ serial_id +' type="checkbox"><br></td></tr>');
                  });
            });
     });

    $("#saveTicketChanges").click(function(){
        
        var ticketBar = $("#ticketProgressBar");        
        var ticketBarContainer = $("#ticketProgressContainer");
        ticketBar.css("width","0%");
        ticketBarContainer.css("visibility", "visible");

        // Build payload to post
        serialIds = [];
        $('.order-item-box:checkbox:checked').each(function(){
            serialIds.push(this.serialId);
        });
        payload = {
            'use_mock': true,
            'replace': ($(".modal-body #replaceTicket").val()) == "true",
            'order_id': $('#order').val(),
            'serial_ids': serialIds
        }

        // TODO call the api endpoint
        $.post("/sales/refund", payload, function(res,status){
                ticketBar.animate({
                        width: "100%"
                }, 25, function(){
                    // Change ticket status to pass
                    $("#status option[value='pass']").prop('selected', 'selected').change();
                    // Delay then hide the progress bar
                    setTimeout(function(){ticketBarContainer.css("visibility", "hidden")},750);
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
