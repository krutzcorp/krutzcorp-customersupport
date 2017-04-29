cd /var/www/krutzcorp-customersupport
echo "pull master"
git pull origin master
echo "installing requirements"
source venv/bin/activate
pip install -r requirements/prod.txt
echo "initializing db"
python3 init_db.py
echo "restarting app"
sudo service krutzcorp-customersupport restart
echo "restarting nginx"
sudo service nginx restart
echo "done"
