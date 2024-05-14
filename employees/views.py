from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Employee

# def employee_details(request, pk):
#     try:
#         employee = Employee.objects.get(pk=pk)
#         print(employee)
#     except:
#         raise Http404

def employee_details(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    # print(employee)
    # return HttpResponse(employee)

    context = {
        'employee': employee
    }
    return render(request, "employee_details.html", context)
