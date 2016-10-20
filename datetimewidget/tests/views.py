
from django.shortcuts import render

from datetimewidget.tests.form import testFormBootstrap3, testFormBootstrap2

# def dateTimeView(request):
# 
#     if request.method == 'POST': # If the form has been submitted...
# 
#         form = testModelForm(request.POST) # A form bound to the POST data
#         if form.is_valid(): # All validation rules pass
#             new_event = form.save()
#             form = testModelForm(instance=new_event)
#             return render(request, 'example/example.html', {
#                 'datetime': new_event,
#                 'form': form,
#             })
#     else:
#         if request.GET.get('id', None):
#             inst = testModel.objects.get(id=request.GET.get('id', None))
#             form = testModelForm(instance=inst)
#         else:
#             form = testModelForm()
# 
#     return render(request, 'example/example.html', {
#         'form': form,
#     })


def dateTimeViewBootstrap3(request):

    if request.method == 'POST': # If the form has been submitted...
        form = testFormBootstrap3(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            return render(request, 'example/example.html', {
                'form': form,
                'bootstrap': 3,
                'success': True,
            })
    else:
        if request.GET.get('id', None):
            inst = testFormBootstrap3.objects.get(id=request.GET.get('id', None))
            form = testFormBootstrap3(instance=inst)
        else:
            form = testFormBootstrap3()

    return render(request, 'example/example.html', {
        'form': form,
        'bootstrap': 3,
    })


def dateTimeViewBootstrap2(request):

    if request.method == 'POST': # If the form has been submitted...
        form = testFormBootstrap2(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            return render(request, 'example/example.html', {
                'form': form,
                'bootstrap': 2,
                'success': True,
            })
    else:
        if request.GET.get('id', None):
            inst = testFormBootstrap2.objects.get(id=request.GET.get('id', None))
            form = testFormBootstrap2(instance=inst)
        else:
            form = testFormBootstrap2()

    return render(request, 'example/example.html', {
        'form': form,
        'bootstrap': 2,
    })
