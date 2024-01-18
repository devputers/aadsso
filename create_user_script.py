# create_user_script.py
from aadsso_app.models import Client, Domain
from django.contrib.auth.models import User
from django_tenants.utils import schema_context

# Assuming 'login1' schema is already created
tenant_login1 = Client.objects.get(schema_name='login1')

# Switch to 'login1' schema context
with schema_context('login1'):
    # Create a user for 'login1' schema
    user_login1 = User.objects.create(username='username_login1', password='password_login1')

# Switch back to the default schema context (optional)
tenant_login1.deactivate()
