import os

# ----------------------------------------------------------------------------------------------------------------------
# Fill database and create superuser
os.system(
    f"python manage.py loaddata product_data.json && "
    f"python manage.py loaddata contact_data.json && "
    f"python manage.py loaddata supplier_data.json && "
    f"python manage.py createsuperuser --noinput"
)
