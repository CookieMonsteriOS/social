# Social API

Social is a simple API for managing users in a database. It allows you to retrieve all users and add new users to the database using HTTP requests.

## Installation

To set up the Social API, follow these steps:

1. Clone the repository:
   ```
   git clone 
   cd social
   ```

2. Install the required dependencies using pip:
   ```
   pip install -r requirements.txt
   ```

## Usage

### Retrieving All Users

To retrieve all users from the database, send a GET request to the `/users` endpoint.

Example:
```
curl http://localhost:5000/users
```

### Adding a New User

To add a new user to the database, send a POST request to the `/adduser` endpoint with the user's name and email in the request body.

Example:
```
curl -X POST -H "Content-Type: application/json" -d '{"name": "John Doe", "email": "john@example.com"}' http://localhost:5000/adduser
```

## Database Schema

The database schema is defined in the `setup/schema.sql` file. It includes the following tables:

- `Users`: Stores information about users, including their ID, name, and email.

## Contributing

If you'd like to contribute to the Social API project, please fork the repository and submit a pull request. We welcome contributions of all kinds, including bug fixes, feature enhancements, and documentation improvements.

## License

This project is licensed under the [MIT License](LICENSE).
