from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    #Due to the fact that almost always in application we want to see only published posts, we make helper manager. So, we dont need always to filter every query on posts by status 'published'
    class PostObject(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status = 'published')

    options = (
        ('draft',  'Draft'),
        ('published', 'Published')
    )

    category = models.ForeignKey(Category, on_delete =models.PROTECT, default=1) #not permit category if any post in db exist which is of that category
    title = models.CharField(max_length=50)
    excerpt = models.TextField(null=True)
    content = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='published')
    published = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts') #if we delete user from db, all its posts will be also deleted. We can use posts of user like 'user__blog_posts, due to the related_name attr.
    status = models.CharField(max_length=20, choices=options, default='published')

    objects = models.Manager() # default manager
    postobjects = PostObject() #our custom 'status filtered' manager

    class Meta:
        ordering: ('-published',)

    def __str__(self):
        return self.title