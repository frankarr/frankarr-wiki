---
title: "Aussie XMLTV WebService"
platform: "msdn"
era: "microsoft"
source_url: "https://learn.microsoft.com/en-us/archive/blogs/frankarr/aussie-xmltv-webservice"
date: "2004-05-12"
---

Note
signing in
or
changing directories
.
changing directories
.
Aussie XMLTV WebService
I stumbled across a really interesting xml webservice that does something really handy, provides access to a local Australian TV program guide information. A very handy service indeed.
Development One's XMLTV based television programme guide information service for Australia
.
The following operations are supported.
GetProviders
Provides a listing of all Television providers for Australia - consisting of a code and a description for each provider.
GetPayProviders
Provides a listing of all Pay Television providers for Australia - consisting of a code and a description for each provider.
GetChannels
Provides a listing of Channels for a given Provider and Region.
GetRegions
Provides a listing of regions for Australia, consisting of a code and a description for each region.
GetPayChannels2
Provides a listing of Pay Television Channels for a given Provider and Region, with the option to list the Pay TV channels or the Free to Air channels.
GetRecordCount
Provides the record count for a given database table.
GetPrograms
Provides a listing of Programs for a given Channel (using its ChannelID) and Date.
GetPayChannels
Provides a listing of Pay Television Channels for a given Provider and Region, with the option to include Free to Air Channels.
GetChannelInfo
Provides the details for a given Channel or Channels. List multiple channels with space delimiter.
GetFreeChannels
Provides a listing of Free to Air Channels for a given Region.
I'm thinking of using this to create an
TV GUIDE
app for my
XDA II
! Hmmm, two dreams apps now for my device.
Comments
Anonymous
May 12, 2004
Awesome! I've been looking for just this very thing. Thanks Frank!
Anonymous
May 12, 2004
Steady on!! Still working on the AFL application. Which is going well and should have demo to you shortly for beta testing.
At least the webservices for this are written so will be a lot easier to write.
Anonymous
May 31, 2009
PingBack from
http://woodtvstand.info/story.php?id=622
Additional resources
Last updated on
2004-05-12
