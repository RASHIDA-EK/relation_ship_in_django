# enrollment/models.py

from django.db import models
from course.models import Course, Student

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_enrolled = models.DateField()

    class Meta:
        unique_together = ('student', 'course')

    def __str__(self):
        return f"{self.student.name} enrolled in {self.course.name}"
