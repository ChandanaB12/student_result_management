from django.db import models

class Student(models.Model):
    usn = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=50)

    semester = models.CharField(max_length=20)
    academic_year = models.CharField(max_length=20)

    def __str__(self):
        return self.usn


class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    subject_code = models.CharField(max_length=20)
    subject_name = models.CharField(max_length=100)

    internal_marks = models.IntegerField()
    external_marks = models.IntegerField()

    total_marks = models.IntegerField()

    status = models.CharField(max_length=10)

    def save(self, *args, **kwargs):
        self.total_marks = self.internal_marks + self.external_marks

        if self.internal_marks >= 20 and self.external_marks >= 20:
            self.status = "PASS"
        else:
            self.status = "FAIL"

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.student.usn} - {self.subject_code}"

