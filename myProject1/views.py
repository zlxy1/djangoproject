from django.shortcuts import render, redirect, get_object_or_404
from .models import Staff
from django.urls import reverse
# 公共函数
def get_filter_staff(params):
    qs=Staff.objects.all()
    search_name=params.get('name','')
    search_gender=params.get('gender','')
    if search_name:
        qs=qs.filter(name__icontains=search_name)
    if search_gender:
        qs=qs.filter(gender=search_gender)
    return qs

def staff_list(request):
   search_name=request.GET.get('name','')
   search_gender=request.GET.get('gender','')
   staff_list=get_filter_staff(request.GET)
   context={'staff_list':staff_list,
            'search_name':search_name,
            'search_gender':search_gender}
   return render(request,'staff/list.html',context)

# 新增员工
def staff_add(request):
    if request.method == "GET":
        return render(request, 'staff/add.html')
    if request.method == "POST":
        Staff.objects.create(
            name=request.POST["name"],
            gender=request.POST["gender"],
            id_card=request.POST.get("id_card") or None,
            phone=request.POST.get("phone") or None,
            birth=request.POST.get("birth") or None,
            address=request.POST.get("address", "")
        )
        return redirect(reverse('staff_list'))

# 编辑员工
def staff_edit(request, pk):
    staff = get_object_or_404(Staff, pk=pk)
    if request.method == 'GET':
        return render(request, 'staff/edit.html', {'staff': staff})
    if request.method == "POST":
        staff.name = request.POST.get("name")
        staff.gender = request.POST.get("gender")
        staff.id_card = request.POST.get("id_card")
        staff.address = request.POST.get("address")
        staff.save()
        return redirect(reverse('staff_list'))

# 删除员工
def staff_delete(request, pk):
    staff = get_object_or_404(Staff, pk=pk)
    if request.method == 'POST':
        staff.delete()
        return redirect('staff_list')
    return redirect('staff_list')
