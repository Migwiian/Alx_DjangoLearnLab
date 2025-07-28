# relationship_app/apps.py

from django.apps import AppConfig # This is the ONLY import that should be at the top level


class RelationshipAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'relationship_app'

    def ready(self):
        # This is the ONLY import that should be inside the ready method
        import relationship_app.signals