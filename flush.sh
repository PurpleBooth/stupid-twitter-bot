#!/bin/bash

source $SECRETS_PATH

export TWITTER_CONSUMER_KEY
export TWITTER_CONSUMER_SECRET
export TWITTER_ACCESS_KEY
export TWITTER_TOKEN_SECRET

exec python flush.py