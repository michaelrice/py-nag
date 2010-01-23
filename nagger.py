#!/usr/bin/env python

__author__ = "Michael Rice"
__version__ = "0.2"
__date__ = "2010-01-23"
__license__ = "Apache2"

import twitter,sys
from optparse import OptionParser

class nagger:
  def __init__(self,uname="test",passwd="test"):
      self.user = uname
      self.passwd = passwd
      self.connect = twitter.Api(username=self.user,password=self.passwd)
  
  def inform(self,user,msg):
      '''Methos to send direct message to a list of users about foo'''
      if len(msg) <= 0 or len(msg) >= 141:
          return False
      self.connect.PostDirectMessage(user, msg)

  def tweetit(self,msg):
      '''Method to just tweet the nagios status'''
      if len(msg) <= 0 or len(msg) >= 141:
          return False
      self.connect.PostUpdate(msg)

def main():
    usage = "usage: %prog [options]"
    version="%prog .02"
    parser = OptionParser()
    parser.add_option('-u', '--user', action="store", dest="user",
        help="Set the user name for the twitter account who will get the message")
    parser.add_option('-t', '--twitusr', action="store",dest="twitusr",
        help="Twitter account to auth as. Default is to use values in the config file")
    parser.add_option("-p", "--twitpass",dest="twitpass",help="Password for Twitter user")
    parser.add_option('-T','--tweetit',action="store_true",dest="tweetit",
        help="Use this option to post to the users status. Do not use with -d or --dmonly")
    parser.add_option("-d","--dmonly",action="store_false", dest="tweetit",
        help="Use this option to direct message a user. Must be used with -u or --user")
    parser.add_option("-m","--msg",dest="msg",help="140 char max len message to be sent to twitter")
    (options, args) = parser.parse_args()
    twitcon = nagger(options.twitusr,options.twitpass)
    if not options.tweetit and options.user:
        twitcon.inform(options.user,options.msg)
    elif options.tweetit:
        twitcon.tweetit(options.msg)
    else:
        print "You are missing some options. Try the -h flag for help"
        sys.exit(2)

if __name__ == "__main__":
    main()
