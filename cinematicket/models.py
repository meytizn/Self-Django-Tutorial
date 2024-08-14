from django.db import models
from django.utils.translation import gettext as _
from django.urls import reverse

# Create your models here.


class Food(models.Model):
  name=models.CharField(_("نام محصصول"), max_length=50)
  description=models.TextField(_("توضیحات محصول"))
  photo=models.ImageField(_("تصویر محصول"), upload_to='cinematicket/')
  rate=models.IntegerField(_("امتیاز محصول"))
  time=models.IntegerField(_("زمان انتظار"))
  price=models.IntegerField(_("قیمت محصول"))
  category=models.ForeignKey("Category", verbose_name=_("دسته بندی محصول  "), on_delete=models.CASCADE,related_name="blog",blank=True,null=True)
  pub_date=models.DateField(_("تاریخ انتشار"), auto_now=False, auto_now_add=True)

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse ("cinematicket:food_list")


class Category(models.Model):
  title=models.CharField(_("عنوان دسته بندی "), max_length=50)
  slug=models.SlugField(_("عنوان دسته بندی لاتین "))
  pub_date=models.DateField(_("زمان انتشار"), auto_now=False, auto_now_add=True)

  def __str__(self):
    return self.title