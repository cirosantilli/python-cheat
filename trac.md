# Trac

Top Python written bug tracker.

Not written in Django unfortunately.

Dependency:

    sudo aptitude install -y python-mysqldb

Install:

    sudo pip install trac

## Prerequisites

Learn how to use <#apache> if you ever want to do serious deployment.

## Create project

create db to use:

    mysql -u root -p -e 'create database trac_test character set utf8'

**MUST BE UTF8!!!**

make a directory and install there:
    d="test"
    mkdir "$d"
    trac-admin "$d" initenv

enter:

    test
    mysql://user:pass@host:3306/dbname
                         ^^^^        
                         default mysql port

##test server

    tracd --port 8000 /path/to/project
    firefox localhost:8000

##apache deployment

For real deployment, can be much faster.

###access rights

the server process must have ownership of the project dir

by default, the owner of the dir is the owner who run ``trac-admin``

however, usually apache runs as a different user.

to find out the user:

    cat ps -Af | grep apache

to find out his group:

    groups $username

finally, change ownership:

    chown -R $username.$groupname "$d"

on Ubuntu at the time of writing the default was:

    username=www-data
    groupname=www-data

###Authentication

Trac uses <#http authentication> and cookies.

you have to set http authentication to the (virtual) location ``/trac/projectname/login``.

when an user hits this URL authenticated, Trac sends session cookies back to him.

to create an admin user, choose the `htpasswd` user you want to promote to admin,
and do:
    
    trac-admin "$project_dir" permission add "$admin_username" TRAC_ADMIN

where ``"$admin_username"`` is exactly one of the `htpasswd` users.

###fastgci

Install fastgci.

    FastCgiConfig -initial-env TRAC_ENV_PARENT_DIR=/usr/share/trac/projects/

`TRAC_ENV_PARENT_DIR` is the parent of all Trac projects.

###automated

this section automates full project creation and setup

it uses:
- multiple projects on a dir
- http basic authentication with cookies
- shared authentication for all projects

add to apache config:

inputs:

    root="/usr/share/trac/"
    projects_dir="$root/projects"
    server_user=www-data
    server_group=www-data
    deploy_dir=/tmp/trac_deploy/
    db_user=trac
    db_pass=asdf
    db_host=localhost
    project_name=test3
    project_dir="$projects_dir/$project_name"
    db=trac_$project_name
    passwd_file="$root/passwd"
    admin_username="admin"

first time:

    sudo mkdir -p "$projects_dir" "$deploy_dir"
    sudo chown $u.$g "$project_dir" "$deploy_dir"
    mysql -u root -p -e "CREATE USER $db_user@$db_host IDENTIFIED BY $db_pass;"
    htpasswd -c "$passwd_file" "$admin_username"

new project:

    mysql -u root -p -e "create database $db character set utf8; grant all on $db.* to $db_user@localhost;"
    sudo -u $u mkdir -p "$project_dir"
    echo -e "$project_name\nmysql://$db_user:$db_pass@localhost:3306/$db" | sudo -u $u trac-admin "$project_dir" initenv
    trac-admin "$project_dir" permission add "$admin_username" TRAC_ADMIN

first time after first new project:

    sudo -u $u trac-admin "$r" deploy "$d"
    sudo mv "$deploy_dir"/* "$root"
    sudo rmdir "$deploy_dir"
