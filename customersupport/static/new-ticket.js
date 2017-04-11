$(document).ready(function () {

    // Takes the drop down selection creates a modal with the ticket type and order number.
    $("#createTicket").click(function (){
        var e = document.getElementById("ticketType");
        var ticketType = e.options[e.selectedIndex].value;
        var orderID = $('#order').val();
        $(".modal-body #titleForm").val('['+ ticketType + '] Order '+ orderID);

     });

});
