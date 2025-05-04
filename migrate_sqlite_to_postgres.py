import os
import django
from django.apps import apps
from django.db import connections, router, transaction

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server.settings")
django.setup()

# Define source and destination database aliases
SQLITE_DB = "default"
POSTGRES_DB = "postgresql"


def migrate_all_data():
    models = apps.get_models()

    for model in models:
        if not model._meta.managed:
            continue  # skip unmanaged models

        print(f"Transferring model: {model.__name__}")

        try:
            source_qs = model.objects.using(SQLITE_DB).all()
            with transaction.atomic(using=POSTGRES_DB):
                for obj in source_qs:
                    obj.pk = obj.pk  # preserve PKs
                    obj.save(using=POSTGRES_DB, force_insert=True)
        except Exception as e:
            print(f"Error transferring {model.__name__}: {e}")

    print("✅ Migration complete.")


if __name__ == "__main__":
    migrate_all_data()
