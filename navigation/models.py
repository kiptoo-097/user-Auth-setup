from django.db import models

class NavLink(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=255, help_text="Use named URL or full path (e.g., /about/)")
    order = models.PositiveIntegerField(default=0)
    is_dropdown = models.BooleanField(default=False)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name


class DropdownLink(models.Model):
    parent = models.ForeignKey(NavLink, related_name='dropdowns', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=255)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.parent.name} > {self.name}"
