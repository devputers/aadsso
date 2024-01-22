Setting Up a Virtual Environment

Prerequisites

- **OS**: Ubuntu 22.04
  - To check your version: lsb_release -a
  
- **Python**: Version 3.10.12
  - To verify your version: python3 -V or python3 --version

- **Postgres**: Version 14.10
  - To verify your version: psql --version
  - To check postgresql running : systemctl status postgresql

Setup Instructions

1. Clone this repository and switch to the relevant branch.

2. Create a virtual environment:

    ```bash
    python3 -m venv _aadsso
    ```

3. Activate the virtual environment:
    
    ```bash
    source _aadsso/bin/activate
    ```

4. Install the dependencies:

    ```bash
    pip install -r reqs.txt
    ```

## Database Default sqlite3
Create a Database
```bash
python manage.py makemigrations
python manage.py migrate_schemas
```

### Configure/Create Postgres Database

To install postgres database
    ```python
    sudo apt update
    sudo apt install postgresql postgresql-contrib
    ```

1. To start postgres database/ service :
    ```python
    sudo service postgresql start    
    ```
2. Enter psql shell
    ```python
    sudo -u postgres psql    
    ```
3. Type the following code in the opened shell [ for create User and database ]:

    ```bash
    CREATE USER username WITH PASSWORD 'user_password';  #(if not created)
    CREATE DATABASE aadsso_db;
    GRANT ALL PRIVILEGES ON DATABASE aadsso_db TO username;
        # ALTER ROLE username SET client_encoding TO 'utf8';
        # ALTER ROLE username SET default_transaction_isolation TO 'read committed';  
    ```

### For Public Database / Schemas and Defaul User , and Groups
 
1. Open a Python shell:

    ```bash
    python manage.py shell
    ```

2. Type the following code in the opened shell:

    ```python
    from django.contrib.auth.models import Group, Permission
    new_group = Group(name="mssso")
    new_group.save()

    # Add Users to Django Groups:
    from django.contrib.auth.models import User, Group
    user = User.objects.create_user(username="ramxyz@example.com", password="98765")
    group = Group.objects.get(name="mssso")
    user.groups.add(group)
    user.save()
      ```

    ```python
    # Create nomssso Groups in the opened shell:
    from django.contrib.auth.models import Group, Permission
    new_group = Group(name="nomssso")
    new_group.save()

    from django.contrib.auth.models import User, Group
    alice = User.objects.create_user(username="alice@example.com", password="333")
    alice.save()

    bob = User.objects.create_user(username="bob@example.com", password="515151")
    bob.save()

    nomssso_group = Group.objects.get(name="nomssso")
    nomssso_group.user_set.add(alice, bob)
    nomssso_group.save()
    ```

3. Exit the shell.
    ```python
    exit()
    ```
4. After configuring the necessary folders and configuration files, run:

    ```bash
    python manage.py runserver 0.0.0.0:8080
    ```
    - access in browser localhost:8080

5. Use the provided email and password to log in. 

### Applying Database Migrations

1. Run makemigrations to create migration files:
    
    ```bash
    python manage.py makemigrations
    ```
2. Apply migrations to update the database:
    
    ```bash
    python manage.py migrate_schemas
    ```

- make sure only use migrate_schemas when working with postgres database for multi tenant

## For Schemas / Database Postgres Create Tenant / schemas and Custom User, Group

1. Open a Python shell:

    ```bash
    python manage.py shell
    ```

2. Type the following code in the opened shell [ for create schemas ]:

    ```python
    from aadsso_app.models import Client, Domain

    # Create public tenant in the opened shell:
    tenant = Client(schema_name="public", name="Public")
    tenant.save()
    domain = Domain(domain="localhost", tenant=tenant, is_primary=True)
    domain.save()

    # Create login1 tenant in the opened shell:

    tenant = Client(schema_name="login1", name="login one")
    tenant.save()
    domain = Domain(domain="login1.localhost", tenant=tenant, is_primary=True)
    domain.save()

    # Create login2 tenant in the opened shell:

    tenant = Client(schema_name="login2", name="login two")
    tenant.save()
    domain = Domain(domain="login2.localhost", tenant=tenant, is_primary=True)
    domain.save()
    ```

3. Type the following code in the opened shell [ for create User for schemas eg. login1 ]:

    ```python
    # Create user tenant1 in the opened shell:

    # Assuming you have the User model and the 'login1' schema already created
    # Switch to the 'login1' schema context
    from aadsso_app.models import Client, Domain
    from webUI import User
    
    login1 = Client.objects.get(schema_name='login1')
    domain = Domain.objects.get(tenant=login1, is_primary=True)

    # Activate the 'login1' schema
    login1.activate()

    # Create a user in the 'login1' schema
    user = User.objects.create(username='your_username', password='your_password')

    # After adding data, switch back to the default schema context (optional)
    tenant.deactivate()

    # To verify that the user was created in the 'login1' schema
    user_in_login1 = User.objects.using('login1').get(username='your_username')

    ```

4. Type the following code in the opened shell [ for create Groups and User, Groups for schemas eg. login1 ]:

    ```python
    # Create user tenant1 in the opened shell:

    # Assuming you have the User model and the 'login1' schema already created
    # Switch to the 'login1' schema context
    from aadsso_app.models import Client, Domain
    from webUI.models import User, Group, User_Groups
    
    login1 = Client.objects.get(schema_name='login1')
    domain = Domain.objects.get(tenant=login1, is_primary=True)

    # Activate the 'login1' schema
    login1.activate()

    # Create a user in the 'login1' schema
    # Create User instances
    user1 = User.objects.create(username='user1', password='password1')
    user2 = User.objects.create(username='user2', password='password2')

    # Create Group instances
    group1 = Group.objects.create(name='mssso')
    group2 = Group.objects.create(name='nomssso')

    # Create User_Groups instances (associating users with groups)
    User_Groups.objects.create(user=user1, group=group1)
    User_Groups.objects.create(user=user1, group=group2)
    User_Groups.objects.create(user=user2, group=group2)

    # After adding data, switch back to the default schema context (optional)
    tenant.deactivate()

    # To verify that the user was created in the 'login1' schema
    user_in_login1 = User.objects.using('login1').get(username='your_username')

    ```

    - **note** also able to add above data using admin login 

4. Exit the shell.
    ```python
    exit() or Ctrl+D to exit
    ```

5. After configuring the necessary folders and configuration files, run:

    ```bash
    python manage.py runserver 0.0.0.0:8080
    ```

6. Use the provided email and password to log in. 

### Applying Database Migrations

1. Run makemigrations to create migration files:
    
    ```bash
    python manage.py makemigrations
    ```

2. Apply migrations to update the database:
    
    ```bash
    python manage.py migrate_schemas
    ```
