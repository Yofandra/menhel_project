from django.core.management.base import BaseCommand
from app.models import User

class Command(BaseCommand):
    help = 'Seed database with initial data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding data...')

        if not User.objects.filter(username='admin').exists():
            User.objects.create_user(
                username='admin',
                password='admin',
                role='admin', 
                is_superuser=True 
            )
            self.stdout.write(self.style.SUCCESS('Superuser created successfully!'))
        else:
            self.stdout.write(self.style.WARNING('Superuser already exists.'))

        self.stdout.write(self.style.SUCCESS('Data seeded successfully!'))
