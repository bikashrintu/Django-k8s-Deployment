from django.db import models


class NewStock(models.Model):
    company = models.CharField(max_length=100, null=True, blank=True)
    model = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='images/')
    description1 = models.TextField()
    description2 = models.TextField()

    def __str__(self):
        return self.model if self.model else "Unnamed Model"  # ✅ Ensures a string is always returned
    

# Define choices for year fields
YEAR_CHOICES = [(r, r) for r in range(2000, 2026)]  # Example range
MANUFACTURE_YEAR_CHOICES = [(r, r) for r in range(1990, 2026)]  # Adjust as needed

class AddStock(models.Model):
    company = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    registered_year = models.IntegerField(choices=YEAR_CHOICES, default=2024)
    owners = models.IntegerField()  # Removed max_length
    color = models.CharField(max_length=100)
    kilometers_done = models.IntegerField()
    fuel_type = models.CharField(max_length=100)
    type=models.CharField(max_length=100, null=True ,blank=True)
    manufactured = models.IntegerField(choices=MANUFACTURE_YEAR_CHOICES, default=2025)
    mileage = models.DecimalField(max_digits=4, decimal_places=1, null=True ,blank=True)  # Increased max_digits

    def __str__(self):
        return f"{self.company} {self.model} ({self.registered_year})"

class CarImages(models.Model):
    Car=models.ForeignKey(AddStock, on_delete=models.CASCADE, related_name='images')
    image1 = models.ImageField(upload_to='product_images/' , blank=True, null=True)
    image2 = models.ImageField(upload_to='product_images/' , blank=True, null=True)
    image3 = models.ImageField(upload_to='product_images/' , blank=True, null=True)
    image4 = models.ImageField(upload_to='product_images/' , blank=True, null=True)
    image5 = models.ImageField(upload_to='product_images/' , blank=True, null=True)
    image6 = models.ImageField(upload_to='product_images/' , blank=True, null=True)
    image7 = models.ImageField(upload_to='product_images/' , blank=True, null=True)
    image8 = models.ImageField(upload_to='product_images/' , blank=True, null=True)
    image9 = models.ImageField(upload_to='product_images/' , blank=True, null=True)
    image10 = models.ImageField(upload_to='product_images/' , blank=True, null=True)
    image11 = models.ImageField(upload_to='product_images/' , blank=True, null=True)
    image12 = models.ImageField(upload_to='product_images/' , blank=True, null=True)



class Review(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    review = models.TextField()
    image = models.ImageField(upload_to='review_images/', blank=True, null=True)  # Image field

    def __str__(self):
        return self.name




# Create your models here.
