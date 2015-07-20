# Stupid twitter bot

Just tweets the wordlist

```shell
heroku create
heroku config:set TWITTER_CONSUMER_KEY=xxx
heroku config:set TWITTER_CONSUMER_SECRET=xxx
heroku config:set TWITTER_ACCESS_KEY=999-xxx
heroku config:set TWITTER_TOKEN_SECRET=xxx
heroku addons:create redistogo
```

Then enable the worker dyno.

```shell
git push heroku master
```
 
It won't clear the list if you just push it again.

To clear ths list run this

```shell
heroku run python flush.py
```

