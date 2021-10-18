from django.shortcuts import render, redirect, get_object_or_404
from .models import study
from django.contrib.auth.models import User

# Create your views here.
def studylist(request):
    posts = study.objects.all()
    return render(request, "study/studylist.html", {"posts": posts})


def new(request):
    return render(request, "study/new.html")


def create(request):
    new_study = study()
    new_study.writer = request.user
    new_study.name = request.POST["name"]
    new_study.section = request.POST["section"]
    new_study.intro = request.POST["intro"]
    new_study.qualification = request.POST["qualification"]
    new_study.member_start = request.POST["member_start"]
    new_study.member_end = request.POST["member_end"]
    new_study.start_date = request.POST["start_date"]
    new_study.due_date = request.POST["due_date"]
    new_study.body = request.POST["body"]
    new_study.difficulty = request.POST["difficulty"]
    new_study.phnum = request.POST["phnum"]
    new_study.image = request.FILES.get("image")
    new_study.is_over = False  # 기본 상태 False

    new_study.save()
    new_study.study_member.add(request.user)  # study가 만들어진 다음에 멤버에 추가해야함

    return redirect("study:detail", new_study.id)


def apply_study(request, id):
    cur_study = study.objects.get(id=id)
    is_apply = request.user in cur_study.study_member_request.all()  # 지원 여부 확인
    if is_apply:  # 지원 취소
        cur_study.study_member_request.remove(request.user)
    else:  # 지원
        cur_study.study_member_request.add(request.user)

    return redirect("study:detail", cur_study.id)


def accept_request(request, study_id, user_id):
    request_user = get_object_or_404(User, pk=user_id)
    cur_study = study.objects.get(id=study_id)
    cur_study.study_member_request.remove(request_user)  # 대기 멤버에서 제거
    cur_study.study_member.add(request_user)  # 멤버에 추가

    return redirect("study:detail", cur_study.id)


def refuse_request(request, study_id, user_id):
    request_user = get_object_or_404(User, pk=user_id)
    cur_study = study.objects.get(id=study_id)
    cur_study.study_member_request.remove(request_user)  # 대기 멤버에서 제거

    return redirect("study:detail", cur_study.id)


def recruit_over(request, id):
    cur_study = study.objects.get(id=id)
    cur_study.is_over = True
    cur_study.study_member_request.clear()  # 마감할거니까 혹시라도 가입요청 있으면 다 지워
    cur_study.save()

    return redirect("study:detail", cur_study.id)


def detail(request, id):
    post = get_object_or_404(study, pk=id)
    # is_author : 현재 접속한 유저가 수정하려는 스터디의 작성자인지 확인하고 저장
    if request.user == post.writer:
        is_author = True
    else:
        is_author = False

    return render(request, "study/detail.html", {"post": post, "is_author": is_author})


def edit(request, id):
    edit_study = study.objects.get(id=id)
    # is_author : 현재 접속한 유저가 수정하려는 스터디의 작성자인지 확인하고 저장
    if request.user == edit_study.writer:
        is_author = True
    else:
        is_author = False

    return render(
        request, "study/edit.html", {"post": edit_study, "is_author": is_author}
    )


def update(request, id):
    update_study = study.objects.get(id=id)
    update_study.writer = request.user
    update_study.name = request.POST["name"]
    update_study.section = request.POST["section"]
    update_study.intro = request.POST["intro"]
    update_study.qualification = request.POST["qualification"]
    update_study.member_start = request.POST["member_start"]
    update_study.member_end = request.POST["member_end"]
    update_study.start_date = request.POST["start_date"]
    update_study.due_date = request.POST["due_date"]
    update_study.body = request.POST["body"]
    update_study.difficulty = request.POST["difficulty"]
    update_study.phnum = request.POST["phnum"]
    if request.FILES.get("image"):  # 이미지가 새로 들어오지 않으면 건드리지 않음
        update_study.image = request.FILES.get("image")

    update_study.save()

    return redirect("study:detail", update_study.id)


def delete(request, id):
    delete_study = study.objects.get(id=id)
    delete_study.delete()

    return redirect("study:studylist")