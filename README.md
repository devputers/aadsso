Setting Up a Virtual Environment

Prerequisites

- **OS**: Ubuntu 22.04
  - To check your version: lsb_release -a
  
- **Python**: Version 3.10.12
  - To verify your version: python3 -V or python3 --version

Setup Instructions

1. Clone this repository and switch to the relevant branch.

2. Create a virtual environment:

    
bash
    python3 -m venv _aadsso


3. Activate the virtual environment:

    
bash
    source _aadsso/bin/activate


4. Install the dependencies:

    
bash
    pip install -r requirements.txt



## Database
Create a Database
```bash
python manage.py migrate
```
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

5. Use the provided email and password to log in. 

### Applying Database Migrations
1. Run makemigrations to create migration files:
    
    ```bash
    python manage.py makemigrations
    ```
2. Apply migrations to update the database:
    
    ```bash
    python manage.py migrate
    ```
