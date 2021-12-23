from django.db import models
# from django.contrib.auth.models import User

class TicketStatus(models.TextChoices):
    TO_DO = 'To Do'
    IN_PROGRESS = 'In Progress'
    IN_REVIEW = 'In Review'
    DONE = 'Done'

class Ticket(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField(blank=True, default='')
    owner = models.ForeignKey('auth.User', related_name='ticketss', on_delete=models.CASCADE)
    # assignee = models.ForeignKey(User, null=True, blank = True, on_delete=models.CASCADE)
    status = models.CharField(max_length=25, choices=TicketStatus.choices, default=TicketStatus.TO_DO)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.title


class Comment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=False)
    status = models.CharField(max_length=25, choices=TicketStatus.choices, default=TicketStatus.TO_DO)
    owner = models.ForeignKey('auth.User', related_name='comments', on_delete=models.CASCADE)
    ticket = models.ForeignKey('Ticket', related_name='comments', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.description