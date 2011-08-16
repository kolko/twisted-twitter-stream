#!/usr/bin/env python
# coding: utf-8

import TwistedTwitterStream
from twisted.internet import reactor
import oauth

class consumer(TwistedTwitterStream.TweetReceiver):
    def connectionMade(self):
        print "connected..."

    def connectionFailed(self, why):
        print "cannot connect:", why
        reactor.stop()

    def tweetReceived(self, tweet):
        print "new tweet:", repr(tweet)

if __name__ == "__main__":
    #TwistedTwitterStream.firehose("username", "password", consumer())
    #TwistedTwitterStream.retweet("username", "password", consumer())
    OAconsumer = oauth.OAuthConsumer('uu', 'bb')
    token = oauth.OAuthToken('xx', 'zz')
    TwistedTwitterStream.sample("username", "password", consumer(), OAconsumer=OAconsumer, token=token)
    reactor.run()
