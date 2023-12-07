from django.contrib import admin
from schedule.models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "major", "grade_point_avg", "year_in_school"]
    list_display_links = ["first_name", "last_name", "major", "grade_point_avg", "year_in_school"]

admin.site.register(Student, StudentAdmin)
