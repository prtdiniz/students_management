from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from app.models import Course, Session_Year

@login_required(login_url='/')
def HOME(request):
    return render(request,'Hod/home.html')

@login_required(login_url='/')
def ADD_STUDENT(request):
    course = Course.objects.all()
    session_year = Session_Year.objects.all()

    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        course_id = request.POST.get('course_id')
        session_year_id = request.POST.get('session_year_id')

        if CustomUser.objects.filter(email=email).exists:
            messages.warning(request,'Email já existe no sistema')
            return redirect('add_student')
        if CustomUser.objects.filter(username=username).exists:
            messages.warning(request,'Usuário já existe no sistema')
            return redirect('add_student')
        else:
            user = CustomUser(
                first_name = first_name,
                last_name = last_name,
                username = username,
                email = email,
                profile_pic = profile_pic,
                user_type = 3,
            )
            user.set_password = password
            user.save()

            course = Course.objects.get(id = course_id)
            session_year = Session_Year.objects.get(id = session_year_id)

    context = {
        'course': course,
        'session_year': session_year,
    }
    return render(request,'Hod/add_student.html',context)

@login_required(login_url='/')
def VIEW_STUDENT(request):
    return render(request,'Hod/view_student.html')
