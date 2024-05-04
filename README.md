# Image_and_signature_detection_from_document-
## Prerequisites

- Python 3.8 or higher
- Django 3.2 or higher
- PostgreSQL 12 or higher

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/rahul4507/Image_and_signature_detection_from_document-.git
    ```

2. Navigate to the project directory:

    ```bash
    cd your_project_dir
    ```

3. Create a virtual environment:

    ```bash
    python -m venv env
    ```

4. Activate the virtual environment:

    On Windows:

    ```bash
    env\Scripts\activate
    ```

    On Unix or MacOS:

    ```bash
    source env/bin/activate
    ```

5. Install the requirements:

    ```bash
    pip install -r requirements.txt
    ```

## Database Setup

1. Install PostgreSQL and create a new database.

2. Update the `DATABASES` setting in `settings.py`:

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'yourdatabase',
            'USER': 'yourusername',
            'PASSWORD': 'yourpassword',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    ```

3. Run migrations:

    ```bash
    python manage.py migrate
    ```

## Running the Project

1. Start the Django development server:

    ```bash
    python manage.py runserver
    ```

2. Open your web browser and navigate to `http://localhost:8000`.

## Sample User Creds for checking

username = omkar
password = User@123
>>>>>>> master
