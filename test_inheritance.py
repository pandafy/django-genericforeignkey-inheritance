import os

import django
from django.apps import apps

# Set up Django environment
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "generickeytest.settings"
)  # Replace with your project name
django.setup()


def check_field_existence(model_name, field_name):
    model = apps.get_model("myapp", model_name)  # Replace with your app name
    has_field = field_name in [f.name for f in model._meta.get_fields()]
    return has_field


if __name__ == "__main__":
    model_name = "ConcreteEntity"
    field_name = "related_object"
    related_object = check_field_existence(model_name, field_name)
    print(f"'{field_name}' exists in {model_name}: {related_object}")
    description = check_field_existence(model_name, "description")
    print(f"'description' exists in {model_name}: {description}")
