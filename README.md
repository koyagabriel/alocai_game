# Alocal Games
A service which will return a combination of games with the highest possible
total value for the given pen-drive space

## Development
* [Flask](http://flask.pocoo.org/) - Flask is a BCD licensed microframework for Python based on Werkzeug and Jinja 2.
* [Python-dotenv](https://github.com/theskumar/python-dotenv) - This library allows the saving of environment variables in .env and loaded when the application runs.
* [SQLAlchemy](https://www.fullstackpython.com/sqlalchemy.html) - This library is a Python distribution containing tools for working with sql databases.

## Installation
#### In Docker Environment
1. Start up your terminal (or Command Prompt on Windows OS).
2. Clone the repository by entering the command `git@github.com:koyagabriel/alocai_game.git` in the terminal.
3. Create a `.env` file in your root directory as described in `.env.example` file and configure the necessary options. It is essential you create this file before running the application.
4. Build a docker image by running the command `docke-compose up`
5. Enter into the python container and setup up your database following these steps: 
    * `python manage.py db init`
    * `python manage.py db migrate`
    * `python manage.py db upgrade`


#### Outside Docker Environment
1. Start up your terminal (or Command Prompt on Windows OS).
2. Ensure that you've `python 3` installed on your PC.
3. Clone the repository by entering the command `git@github.com:koyagabriel/alocai_game.git` in the terminal.
4. Create a `.env` file in your root directory as described in `.env.example` file and configure the necessary options. It is essential you create this file before running the application.
5. Install requirements by running the command `pip3 install -r requirements.txt`
6. Setup up your database following these steps: 
    * `python manage.py db init`
    * `python manage.py db migrate`
    * `python manage.py db upgrade`
7. Start local server by running the command.
   `bash server.sh`

### API Resource Endpoints
URL Prefix = Base URL is `http://localhost:5000/api/v1` on your local system.


| EndPoint                                                       | Functionality                                                                                |                     Sample Parameters                     |
| -------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | :-------------------------------------------------------: |
| **GET** `/index`                                               | Gets index page                                                                              |                                                           |
| **GET** `/status`                                              | Gets state of database connection                                                            |
| **GET** `/docs`                                                | Get api docs                                                                                 |                                                           |
| **POST** `/games`                                              | Post a game                                                                                  | `{"name": "sample", "price": 71.7,  "space": 1073741824}` |
| **GET** `/best_value_games?pen_drive_space={POSITIVE_INTEGER}` | Fetches a combination with the highest possible total value that fits given pen-drive space. |                                                           |

## Authors

**Koya Gabriel.**
