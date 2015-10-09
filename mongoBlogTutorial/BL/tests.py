from django.test import TestCase

from models import Post
# Create your tests here.

class QuestionMethodTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        post = Post.objects.create(title='Hello MongoDB!',text='Just wanted to drop a note from Django. Cya!',tags=['mongodb', 'django'])

