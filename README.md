# LearnPy

Django scripts

    virtualenv pyblog
    cd pyblog
    scripts\activate

    pip install django
    python -m django --version
    django-admin

    django-admin startproject django_project
    cd django_project

    python manage.py runserver

    python manage.py startapp blog

    python manage.py makemigrations
        python manage.py sqlmigrate blog 0001
    python manage.py migrate
        

    python manage.py createsuperuser

    python manage.py shell
        from blog.models import Post
        from django.contrib.auth.models import User
        User.objects.all()
        User.objects.first()
        User.objects.filter(username='viks')
        User.objects.filter(username='viks').first()
        user = User.objects.filter(username='viks').first()
        user.id
        user.pk
        user = User.objects.get(id=1)

        Post.objects.all()
        post_1 = Post(title='blog1', content = 'first post content', author=user)
        post_1.save()

        post_2 = Post(title='blog2', content = '2 post content', author_id=user.id)
        post_2.save()

        post = Post.objects.first()
        post.content
        post.date_posted
        post.author
        post.author.email

        user.post_set
        user.post_set.all()
        user.post_set.create(title='blog 3', content = '3 post content')






    