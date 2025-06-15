from django.contrib import admin
from .models import Client, Message, Mailing, MailingAttempt

class ClientAdmin(admin.ModelAdmin):
    """Админка для клиентов рассылки."""
    list_display = ('email', 'full_name', 'owner')
    search_fields = ('email', 'full_name')
    list_filter = ('owner',)

class MessageAdmin(admin.ModelAdmin):
    """Админка для сообщений рассылки."""
    list_display = ('subject', 'owner')
    search_fields = ('subject',)
    list_filter = ('owner',)

class MailingAdmin(admin.ModelAdmin):
    """Админка для рассылок."""
    list_display = ('id', 'status', 'start_at', 'end_at', 'owner')
    search_fields = ('id',)
    list_filter = ('status', 'owner')

class MailingAttemptAdmin(admin.ModelAdmin):
    """Админка для попыток рассылки."""
    list_display = ('id', 'mailing', 'client', 'attempted_at', 'status', 'owner')
    search_fields = ('id', 'mailing__id', 'client__email')
    list_filter = ('status', 'owner')

admin.site.register(Client, ClientAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Mailing, MailingAdmin)
admin.site.register(MailingAttempt, MailingAttemptAdmin)
