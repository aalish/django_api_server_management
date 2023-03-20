# Django SSH API
This is a Django application that provides an API for executing scripts on remote servers using SSH. The API takes a token and other parameters such as server name and then connects to the specified server over SSH, executes the script, and returns the output and error messages as a JSON response.

## Requirements
To run this application, you will need:

* Python 3.x
* Django 3.x
* Paramiko
* json
You can install Django and Paramiko using pip:


`pip install django paramiko json`

# Usage
To use this application, follow these steps:

* Clone this repository to your local machine.
* Open a terminal and navigate to the directory where you cloned the repository.
* Start the Django development server using the following command:

`python manage.py runserver`

Use an HTTP client (e.g., curl, Postman, or a web browser) to send a GET request to the /execute-script endpoint with the following parameters:
token: The API token (you can change this to a more secure authentication method).
server_name: The name or IP address of the server you want to connect to.

## For example:

`http://localhost:8000/execute-script?token=YOUR_TOKEN&server_name=YOUR_SERVER_NAME` 

The API will execute the script on the remote server and return the output and error messages as a JSON response.
Security Considerations
This application has several security considerations that you should keep in mind:

* The API token is currently stored as a hard-coded string in the execute_script view function. You should use a more secure authentication method (e.g., OAuth, JWT) if you plan to deploy this application to a production environment.

* The remote server should be properly secured to prevent unauthorized access.

