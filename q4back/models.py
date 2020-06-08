from django.db import models

# Create your models here.


class Artist(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    information = models.TextField()


class Artwork(models.Model):
    PALLET_CHOICE(
        blue, yellow, red, light, dark
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    artist = models.ForeignKey(
        Artist, on_delete=models.CASCADE, related_name='artwork')
    primary_pallet = models.CharField(max_length=1, choices=PALLET_CHOICE)
    secondary_pallet = models.CharField(max_length=1, choices=PALLET_CHOICE)
    medium = models.CharField(max_length=100)


class ArtistImage(models.Model):
    artist_image = models.ForeignKey(
        Artist, on_delete=models.CASCADE, related_name='artist_image')
    image_url = models.ImageField()


class ArtworkImage(models.Model):
    artwork_image = models.ForeignKey(
        Artwork, on_delete=models.CASCADE, related_name='artwork_image')
    image_url = models.ImageField()
