# Stupid twitter bot

This is a really simple twitter bot that will simply tweet a message every hour from a word list. It will be a random word from the word list.

## Getting Started

These instructions will tell you get this bot up and running on Heroku.

### Prerequisities

#### Heroku

You'll need a [Heroku account](https://dashboard.heroku.com), and to have checked with repository out, updated the `wordlist.txt` with your words and committed it.

Install the [Heroku toolbelt](https://toolbelt.heroku.com) too, and login to it.

#### Bot Access Tokens for Twitter

You'll also need a twitter account you want to use for a bot, and to [create an application](https://apps.twitter.com/app/new) with an access token via twitters web interface.

### Installing

First start your server.

Remember to fill in your twitter keys in the config variables before running the commands.

```shell
heroku create
heroku config:set TWITTER_CONSUMER_KEY=xxx
heroku config:set TWITTER_CONSUMER_SECRET=xxx
heroku config:set TWITTER_ACCESS_KEY=999-xxx
heroku config:set TWITTER_TOKEN_SECRET=xxx
heroku addons:create redistogo
```

You'll then need to login to Heroku and change your server to have the worker enabled. Go to the server you just created with the above command, click edit to the right of "traditional dynos" and click the switch next to the worker and press save.
 
Then start your worker with your code running on it.

```shell
git push heroku master
```
 
The list will stay persisted between multiple updates. It won't update.
To clear the list of tweets run.

```shell
heroku run python flush.py
```

Then run 
```shell
heroku ps:restart worker.1
```

to repopulate the list.

## Built With

* [python-twitter](https://github.com/bear/python-twitter) - To send the tweets   
* [redis-py](https://github.com/andymccurdy/redis-py) - As a persistent queue to store the tweets   
* [Heroku](https://heroku.com) - Somewhere to host it for free

## Contributing

Feel free to submit pull requests and issues. If it's a particularly large PR, you may wish to discuss it in an issue first.

Please note that this project is released with a [Contributor Code of Conduct](https://github.com/PurpleBooth/stupid-twitter-bot/blob/master/code_of_conduct.md). By participating in this project you agree to abide by its terms.

## Versioning

We use [SemVer](http://semver.io/) for the version tags available See the tags on this repository. 

## Authors

**Billie Thompson** - *Developer* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/PurpleBooth/stupid-twitter-bot/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/PurpleBooth/stupid-twitter-bot/blob/master/LICENSE.md) file for details.

## Acknowledgments

* I think the [Every Witch Word bot](https://twitter.com/everywitchword) is cool, so I wrote this library to steal their idea.
* Mispy did this idea first and better, except with an [markov chains ebook bot](https://github.com/mispy/twitter_ebooks).
