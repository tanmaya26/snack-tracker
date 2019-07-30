from django.db import models
import os


class User(models.Model):
    name = models.CharField(max_length=200, default='admin')
    password = models.CharField(max_length=200, default='admin')
    email = models.CharField(max_length=200, default='admin@admin.com')

    def __str__(self):
        return "{} - {}".format(self.name, self.password)


def get_image_path(instance, filename):
    return os.path.join('photos', filename[28:len(filename)])


class Snack(models.Model):
    snack_name = models.CharField(max_length=200)
    snack_quantity = models.IntegerField('Quantity')
    snack_description = models.CharField(max_length=200, default='desc')
    snack_image = models.CharField(null=True, max_length=200)
    snack_tag = models.CharField(max_length=200, default='SWEET', null=True)

    def __str__(self):
        return "{} - {} - {}".format(self.snack_name, self.snack_quantity, self.snack_description)


class Image(models.Model):
    image = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    snack = models.ForeignKey(Snack, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.image)


class Tag(models.Model):
    snack = models.ForeignKey(Snack, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return "{} - {}".format(self.snack, self.name)


class Request(models.Model):
    snack = models.ForeignKey(Snack, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=0)
    description = models.CharField(max_length=200, default='yummy')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, null=True, blank=True)
    image = models.CharField(max_length=200, null=True)

    def __str__(self):
        return "{} - {}".format(self.snack, self.quantity)


class Operation(models.Model):
    operation = models.CharField(max_length=200)

    def __str__(self):
        return "{}".format(self.operation)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    snack = models.ForeignKey(Snack, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return "{} - {} - {}".format(self.user, self.snack, self.likes)


class Dislike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    snack = models.ForeignKey(Snack, on_delete=models.CASCADE)
    dislikes = models.IntegerField(default=0)

    def __str__(self):
        return "{} - {} - {}".format(self.user, self.snack, self.dislikes)
