from django.db import models
from django.contrib.auth.models import User

class Quiz(models.Model):
    class Topic(models.TextChoices):
        GENERAL_KNOWLEDGE = 'GK', 'General Knowledge'
        MOVIES = 'MV', 'Movies & TV Shows'
        GAMES = 'VG', 'Video Games'
        MUSIC = 'MU', 'Music'
        SCIENCE = 'SC', 'Science & Nature'
        HISTORY = 'HS', 'History & Culture'
        INTERNET = 'IN', 'Internet & Pop Culture'
        SPORTS = 'SP', 'Sports'
        LITERATURE = 'LT', 'Literature & Language'
        LOGIC = 'LG', 'Logic & Riddles'
        ANIME = 'AN', 'Anime'
        CARTOON = 'CT', 'Cartoons'

    title = models.CharField(max_length=50)
    topic = models.CharField(
        max_length=10,
        choices=Topic.choices,
        default=Topic.GENERAL_KNOWLEDGE,
    )
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="quiz_images/", null=True, blank=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.get_topic_display()})"

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to="quiz_questions_images/", null=True, blank=True)
    image_url = models.URLField(blank=True, null=True)

class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    text = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to="quiz_answers_images/", null=True, blank=True)
    image_url = models.URLField(blank=True, null=True)
    is_correct = models.BooleanField(default=False) 
    
    