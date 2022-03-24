## Installation steps for News Api:
1. Running the docker using below command
`docker-compose up --build` for first use it will install all
dependencies and create docker container for this project
2. After running above command you can run just `docker-compose up`
3. You can just use this command to use backup db 
`cat dump.sql | docker exec -i news_db_1 psql -U postgres
`
4. Default user *username: admin* ||
*password: 12345* in order to enter the admin panel.
5. You can also run this command to change ownership
`sudo chown -R $USER:$USER .`


### This is the link for github: 
[Github](git@github.com:ShamsiddinToshmirzaev/News-Api.git)


### This is the link for heroku:
[Heroku](https://link-url-here.org)

### This is the link for postman documentation
[Postman](https://documenter.getpostman.com/view/10331149/UVsTphSs)