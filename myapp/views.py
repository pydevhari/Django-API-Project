from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Marks
from .models import Addmision

class Insertdata(View):

    def display_page(request):
        return render(request, 'index.html')

    def get_result(request):
        return render(request, 'get_result.html')

    def admission(request):
        return render(request, 'admission.html')

    def delete_student(request):
        return render(request, 'delete_student.html')

    def delete_stu(request):
        if request.method == 'POST':
            name = request.POST['name']
            email = request.POST['email']
            Addmision.objects.filter(name=name, email=email).delete()
            return HttpResponse('Admission cancelled successfully!!')

    def update_action(request):
        if request.method == 'POST':
            name = request.POST['name']
            email = request.POST['email']
            fname = request.POST['fname']
            mname = request.POST['mname']
            mob = request.POST['mob']

            Addmision.objects.filter(name=name, mob=mob).update(email=email, fname=fname, mname=mname)
            return HttpResponse('<script>alert("Data updated successfully!!")</script>')

    def update_detail(request):
        return render(request, 'update_detail.html')

    def update_verify(request):
        if request.method == 'POST':
            name = request.POST['name']
            email = request.POST['email']
            query_set = Addmision.objects.filter(name=name, email=email)
            if query_set.count():
                return render(request, 'update_panel.html', {'results': query_set})
            else:
                return render(request, 'update_detail.html')

    def insert_addmision_data(request):
        if request.method == 'POST':
            name = request.POST['name']
            email = request.POST['email']
            fname = request.POST['fname']
            mname = request.POST['mname']
            mob = request.POST['mob']

            query_set = Addmision(name=name, email=email,
                        fname=fname, mname=mname, mob=mob)
            query_set.save()
            return HttpResponse('Admission successfully')

    # @csrf_token
    def insert_data(request):
        if request.method == 'POST':
            name = request.POST['name']
            roll = request.POST['roll']
            enroll = request.POST['enroll']
            fname = request.POST['fname']
            mname = request.POST['mname']
            total = request.POST['total']
            result = request.POST['result']
            category = request.POST['category']
            obt_list = [request.POST['obt_dbms'], request.POST['obt_os'],
                        request.POST['obt_algo'], request.POST['obt_java'],
                        request.POST['obt_cn'], request.POST['obt_java'],
                        request.POST['obt_java_lab']]
            remark_list = [request.POST['remark_dbms'], request.POST['remark_algo'],
                           request.POST['remark_java'], request.POST['remark_os'],
                           request.POST['remark_cn'], request.POST['remark_java_lab']]
            for i in range(6):
                data = Marks(name=name, enroll=enroll, roll=roll, fname=fname, mname=mname,
                             category=category, obt=obt_list[i], remark = remark_list[i],
                             total=total, result=result)
                data.save()
            return render(request, 'get_result.html')

    def fetch_result_data(request):
        if request.method == 'POST':
            roll_no = request.POST['roll_no']
            results = Marks.objects.filter(roll=roll_no)
            if results.count():
                obts = []
                remarks = []
                for i in results:
                    obts.append(i.obt)
                    remarks.append(i.remark)
                data = {'results': results, 'obt':obts, 'remark':remarks}
                return render(request, 'display_result.html', data)
            else:
                return render(request, 'get_result.html')

