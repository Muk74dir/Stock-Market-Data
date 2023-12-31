# Stock Market Data Visualization Project

This Django project focuses on visualizing stock market data using Chart.js. It includes functionalities to load data from JSON files, store it in a database, and display interactive charts on a web interface.

## Setup Project

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Muk74dir/Stock-Market-Data.git
    cd Stock-Market-Data
    ```

2. **Create a virtual environment and install dependencies:**

    ```bash
    python -m venv venv
    venv/Scripts/activate or source venv/bin/activate
    pip install -r requirements.txt
    ```

3. **Create a `.env` File**

4. **Add the following lines, replacing the placeholders with your actual values:**

    ```bash
    DB_NAME=your_database_name
    DB_USER=your_database_user
    DB_PASSWORD=your_database_password
    DB_HOST=your_database_host
    DB_PORT=your_database_port
    ```

5. **Update Django Project Settings**

    ```bash
    from decouple import config
    ```

    ```bash
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': config('DB_NAME'),
            'USER': config('DB_USER'),
            'PASSWORD': config('DB_PASSWORD'),
            'HOST': config('DB_HOST'),
            'PORT': config('DB_PORT'),
        }
    }
    ```


6. **Run Migration to connect with database**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

7. **Load the json file data in Database:**

    ```bash
    python manage.py load_json_data
    ```

8. **Run the server:**

    ```bash
    python manage.py runserver
    ```

## Access the Application
- Visit http://127.0.0.1:8000/ in your web browser to access the home page.

## Usage
- Navigate to the chart page to visualize stock market data for different trade codes. 
- Use the dropdown to select a specific trade code, and the charts will dynamically update.

### Contributing
- Contributions are welcome! Please open an issue or create a pull request for any improvements or bug fixes.
