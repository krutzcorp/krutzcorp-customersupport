# Customer Support Service

## Setup

1. Install [Python 3.6](https://www.python.org/downloads/)
2. Install `virtualenv` using `pip`. Open a terminal and run `pip install virtualenv`.
3. Clone this repo and open a terminal in the repo's folder.
4. Create a new virtual environment by running `virtualenv venv`.
5. To activate the virtual environment, run:
    - OSX/Linux: `source venv/bin/activate`
    - Windows: `venv\Scripts\activate`
6. Install the requirements for the project with `pip install -r requirements.txt`.
7. Initialize the database:
    ```bash
    $ python
    >>> from customersupport.database import init_db
    >>> init_db()
    >>> exit()
    ```

## Running the Server

To run the server, activate the virtual environment then run `python run.py`

The site should be available at [http://127.0.0.1:5000](http://127.0.0.1:5000/).

## Updating the deployment server

- Unix:
`ssh root@vm343f.se.rit.edu 'bash -s' < deploy.sh`

- Windows Based:
`plink root@vm343f.se.rit.edu -m deploy.sh`
