from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def calculator(request, operation, num1, num2):
    result = None
    error = None
    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            error = "Division by zero error"
        else:
            result = num1 / num2
    else:
        error = "Invalid operation"

    return JsonResponse({'operation': operation, 'num1': num1, 'num2': num2, 'result': result, 'error': error})

def calculator_form(request):
    result = None
    error = None
    num1 = num2 = operation = None

    if request.method == 'POST':
        try:
            num1 = int(request.POST.get('num1'))
            num2 = int(request.POST.get('num2'))
            operation = request.POST.get('operation')
            if operation == 'add':
                result = num1 + num2
            elif operation == 'subtract':
                result = num1 - num2
            elif operation == 'multiply':
                result = num1 * num2
            elif operation == 'divide':
                if num2 == 0:
                    error = "Division by zero error"
                else:
                    result = num1 / num2
            else:
                error = "Invalid operation"
        except Exception as e:
            error = str(e)

    return render(request, 'calculator_form.html', {
        'result': result,
        'error': error,
        'num1': num1,
        'num2': num2,
        'operation': operation,
    })
