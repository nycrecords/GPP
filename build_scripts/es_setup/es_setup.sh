#!/usr/bin/env bash
# 1. Install java
yum -y install java-1.8.0-openjdk

# 2. Download Elastic Search
wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-6.6.0.rpm -P /tmp

# 3. Install Elastic Search
rpm -ivh /tmp/elasticsearch-6.6.0.rpm

# 4. Autostart Elastic Search
sudo chkconfig --add elasticsearch

# 5. Configure Elastic Search
mv /etc/elasticsearch/elasticsearch.yml /etc/elasticsearch/elasticsearch.yml.orig
# TODO: make this sudoedit because symlink no longer works
cp /vagrant/build_scripts/es_setup/elasticsearch.yml /etc/elasticsearch/elasticsearch.yml

# Install nginx and create ssl certs if not running on a single server
if [ "$1" != single_server ]; then
    echo "complete complete complete COMPLETE"
    yum -y install rh-nginx18-nginx

    bash -c "printf '#\!/bin/bash\nsource /opt/rh/rh-nginx18/enable\n' > /etc/profile.d/nginx18.sh"

    mv /etc/opt/rh/rh-nginx18/nginx/nginx.conf /etc/opt/rh/rh-nginx18/nginx/nginx.conf.orig

    ln -s /vagrant/build_scripts/es_setup/nginx_conf/nginx.conf /etc/opt/rh/rh-nginx18/nginx/nginx.conf

    openssl req \
           -newkey rsa:4096 -nodes -keyout /vagrant/build_scripts/es_setup/elasticsearch_dev.key \
           -x509 -days 365 -out /vagrant/build_scripts/es_setup/elasticsearch_dev.crt -subj "/C=US/ST=New York/L=New York/O=NYC Department of Records and Information Services/OU=IT/CN=womensactivism.nyc"
    openssl x509 -in /vagrant/build_scripts/es_setup/elasticsearch_dev.crt -out /vagrant/build_scripts/es_setup/elasticsearch_dev.pem -outform PEM

    sudo service rh-nginx18-nginx restart
fi

mkdir -p /data/es_logs
chown -R vagrant:vagrant /data
chmod 777 -R /data

# 6. Start Elastic Search
sudo /etc/init.d/elasticsearch start