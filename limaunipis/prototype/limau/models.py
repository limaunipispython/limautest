from django.db import models
from django.template.defaultfilters import slugify 
from django.utils import timezone
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill
from limau.choices import * 
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

# Recipe category class like [Malay, Asian, Western]
class RecipeCategory(models.Model):
    name_bm = models.CharField(max_length=128)
    name_en = models.CharField(max_length=128)
    description = models.TextField()
    slug = models.SlugField(default="will-be-generated-once-save")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name_en)
        super(RecipeCategory, self).save(*args, **kwargs)

    def __str__(self):
        return self.name_en

# Article category class like [General, Baby food, Health food]
class ArticleCategory(models.Model):
    name_bm = models.CharField(max_length=128)
    name_en = models.CharField(max_length=128)
    description = models.TextField()
    slug = models.SlugField(default="will-be-generated-once-save")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name_en)
        super(ArticleCategory, self).save(*args, **kwargs)

    def __str__(self):
        return self.name_en

# Restaurant category like [Malay, Western, Thai, Russian, etc]
class RestaurantCategory(models.Model):
    name_bm = models.CharField(max_length=128)
    name_en = models.CharField(max_length=128)
    description = models.TextField()
    slug = models.SlugField(default="will-be-generated-once-save")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name_en)
        super(RestaurantCategory, self).save(*args, **kwargs)

    def __str__(self):
        return self.name_en

# ingredient class for ingredient like [limau-nipis, sugar, salt, etc]
class Ingredient(models.Model):
    name_bm = models.CharField(max_length=128)
    name_en = models.CharField(max_length=128)
    thumbnail = ProcessedImageField(upload_to='ingredient_thumbnail', processors=[ResizeToFill(320,180)], format="JPEG", options={'quality':70})
    description = models.TextField()
    slug = models.SlugField(default='will-be-generated-once-save')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name_en)
        super(Ingredient, self).save(*args, **kwargs)

    def __str__(self):
        return self.name_en

class Recipe(models.Model):
    recipecategory = models.ForeignKey(RecipeCategory)
    name_bm = models.CharField(max_length=128)
    name_en = models.CharField(max_length=128)
    youtube_url = models.URLField()
    thumbnail = ProcessedImageField(upload_to='recipe_thumbnail', processors=[ResizeToFill(640,360)], format="JPEG", options={'quality':70})
    thumbnail2 = ProcessedImageField(upload_to='recipe_thumbnail', processors=[ResizeToFill(640,360)], format="JPEG", options={'quality':70})
    thumbnail3 = ProcessedImageField(upload_to='recipe_thumbnail', processors=[ResizeToFill(640,360)], format="JPEG", options={'quality':70})
    description = models.TextField(default="type a description of your recipe")
    ingredient_content = models.TextField(default="type your ingredients here, in <li> form")
    ingredients = models.ManyToManyField(Ingredient)
    created_date = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(default='will-be-generated-once-save')
    serve = models.IntegerField(choices=SERVING_NUMBER, default=3)
    instruction = models.TextField(default="fill in step by step instruction here")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name_en)#should be name_bm
        super(Recipe, self).save(*args, **kwargs)

    def __str__(self):
        return self.name_en

class Article(models.Model):
    articlecategory = models.ManyToManyField(ArticleCategory)
    title_bm = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    thumbnail = ProcessedImageField(upload_to='article_thumbnail', processors=[ResizeToFill(640,260)], format="JPEG", options={'quality':80})
    text_bm = models.TextField()
    slug = models.SlugField(default='will-be-generated-once-save')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title_bm)
        super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return self.title_bm

class Restaurant(models.Model):
    restaurantcategory = models.ManyToManyField(RestaurantCategory)
    name_bm = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    description = models.TextField()
    building_thumbnail = ProcessedImageField(upload_to='restaurant_thumbnail/building', processors=[ResizeToFill(320,180)], format="JPEG", options={'quality':70})
    menu_thumbnail = ProcessedImageField(upload_to='restaurant_thumbnail/menu', processors=[ResizeToFill(320,180)], format="JPEG", options={'quality':70})
    food_thumbnail_1 = ProcessedImageField(upload_to='restaurant_thumbnail/food', processors=[ResizeToFill(320,180)], format="JPEG", options={'quality':70})
    food_thumbnail_2 = ProcessedImageField(upload_to='restaurant_thumbnail/food', processors=[ResizeToFill(320,180)], format="JPEG", options={'quality':70})
    created_date = models.DateTimeField(default=timezone.now)
    food_quality = models.IntegerField(choices=RATING_CHOICES, default=1)
    food_variety = models.IntegerField(choices=RATING_CHOICES, default=1)
    etiquette = models.IntegerField(choices=RATING_CHOICES, default=1)
    cleanliness = models.IntegerField(choices=RATING_CHOICES, default=1)
    access = models.IntegerField(choices=RATING_CHOICES, default=1)
    limau_meter = models.IntegerField(default=1)
    starhtml = models.TextField(default="nothing")
    slug = models.SlugField(default='will-be-generated-once-save')

    def calculate_meter(self):
        average = float(self.food_quality*0.4+self.food_variety*0.2+self.etiquette*0.15+self.cleanliness*0.15+self.access*0.10)
        return int(round(average))

    def return_star(self, meter):
        multiplierFull = int(meter)
        multiplierVoid = 5-int(meter)
        fullStar = '<i class="fa fa-star"></i>'
        voidStar = '<i class="fa fa-star-o"></i>'
        value = multiplierFull*fullStar + multiplierVoid*voidStar
        return value
        
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name_bm)
        self.limau_meter = self.calculate_meter()
        self.starhtml = self.return_star(meter=self.limau_meter)
        super(Restaurant, self).save(*args, **kwargs)

    def __str__(self):
        return self.name_bm

