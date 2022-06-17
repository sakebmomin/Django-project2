from django.contrib import admin
from relations.models import Album,Song,Author,Book,Vehicle,Car


@admin.register(Album)
class Album(admin.ModelAdmin):
    pass

@admin.register(Song)
class Song(admin.ModelAdmin):
    pass

@admin.register(Author)
class Author(admin.ModelAdmin):
    pass

@admin.register(Book)
class Book(admin.ModelAdmin):
    pass

@admin.register(Vehicle)
class Vehicle(admin.ModelAdmin):
    pass

@admin.register(Car)
class Car(admin.ModelAdmin):
    pass

# Register your models here.
