from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {})

def pluss(request):
    from random import randint

    num_1 = randint(1,10)
    num_2 = randint(1,10)


    if request.method == 'POST':
        answer = request.POST['answer']
        old_num_1 = request.POST['old_num_1'] 
        old_num_2 = request.POST['old_num_2']


        #errorhandeling if no answer is given and user click the svar-button
        if not answer:
            my_answer = 'Du glemte å svare.....'
            color='warning'
            return render(request, 'pluss.html' , {
            'my_answer':my_answer,
            'answer':answer,
            'num_1': num_1,
            'num_2': num_2,
            'color':color,
            
            })

        correct_answer = int(old_num_1) + int(old_num_2)
        if int(answer) == correct_answer:
            my_answer = 'Correct! ' + old_num_1 + ' + ' + old_num_2 + ' = ' + answer
            color = 'success'
        else:
            my_answer = 'Incorrect.. ' + old_num_1 + ' + ' + old_num_2 + ' = ' + str(correct_answer)
            color = 'danger'



        return render(request, 'pluss.html' , {
            'answer':answer,
            'my_answer': my_answer,
            'num_1': num_1,
            'num_2': num_2,
            'color': color,
            })

    return render(request, 'pluss.html', {

        'num_1': num_1,
        'num_2': num_2,
        })

def minus(request):
    from random import randint

    num_1 = randint(1,10)
    num_2 = randint(1,10)


    if request.method == 'POST':
        answer = request.POST['answer']
        old_num_1 = request.POST['old_num_1'] 
        old_num_2 = request.POST['old_num_2']

        #errorhandeling if no answer is given and user click the svar-button
        if not answer:
            my_answer = 'Du glemte å svare.....'
            color='warning'
            return render(request, 'minus.html' , {
            'my_answer':my_answer,
            'answer':answer,
            'num_1': num_1,
            'num_2': num_2,
            'color':color,
            
            })


        correct_answer = int(old_num_1) - int(old_num_2)
        if int(answer) == correct_answer:
            my_answer = 'Correct! ' + old_num_1 + ' - ' + old_num_2 + ' = ' + answer
            color = 'success'
        else:
            my_answer = 'Incorrect.. ' + old_num_1 + ' - ' + old_num_2 + ' = ' + str(correct_answer)
            color = 'danger'



        return render(request, 'minus.html' , {
            'answer':answer,
            'my_answer': my_answer,
            'num_1': num_1,
            'num_2': num_2,
            'color': color,
            })

    return render(request, 'minus.html', {

        'num_1': num_1,
        'num_2': num_2,
        })

def gange(request):
    from random import randint

    num_1 = randint(1,10)
    num_2 = randint(1,10)


    if request.method == 'POST':
        answer = request.POST['answer']
        old_num_1 = request.POST['old_num_1'] 
        old_num_2 = request.POST['old_num_2']

        #errorhandeling if no answer is given and user click the svar-button
        if not answer:
            my_answer = 'Du glemte å svare.....'
            color='warning'
            return render(request, 'gange.html' , {
            'my_answer':my_answer,
            'answer':answer,
            'num_1': num_1,
            'num_2': num_2,
            'color':color,
            
            })

        correct_answer = int(old_num_1) * int(old_num_2)
        if int(answer) == correct_answer:
            my_answer = 'Correct! ' + old_num_1 + ' * ' + old_num_2 + ' = ' + answer
            color = 'success'
        else:
            my_answer = 'Incorrect.. ' + old_num_1 + ' * ' + old_num_2 + ' = ' + str(correct_answer)
            color = 'danger'



        return render(request, 'gange.html' , {
            'answer':answer,
            'my_answer': my_answer,
            'num_1': num_1,
            'num_2': num_2,
            'color': color,
            })

    return render(request, 'gange.html', {

        'num_1': num_1,
        'num_2': num_2,
        })
    

def dele(request):
    from random import randint

    num_1 = randint(1,10)
    num_2 = randint(1,10)


    if request.method == 'POST':
        answer = request.POST['answer']
        old_num_1 = request.POST['old_num_1'] 
        old_num_2 = request.POST['old_num_2']

        #errorhandeling if no answer is given and user click the svar-button
        if not answer:
            my_answer = 'Du glemte å svare.....'
            color='warning'
            return render(request, 'dele.html' , {
            'my_answer':my_answer,
            'answer':answer,
            'num_1': num_1,
            'num_2': num_2,
            'color':color,
            
            })


        correct_answer = float(old_num_1) / float(old_num_2)
        if float(answer) == correct_answer:
            my_answer = 'Correct! ' + old_num_1 + ' / ' + old_num_2 + ' = ' + answer
            color = 'success'
        else:
            my_answer = 'Incorrect.. ' + old_num_1 + ' / ' + old_num_2 + ' = ' + str(correct_answer)
            color = 'danger'



        return render(request, 'dele.html' , {
            'answer':answer,
            'my_answer': my_answer,
            'num_1': num_1,
            'num_2': num_2,
            'color': color,
            })

    return render(request, 'dele.html', {

        'num_1': num_1,
        'num_2': num_2,
        })
