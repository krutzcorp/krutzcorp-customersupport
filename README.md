# Customer Support Service

## Setup

1. Install [Python 3.6](https://www.python.org/downloads/)
2. Install `virtualenv` using `pip`. Open a terminal and run `pip install virtualenv`.
3. Clone this repo and open a terminal in the repo's folder.
4. Create a new virtual environment by running `virtualenv venv`.
5. To activate the virtual environment, run:
    - OSX/Linux: `source venv/bin/activate`
    - Windows: `venv\Scripts\activate`
6. Install the requirements for the project with `pip install -r requirements/dev.txt`.
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

# Production

## Setting up the deployment server

We followed the [Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uwsgi-and-nginx-on-ubuntu-14-04) instructions for building Flask apps with NGINX. We've provided two files to make the process easier.

Move `nginx_files/krutzcorp-customersupport` into `/etc/nginx/sites-available/`.
Move `nginx_files/krutzcorp-customersupport.conf` into `etc/init/`.

move 

## Updating the deployment server

- Unix:
`ssh root@vm343f.se.rit.edu 'bash -s' < deploy.sh`

- Windows Based:
`plink root@vm343f.se.rit.edu -m deploy.sh`

### Deploying a migration

- To deploy migrations replace `deploy.sh` with `deploy_with_migrations.sh`

## Restarting the deployment server

- Unix:
`ssh root@vm343f.se.rit.edu 'bash -s' < restart.sh`

- Windows Based:
`plink root@vm343f.se.rit.edu -m restart.sh`

## Debugging the server

Nginx logs can be found in `/var/log/nginx`

Flask logs can be found in `/var/log/uwsgi`

## Testing

### Functional Tests

To run the functional tests, ensure that a local server is running. Then run:
```
python functional_tests.py
```
