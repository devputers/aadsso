# # create_user_script.py
# from aadsso_app.models import Client, Domain
# from django.contrib.auth.models import User
# from django_tenants.utils import schema_context

# # Assuming 'login1' schema is already created
# tenant_login1 = Client.objects.get(schema_name='login1')

# # Switch to 'login1' schema context
# with schema_context('login1'):
#     # Create a user for 'login1' schema
#     user_login1 = User.objects.create(username='username_login1', password='password_login1')

# # Switch back to the default schema context (optional)
# tenant_login1.deactivate()

# myscript.py

import os
from django_tenants.utils import schema_context
from webUI.models import CustomUser, CustomGroup
from aadsso_app.models import Client
from django.db import connection, transaction

def create_user_and_group():
    # Replace 'your-tenant-domain.com' and 'your_tenant_schema_name' with actual values
    # tenant = Client(domain_url='your-tenant-domain.com', schema_name='your_tenant_schema_name')
    # tenant.save()

    # Switch to the tenant's context
    with schema_context('login1'):
        # Create a custom user
        user = CustomUser.objects.create(username='example_user', email='user@example.com', password='password')

        # Create a custom group
        group = CustomGroup.objects.create(name='example_group')

        # Add the user to the group
        user.groups.add(group)

    # Save changes
    transaction.commit()

create_user_and_group()
