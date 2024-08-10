# TodoApp Web Project

This project is a simple To-Do app built with Django, designed to track and manage tasks as part of my Django learning process.

## Project Overview

The TodoApp is a basic web application for managing to-do tasks. It allows users to create, view, update, and delete tasks. The app is intended to help me learn and understand the core concepts of Django, including models, views, templates, and form handling.

## Features

- **Task Creation**: Add new tasks with a title and description.
- **Task List**: View a list of all tasks.
- **Task Update**: Edit existing tasks.
- **Task Deletion**: Remove tasks from the list.
- **Task Status**: Mark tasks as completed or pending.

## Installation

To run this project locally, follow these steps:

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/todoapp-web-project.git
    ```

2. **Navigate to the project directory**:

    ```bash
    cd todoapp-web-project
    ```

3. **Create a virtual environment**:

    ```bash
    python -m venv env
    ```

4. **Activate the virtual environment**:

    - On Windows:

      ```bash
      .\env\Scripts\activate
      ```

    - On macOS/Linux:

      ```bash
      source env/bin/activate
      ```

5. **Install the required packages**:

    ```bash
    pip install -r requirements.txt
    ```

6. **Apply database migrations**:

    ```bash
    python manage.py migrate
    ```

7. **Run the development server**:

    ```bash
    python manage.py runserver
    ```

8. **Open your browser and go to**: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Usage

- **Home Page**: Displays a list of all tasks with options to add, edit, or delete tasks.
- **Add Task**: Click the "Add Task" button to create a new task.
- **Edit Task**: Click on a task to update its details.
- **Delete Task**: Click the delete icon next to a task to remove it.

## Project Structure

- `todo/`: Contains the Django application code.
  - `migrations/`: Database migrations.
  - `__init__.py`: Initializes the app.
  - `admin.py`: Admin interface configuration.
  - `apps.py`: Application-specific configurations.
  - `models.py`: Defines the data models.
  - `tests.py`: Test cases for the app.
  - `urls.py`: URL routing for the app.
  - `views.py`: Defines the views and logic.

- `todoappdjango/`: Contains the Django project settings and configuration.
  - `__init__.py`: Initializes the project.
  - `settings.py`: Project settings.
  - `urls.py`: URL routing for the project.
  - `wsgi.py`: WSGI application entry point.

- `manage.py`: Command-line utility for administrative tasks.

## Contributing

Feel free to fork the repository, make changes, and submit a pull request. Contributions are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to the Django documentation and community for providing the resources and support for learning Django.
