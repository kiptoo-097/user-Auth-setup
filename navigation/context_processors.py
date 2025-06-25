from .models import NavLink

def navbar_links(request):
    navlinks = NavLink.objects.prefetch_related('dropdowns').all()
    return {'navlinks': navlinks}
