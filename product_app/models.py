from django.db import models
from cloudinary.models import CloudinaryField
from category_app.models import Category
from django.core.validators import MinValueValidator, MaxValueValidator  

class Product(models.Model):
    product_name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image_1 = CloudinaryField('image')
    image_2 = CloudinaryField('image', blank=True, null=True)
    image_3 = CloudinaryField('image', blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_listed = models.BooleanField(blank=False, default=True)
    delete_opt = models.BooleanField(blank=False, default=False)
    offer_percentage = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)], default=0
    )

    def save(self, *args, **kwargs):
        if self.category:
            self.unit = self.category.category_unit
        super().save(*args, **kwargs)


    def __str__(self):
        return self.product_name

    
#==========================================================================================================

class Variant(models.Model):
    ATTAR = [
        ('3ml', '3ml'), ('6ml', '6ml'), ('12ml', '12ml'),
    ]
    PERFUME = [
        ('10ml', '10ml'), ('20ml', '20ml'), ('100ml', '100ml'),
    ]
    STICKS = [
        ('20gm', '20gm'), ('50gm', '50gm'), ('100gm', '100gm'),
    ]

    SIZE_CHOICES = ATTAR + PERFUME + STICKS

    product = models.ForeignKey(Product, related_name='variants', on_delete=models.CASCADE)
    size = models.CharField(max_length=255, choices=SIZE_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    stock = models.PositiveIntegerField()
    offer_percentage = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)], default=0
    )
    created_at = models.DateField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)
    featured = models.BooleanField(blank=False, default=False) 
    
    
    def product_price_after(self):

        variant_offer = self.offer_percentage
        product_offer = self.product.offer_percentage
        category_offer = self.product.category.category_offer

        highest_offer = max(variant_offer, product_offer, category_offer)    # we need only to apply the highest offers among 
                                                                             # these three levels offers
        discounted_price = self.price - (highest_offer * self.price / 100)

        return round(discounted_price, 2)
    
    def __str__(self): 
        return f"{self.product.product_name} - {self.size}"