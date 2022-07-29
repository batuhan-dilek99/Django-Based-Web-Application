def getSingleTicket(request, pk):
    ticket = TicketDataTable.objects.get(id = pk)
    
    ticket.status_flag = Status.get(2)
    ticket.save()

    operation = -1
    if request.method == 'POST':
        operation = request.POST.get("op_select")
        print()
        print(operation)
        print()
        
        if(operation == "1"):
            ticket.operation_flag = int(operation)
            ticket.status_flag = 1
            ticket.save() 
            return redirect('http://127.0.0.1:8000/tickets/')
        elif(operation == "2"):
            ticket.operation_flag = int(operation)
            ticket.status_flag = 1
            ticket.save()
            return redirect('http://127.0.0.1:8000/tickets/')
        elif(operation == "0"):
            ticket.operation_flag = int(operation)
            ticket.status_flag = 0
            ticket.save()
            return redirect('http://127.0.0.1:8000/tickets/')
        else:
            ticket.operation_flag = int(operation)
            ticket.status_flag = 0
            ticket.save()
            return redirect('http://127.0.0.1:8000/tickets/')

    context = {
        'ticket' : ticket
    }
    return render(request, 'home/individualTicket.html', context)
