
### This project goes:

Dev on local branch -> PR on webui -> travis tests -> merge into master -> auto deployment on heroku

Followed [this] guide on setup.(https://medium.com/@felipeluizsoares/automatically-deploy-with-travis-ci-and-heroku-ddba1361647f)



### Tech Requirements

-  All packages listed in the requirements.txt
- `heroku config:set APP_SETTINGS=config.ProductionConfig` so that the config file is read in Production(Heroku)
- Environment vars sets on Travis = `APP_SETTINGS="config.DevelopmentConfig"`
- `travis encrypt $(heroku auth:token) -r cormon1976/u8s --add` to get and add the token for travis.
