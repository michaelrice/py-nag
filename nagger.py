#!/usr/bin/env python
"""Nagger to use with Nagios to notify via Twitter

Usage: nagger [options]

Required Options:
    if:
      --dmonly                    This is used to only direct message the list of users
                                  Can not be used with --tweetit
      --users=...                 Comma seperated list of twitter
                                  bob,tim,jack
    if:
      --tweetit                   This will just post the msg to your timeline for all followers to see
                                  This option can not be used with --dmonly
    --msg=...                     This should be in the form: --msg="my message goes here"
                                  This message can not be empty, or > 140 Chars (strict)
                                  This app will not wrap your post to make multiple tweets
    --twitusr=...                 Username of twitter user
    --twitpass=...                Password for the twitter account
"""
__author__ = "Michael Rice"
__version__ = "0.1"
__date__ = "2010-01-22"
__license__ = "Apache"



import twitter
import getopt
import os
import sys

class nagger:

  def __init__(self,uname="test",passwd="test"):
      self.user = uname
      self.passwd = passwd
      self.connect = twitter.Api(username=self.user,password=self.passwd)
  
  def inform(self,users,msg):
      '''Methos to send direct message to a list of users about foo'''
      if type(users).__name__ != 'list':
          return False
      if len(msg) <= 0 or len(msg) >= 141:
          return False
      # now we know we have a list and a valid length message lets loop though and 
      # send the message to each user
      for user in users:
          self.connect.PostDirectMessage(user, msg)

  def tweetit(self,msg):
      '''Method to just tweet the nagios status'''
      if len(msg) <= 0 or len(msg) >= 141:
          return False

      self.connect.PostUpdate(msg)

def main(argv):
    dmonly = False
    tweetit = False
    users = []
    msg = ''
    twitusr = ''
    twitpass = ''

    try:
        opts,args = getopt.getopt(argv, 'h',['help','users=','twitusr=','twitpass=','dmonly','tweetit','msg='])
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    for opt,arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
        elif opt == '--dmonly':
            dmonly = True
            tweetit = False
        elif opt == '--tweetit':
            dmonly = False
            tweetit = True
        elif opt == '--users':
            users = arg.split(',')
        elif opt == '--twitusr':
            twitusr = arg
        elif opt == '--twitpass':
            twitpass = arg
        elif opt == '--msg':
            if len(arg) <= 0 or len(arg) >= 141:
                usage()
                sys.exit()
            msg = arg
        
    twitcon = nagger(twitusr,twitpass)
    if dmonly and not tweetit:
        twitcon.inform(users,msg)
    if tweetit and not dmonly:
        twitcon.tweetit(msg)

def usage():
    print __doc__

if __name__ == "__main__":
    main(sys.argv[1:])
