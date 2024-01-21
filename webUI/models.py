from django.db import models


# class User(models.Model):
#     username = models.CharField(max_length=50)
#     password = models.CharField(max_length=50)

#     def __str__(self):
#         return self.username

# class Group(models.Model):
#     name = models.CharField(max_length=50)

#     def __str__(self):
#         return self.name


# class User_Groups(models.Model):
#     userid = models.CharField(max_length=50)
#     groupid = models.CharField(max_length=50)

#     def __str__(self):
#         return self.groupid

from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username

class Group(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class User_Groups(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.group.name}"
