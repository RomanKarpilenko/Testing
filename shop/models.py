from django.db import models

# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')
#     def __str__(self):
#         return self.question_text
#
# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)
#     def __str__(self):
#         return self.choice_text
#
# class Subscribers(models.Model):
#     Email = models.EmailField()
#     Name = models.CharField(max_length=30)
#     def __str__(self):
#         return self.Name

class Track (models.Model):
    track_name = models.CharField(max_length=100, blank=False)
    track_text = models.TextField(max_length=1000, blank=False)
    icon = models.CharField(max_length=300, blank=False)
    date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    def __str__(self):
         return self.track_name