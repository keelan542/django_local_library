from django.db import models
from django.urls import reverse
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower

class Genre(models.Model):
    """Model representing a book genre"""
    name = models.CharField(
        max_length=200,
        unique=True,
        help_text="Enter a book genre (e.g. Science Function, French)"
    )

    def __str__(self):
        """String for representing the Model object"""
        return self.name
    
    def get_absolute_url(self):
        """Returns the url to access a particular genre instance"""
        return reverse('genre-detail', args=[str(self.id)])
    
    class Meta:
        constrains = [
            UniqueConstraint(
                Lower('name'),
                violation_error_message="Genre already exists (case insensitive match)"
            )
        ]