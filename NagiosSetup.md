#How to use this with nagios

# Introduction #

define command {
> command\_name notify-errr-by-twitter
> command\_line /usr/local/bin/nagger -d --msg="some msg" -uerrr --twitusr=nagger01 --twitpass=mypass
}

This would be for direct messaging the user errr on twitter. The message would come from nagger01. Both of these accounts must be valid.

Options:
> -h, --help            show this help message and exit
> -u USER, --user=USER  Set the user name for the twitter account who will get
> > the message

> -t TWITUSR, --twitusr=TWITUSR
> > Twitter account to auth as. Default is to use values
> > in the config file

> -p TWITPASS, --twitpass=TWITPASS
> > Password for Twitter user

> -T, --tweetit         Use this option to post to the users status. Do not
> > use with -d or --dmonly

> -d, --dmonly          Use this option to direct message a user. Must be used
> > with -u or --user

> -m MSG, --msg=MSG     140 char max len message to be sent to twitter


# Details #

Add your content here.  Format your content with:
  * Text in **bold** or _italic_
  * Headings, paragraphs, and lists
  * Automatic links to other wiki pages