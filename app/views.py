from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
import random


def tags():
    tag_array = []
    for i in range(random.randint(1, 10)):
        tag_array.append('tag' + str(i))
    return tag_array


questions = [
    {
        'id': idx,
        'member': 'Member',
        'time': '26.12.2019 13:34',
        'title': f'title {idx}',
        'text': 'text so much texttexch texttext text s much texttext text so much texttext ttext so much texttext text so much texttext text so much texttext text so much texttext text so much te much texttext text so much texttext text so much texttext text so much te much texttext text so much texttext text so much texttext text so much te much texttext text so much texttext text so much texttext text so much te much texttext text so much texttext text so much texttext text so much te much texttext text so much texttext text so much texttext text so much te much texttext text so much texttext text so much texttext text so much te much texttext text so much texttext text so much texttext text so much te much texttext text so much texttext text so much texttext text so much t much texttext text so much texttext text so much texttext text so much te much texttext text so much texttext text so much texttext text so much te much texttext text so much texttext text so much texttext text so much te much texttext text so much texttext text so much texttext text so much te much texttext text so much texttext text so much texttext text so much te much texttext text so much texttext text so much texttext text so much te much texttext text so much texttext text so much texttext text so much te much texttext text so much texttext text so much texttext text so much te much texttext text so much texttext text so much texttext text so much te much texttext text so much texttext text so much texttext text so much texttext text so much texttext text so much texttext ttext so much texttext text so much texttext text so much texttext text so much texttext text so much te much texttext text so much texttext text so much texttext text so much te much texttext text so much texttext text so much texttext text so much te much texttext text so much texttext text so much texttext text so much te much texttext text so much texttext text so much texttext text so much te much texttext text so much texttext text so muchuch texttext  vv for text so much texttext text so much texttexttext so much texttext text so much texttext vv  vv',
        'tags': tags()
    } for idx in range(10)
]
best_members = ['Tom', 'Leila', 'Mr. Freedom', 'ClJack']
tags = ['tag1', 'tag2', 'tag3', 'tag4', 'tag5', 'tag6', 'tag7', 'tag8', 'tag9']

comments = [
    {
        'idq': idx,
        'comment_info': [
            {
            'time': '27.10.20 17:52',
            'member' : 'member',
            'text': 'it is comment it is commentit is commentit is commentit is commentit is commentit is commentit is commentit is comment it is comment it is comment'
            } for i in range(idx)
        ]
    } for idx in range(10)
]
user_info = {
    'login': 'myLog123',
    'email': 'my2@email.ru',
    'nickname': 'Zabelina'
}
user = True


def index(request):
    return render(request, "base.html", {})


def new_questions(request):
    return render(request, "hot_questions.html", {
        'questions': questions,
        'members': best_members,
        'tags': tags,
        'user': user,
        'style': True,
        'type': 'new'
    })


def hot_questions(request):
    # contact_list = questions
    # paginator = Paginator(contact_list, 5)  # Show 25 contacts per page
    #
    # page = request.GET.get('page')
    # contacts = paginator.get_page(page)
    return render(request, "hot_questions.html", {
        'questions': questions,
        'members': best_members,
        'tags': tags,
        'user': user,
        'style': True,
        'type': 'hot'
    })


def tag_questions(request, tag):
    result = []
    for q in questions:
        for t in q.get('tags'):
            if t == tag:
                result.append(q)
                break
    return render(request, "hot_questions.html", {
        'questions': result,
        'members': best_members,
        'tags': tags,
        'user': user,
        'style': True
    })


def add_question(request):
    return render(request, "add_question.html", {
        'members': best_members,
        'tags': tags,
        'user': user
    })


def question_answer(request, pk):
    question = questions[pk]
    com = comments[0]
    for i in comments:
        if i.get('idq') == pk:
            com = i
            break
    return render(request, "question_answer.html", {
        'question': question,
        'members': best_members,
        'tags': tags,
        'user': user,
        'style': False,
        'comments': com.get('comment_info')
    })


def settings_page(request):
    return render(request, "settings_page.html", {
        'members': best_members,
        'tags': tags,
        'user': True,
        'user_info': user_info
    })


def login_page(request):
    return render(request, "login_page.html", {
        'members': best_members,
        'tags': tags,
        'user': False
    })


def signup_page(request):
    return render(request, "signup_page.html", {
        'members': best_members,
        'tags': tags,
        'user': False
    })
