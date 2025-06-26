from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name=_("Category Name"),
        help_text=_("The name of the category as displayed to users")
    )
    slug = models.SlugField(
        max_length=100,
        unique=True,
        verbose_name=_("URL Slug"),
        help_text=_("A URL-friendly version of the name (auto-generated if blank)")
    )
    order = models.PositiveIntegerField(
        default=0,
        verbose_name=_("Display Order"),
        help_text=_("Higher numbers appear first. Categories with same order are sorted alphabetically.")
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name=_("Is Active"),
        help_text=_("Whether this category should be displayed")
    )
    show_in_navbar = models.BooleanField(
        default=True,
        verbose_name=_("Show in Navigation"),
        help_text=_("Display this category in the main navigation bar")
    )
    template_name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name=_("Custom Template"),
        help_text=_("Override default template (e.g., 'navigation/contact.html')")
    )
    
    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
        ordering = ['-order', 'name']
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('navigation:category', args=[self.slug])
    
    def save(self, *args, **kwargs):
        if not self.slug:
            from django.utils.text import slugify
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class SubCategory(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name=_("Subcategory Name")
    )
    slug = models.SlugField(
        max_length=100,
        unique=True,
        verbose_name=_("URL Slug")
    )
    category = models.ForeignKey(
        Category, 
        related_name='subcategories', 
        on_delete=models.CASCADE,
        verbose_name=_("Parent Category")
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name=_("Is Active")
    )
    order = models.PositiveIntegerField(
        default=0,
        verbose_name=_("Display Order"),
        help_text=_("Higher numbers appear first within the same category")
    )
    template_name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name=_("Custom Template")
    )
    
    class Meta:
        verbose_name = _("Subcategory")
        verbose_name_plural = _("Subcategories")
        ordering = ['category__order', '-order', 'name']
        constraints = [
            models.UniqueConstraint(
                fields=['category', 'slug'],
                name='unique_category_subcategory_slug'
            )
        ]
    
    def __str__(self):
        return f"{self.category.name} > {self.name}"
    
    def get_absolute_url(self):
        return reverse('navigation:subcategory', args=[self.slug])
    
    def save(self, *args, **kwargs):
        if not self.slug:
            from django.utils.text import slugify
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)