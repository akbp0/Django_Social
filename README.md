# Django Social Network Project

This Django project is a specialized and precisely designed virtual social network with the following features:

1. **Post Management**
   - Creating new posts
   - Updating existing posts
   - Deleting posts
   - Viewing posts

2. **Post Content**
   - Posts can include both text and images.

3. **User Profiles**
   - Each user has a profile picture.

4. **Nested Comments**
   - Users can leave threaded comments on posts.

5. **Search**
   - Searching functionality that allows users to search for posts and other users.

6. **Password Recovery**
   - Users can recover their passwords by email verification.

7. **Email Verification**
   - Email addresses are validated using a verification code.

8. **Direct Messaging**
   - Users can send direct messages to each other.

9. **Comprehensive Testing**
   - The entire project has been thoroughly tested to ensure high quality and reliability.

And more...

## File Structure

The project's file structure follows Django conventions and includes the following files and directories:

- manage.py: Django's command-line utility for various project management tasks.
- requirements.txt: A file containing all the required Python dependencies for the project.
- virtual_social_network/: A directory containing the project's main Django application.
  - settings.py: The main settings file for the Django project.
  - urls.py: The URL configuration file that maps URLs to specific views.
  - models.py: Contains the database models for the project.
  - views.py: Contains the views for rendering the templates and handling user requests.
  - forms.py: Includes the forms used for data validation and rendering in templates.
  - templates/: A directory containing the HTML templates for the project.
  - static/: A directory for storing static files such as CSS, JavaScript, and images.

## Getting Started

To get started with this project, follow these steps:

1. Clone the repository:
``` bash
git clone https://github.com/your-username/virtual-social-network.git
```

2. Install the required dependencies:
``` python
pip install -r requirements.txt
 ```

3. Configure the database settings in settings.py.

4. Apply database migrations:
 ```python
 python manage.py migrate
   ```

6. Run the test suite to ensure the project is functioning correctly:
``` python
python manage.py test
```
   
   

7. Start the development server:
``` python
python manage.py runserver
```
   

8. Open your web browser and visit http://localhost:8000 to access the application.

## Contributing

If you would like to contribute to this project, please follow these guidelines:

1. Fork the repository and create a new branch.
2. Implement your feature or bug fix.
3. Write clear and concise commit messages.
4. Test your changes thoroughly and ensure all tests pass.
5. Submit a pull request, describing the changes and their purpose.
