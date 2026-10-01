# Quiz 3 Django - Strawberry Matcha Student List

A beginner-friendly Django application demonstrating:

**Model → View → URL → Template**

## Design

The UI uses a strawberry-matcha palette inspired by the reference images:

- Strawberry: `#F9D1D9`
- Matcha: `#838F58`
- Cream background
- Rounded rectangular cards
- Soft coquette-inspired typography and heart/flower details

## Run locally

### 1. Create and activate a virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 2. Install Django

```bash
pip install -r requirements.txt
```

### 3. Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Load the sample students

```bash
python manage.py loaddata students
```

### 5. Run the server

```bash
python manage.py runserver
```

Open the local address shown in the terminal.

## Optional: Django Admin

Create an admin account:

```bash
python manage.py createsuperuser
```

Then visit:

`/admin/`

## Model → View → URL → Template flow

1. `main/models.py` defines the `Student` database model.
2. `main/views.py` gets the student records with `Student.objects.all()`.
3. `main/urls.py` connects the empty URL path to `views.home`.
4. `main/templates/main/home.html` displays the records using a Django template loop.
5. `static/css/style.css` controls the strawberry-matcha/coquette design.
