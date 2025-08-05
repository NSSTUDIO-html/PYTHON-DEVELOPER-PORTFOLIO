from django.shortcuts import render, get_object_or_404
from .models import Quiz, Question, Choice

def quiz_list(request):
    quizzes = Quiz.objects.all()
    return render(request, 'quiz/quiz_list.html', {'quizzes': quizzes})

def quiz_detail(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz.question_set.all()

    if request.method == 'POST':
        score = 0
        for question in questions:
            selected = request.POST.get(str(question.id))
            if selected:
                choice = Choice.objects.get(id=selected)
                if choice.is_correct:
                    score += 1
        return render(request, 'quiz/result.html', {'score': score, 'total': questions.count()})

    return render(request, 'quiz/quiz_detail.html', {'quiz': quiz, 'questions': questions})
