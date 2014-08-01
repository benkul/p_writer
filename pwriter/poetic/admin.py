from django.contrib import admin
from poetic.models import Poem, Line, SourceText


# Register your models here.
admin.site.register(Poem)
admin.site.register(Line)
admin.site.register(SourceText)

