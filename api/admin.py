from django.contrib import admin
from api.models import Ticket
from api.models import Comment


admin.site.register(Ticket)
admin.site.register(Comment)
