$(document).ready(function(){
    
    $("#listTicketsButton").click(function(){
        $.get("/api/ticket",{customer_id:$("#customer").val()})
            .done(function (data) {
                $("#listTicketSelection").find("option").remove();
                $.each(data, function(index, item){
                    $("#listTicketSelection").append(
                        $('<option></option>')
                            .text(`ID: ${item.id} Customer: ${item.customer_id}  Date: ${item.date_opened} Type: ${item.ticket_type} Status: ${item.current_status}`)
                            .val(item.id)
                    );                    
                });
            });
    });

    $("#selectTicket").click(function(){
        $("#ticketId").val($("#listTicketSelection").val());
        $("#listTicketModal").modal("hide");
    });

    //Hook up a change listener to see if the list-tickets button should be active
    $(document.body).on('change','#customer',function(){
        if(!$(this).val()){
            $("#listTicketsButton").prop('disabled',true);
        } else {
            $("#listTicketsButton").prop('disabled',false);
        }
    });

});
