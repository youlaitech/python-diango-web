import MySQLdb
from django.shortcuts import render, redirect


# Create your views here.
# 学生信息列表处理函数
def index(request):
    student_no = request.GET.get('student_no', '')
    student_name = request.GET.get('student_name', '')

    sql = "SELECT id,student_no,student_name FROM sims_student WHERE 1=1 "
    if student_no.strip() != '':
        sql = sql + " and student_no = '" + student_no+"'"
    if student_name.strip() != '':
        sql = sql + " and student_name = '" + student_name+"'"

    print(sql)
    conn = MySQLdb.connect(host="localhost", user="root", passwd="123456", db="sms", charset='utf8')
    with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
        cursor.execute(sql)
        students = cursor.fetchall()
    return render(request, 'student/index.html', {'students': students,
                                                  'student_name':student_name,'student_no':student_no})


# 学生信息新增处理函数
def add(request):
    if request.method == 'GET':
        return render(request, 'student/add.html')
    else:
        student_no = request.POST.get('student_no', '')
        student_name = request.POST.get('student_name', '')
        conn = MySQLdb.connect(host="localhost", user="root", passwd="123456", db="sms", charset='utf8')
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("INSERT INTO sims_student (student_no,student_name) "
                           "values (%s,%s)", [student_no, student_name])
            conn.commit()
        return redirect('../')


# 学生信息修改处理函数
def edit(request):
    if request.method == 'GET':
        id = request.GET.get("id")
        conn = MySQLdb.connect(host="localhost", user="root", passwd="123456", db="sms", charset='utf8')
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("SELECT id,student_no,student_name FROM sims_student where id =%s", [id])
            student = cursor.fetchone()
        return render(request, 'student/edit.html', {'student': student})
    else:
        id = request.POST.get("id")
        student_no = request.POST.get('student_no', '')
        student_name = request.POST.get('student_name', '')
        conn = MySQLdb.connect(host="localhost", user="root", passwd="123456", db="sms", charset='utf8')
        with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
            cursor.execute("UPDATE sims_student set student_no=%s,student_name=%s where id =%s",
                           [student_no, student_name, id])
            conn.commit()
        return redirect('../')


# 学生信息删除处理函数
def delete(request):
    id = request.GET.get("id")
    conn = MySQLdb.connect(host="localhost", user="root", passwd="123456", db="sms", charset='utf8')
    with conn.cursor(cursorclass=MySQLdb.cursors.DictCursor) as cursor:
        cursor.execute("DELETE FROM sims_student WHERE id =%s", [id])
        conn.commit()
    return redirect('../')
