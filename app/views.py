from django.shortcuts import render
from app.models import Question, Answer
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

user_info = {
    'login': 'myLog123',
    'email': 'my2@email.ru',
    'nickname': 'Zabelina'
}
user = True


def pagination(object_list, request, per_page=10):
    p = request.GET.get('page')
    paginator = Paginator(object_list, per_page)

    try:
        content = paginator.page(p)
    except PageNotAnInteger:
        content = paginator.page(1)
    except EmptyPage:
        content = paginator.page(paginator.num_pages)

    return content


def new_questions(request):
    return render(request, "hot_questions.html", {
        'questions': pagination(Question.objects.new().prefetch_related('likequestion_set'), request),
        'user': user,
        'style': True,
        'type': 'new'
    })


def hot_questions(request):
    return render(request, "hot_questions.html", {
        'questions': pagination(Question.objects.hot().prefetch_related('likequestion_set'), request),
        'user': user,
        'style': True,
        'type': 'hot'
    })


def tag_questions(request, tag):
    return render(request, "hot_questions.html", {
        'questions': pagination(Question.objects.tag(tag), request),
        'user': user,
        'style': True
    })


def author_questions(request, author):
    return render(request, "hot_questions.html", {
        'questions': pagination(Question.objects.author(author).prefetch_related('likequestion_set'), request),
        'user': user,
        'style': True
    })


def add_question(request):
    return render(request, "add_question.html", {
        'user': user
    })


def question_answer(request, pk):
    return render(request, "question_answer.html", {
        'questions': Question.objects.one_question(pk),
        'user': user,
        'style': False,
        'comments': pagination(Answer.objects.answers(pk), request, per_page=3)
    })


def settings_page(request):
    return render(request, "settings_page.html", {
        'user': True,
        'user_info': user_info
    })


def login_page(request):
    return render(request, "login_page.html", {
        'user': False
    })


def signup_page(request):
    return render(request, "signup_page.html", {
        'user': False
    })
