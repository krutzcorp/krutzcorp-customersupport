$(document).ready(function(){
    
    $("#listTicketsButton").click(function(){
        $.get("api/ticket/customer",{customer_id:$("#customer").val()})
            .done(function (data) {
                $("#listTicketSelection").find("option").remove();
                $.each(data, function(index, item){
                    $("#listTicketSelection").append(
                        $('<option></option>')
                            .text(`id: ${item.id} customer_id: ${item.customer_id}  date: ${item.date_opened} issue: ${item.issue} status: ${item.current_status}`)
                            .val(item.id)
                    );                    
                });
            });
    });

    $("#selectTicket").click(function(){
        $("#ticketId").val($("#listTicketSelection").val());
        $("#listTicketModal").modal("hide");
    });

});