class UserRecipe(models.Model):
    # pending user field to identify who submit the recipe
    user = models.ForeignKey('auth.User')
    recipecategory = models.ForeignKey(RecipeCategory)
    name_bm = models.CharField(max_length=128, unique=True)
    name_en = models.CharField(max_length=128, unique=True)
    description = models.TextField(max_length=300, default="my food is the best in the world!!") #this one should be a textfield 
    ingredients = models.TextField(default="key in your ingredienst here in <li>ingredients</li> tag")
    instructions = models.TextField(default="key in your instruction here in <li>ingredients<li> tag")
    picture_1 = ProcessedImageField(upload_to='user_recipe_thumbnail', processors=[ResizeToFill(640,360)], format="JPEG", options={'quality':70})
    picture_2 = ProcessedImageField(upload_to='user_recipe_thumbnail', processors=[ResizeToFill(640,360)], format="JPEG", options={'quality':70})
    #need to add postdate field
    created_date = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(default='will-be-generated-once-save')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name_bm)
        super(UserRecipe, self).save(*args, **kwargs)

    def __str__(self):
        return self.name_bm

# Additional attribute for user model
# Default User model contains username, password, email, first name, surname
class UserProfile(models.Model):
    # Link UserProfile to a User model instance
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Additional attributes to be added
    default_pic = '/media/user_picture/Koala.jpg'  
    picture = ProcessedImageField(upload_to="user_picture", processors=[ResizeToFill(180, 180)], format="JPEG", options={'quality':70}, null=True, blank=True, default=default_pic)
    description = models.TextField(max_length=300, default="description")
    badge = models.IntegerField(choices=BADGES, default=3)

    def __str__(self):
        return self.user.username

# Below is the code to auto create user profile when they register
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()


class MobileBanner(models.Model):
    name = models.CharField(max_length=100, default="description")
    image = ProcessedImageField(upload_to="mobilebanner", processors=[ResizeToFill(360, 360)], format="PNG", options={'quality':70}, null=True, blank=True)
    status = models.IntegerField(choices=ACTIVE_CHOICES, default=2)
    image_url = models.URLField(default="www.google.com")

    def __str__(self):
        return self.name

# models for announcement
class Announcement(models.Model):
    about = models.CharField(max_length=50, default="description of announcement")
    text = models.TextField(default="write the announcement here")
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.about

# ---------------------Product Section---------------------------
# models for Product

class ProductCategory(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField(default="fill in product description here")
    slug = models.SlugField(default="will-be-generated-once-save")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(ProductCategory, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(ProductCategory, null=True)
    name = models.CharField(max_length=100, default="fill in your product name here")
    image_1 = ProcessedImageField(upload_to="products", processors=[ResizeToFill(360, 360)], format="PNG", options={'quality':80}, null=True, blank=True )
    image_2 = ProcessedImageField(upload_to="products", processors=[ResizeToFill(360, 360)], format="PNG", options={'quality':80}, null=True, blank=True )
    image_3 = ProcessedImageField(upload_to="products", processors=[ResizeToFill(360, 360)], format="PNG", options={'quality':80}, null=True, blank=True )
    image_4 = ProcessedImageField(upload_to="products", processors=[ResizeToFill(360, 360)], format="PNG", options={'quality':80}, null=True, blank=True )
    definition = models.CharField(max_length=300, default="Fill in product short definition here")
    optional_definition_switch = models.BooleanField(default=True)
    optional_definition = models.TextField(default="Fill in extra definition in HTML form here if switch = true")
    original_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_switch = models.BooleanField(default=False)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default="5.00")
    in_stock = models.BooleanField(default=True)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2, default="50.00")
    member_price_switch = models.BooleanField(default=False)
    discount_member = models.DecimalField(max_digits=10, decimal_places=2, default="7.50")
    discounted_member_price = models.DecimalField(max_digits=10, decimal_places=2, default="50.00")
    slug = models.SlugField(default="will-be-generated-once-save")
    created_date = models.DateTimeField(default=timezone.now)

    def calculate_general_price(self):
        value = ((100-self.discount)/100)*self.original_price
        return float(round(value))

    def calculate_member_price(self):
        value = ((100-self.discount_member)/100)*self.original_price
        return float(round(value))
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.discounted_price = self.calculate_general_price()
        self.discounted_member_price = self.calculate_member_price()
        super(Product, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name

class ProductBanner(models.Model):
    name = models.CharField(max_length=300)
    image = ProcessedImageField(upload_to="productBanners", processors=[ResizeToFill(960, 384)], format="PNG", options={'quality':80}, null=True, blank=True )
    description = models.CharField(max_length=300)  

    def __str__(self):
        return self.name

    




