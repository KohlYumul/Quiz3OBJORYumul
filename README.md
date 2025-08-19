Installation
Clone the repository:

git clone https://github.com/KohlYumul/Quiz3OBJORYumul

cd Quiz3OBJORYumul

Create and activate a virtual environment:

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
venv\Scripts\activate
Install the required packages:

pip install -r requirements.txt

A sample requirements.txt would look like this:

Django==5.2.5
Pillow==10.4.0
Download and set up Bootstrap:
Download the compiled CSS and JS files from the official Bootstrap website. Place bootstrap.min.css in a static/css/ directory and bootstrap.bundle.min.js in a static/js/ directory within your project root.

Run database migrations:

python manage.py makemigrations
python manage.py migrate

Create a superuser:

python manage.py createsuperuser
Follow the prompts to create an admin account.

Run the development server:

python manage.py runserver

Note that if there is a conflicting server, you can insert a different 4 digit number

Example:

python manage.py runserver 9321

Usage

Admin Panel: Navigate to http://127.0.0.1:8000/admin/ and log in with the superuser account. You can add new job openings here.

User Registration: Access http://127.0.0.1:8000/register/ to create a new user account. Note that emails must end with @objor.com.

Job Listings: The main page at http://127.0.0.1:8000/ displays a list of all job openings. Use the search bar to filter listings.

Job Details: Click on a job title to view its details.

Admin View: If logged in as an admin, you will see a table of all applicants and buttons to edit or delete the job.

Regular User View: If logged in as a non-admin, you will see the job details and a form to upload your resume and apply.




