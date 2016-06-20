from .models import Elder, Family

john, created = Elder.objects.get_or_create(
    name='john', 
    defaults={'age': 60}
)

kelly, created = Family.objects.get_or_create(
    name='kelly',
    defaults={'line':"u2ef38a8c1f3f1c2c63bdf9c0a629023c", 'elder':john}
)


lily, created = Family.objects.get_or_create(
    name='lily',
    defaults={'line': "ue750be100842de87bf21da1b5717cc35", 'elder':john}
)

print Family.objects.all()
