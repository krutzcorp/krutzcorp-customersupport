cd /var/www/krutzcorp-customersupport
echo "pull master"
git pull origin master
echo "restarting app"
sudo service krutzcorp-customersupport restart
echo "restarting nginx"
sudo service nginx restart
echo "done"
