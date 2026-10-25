---
title: "Announcing Ruby.NET interop support in Beta 0.8"
platform: "msdn"
era: "microsoft"
source_url: "https://learn.microsoft.com/en-us/archive/blogs/frankarr/announcing-ruby-net-interop-support-in-beta-0-8"
date: "2007-06-05"
---

Note
signing in
or
changing directories
.
changing directories
.
Announcing Ruby.NET interop support in Beta 0.8
The
Ruby.NET team at QUT
continues to release updates. I got the following email from Wayne Kelly today
From:
Wayne Kelly
Sent:
Tuesday, 5 June 2007 4:14 PM
To:
Frank Arrigo
Subject:
Announcing Ruby.NET interop support in Beta 0.8
Dear frank,
We are pleased to announce the release of a new Beta (version 0.8) of the Gardens Point Ruby.NET compiler. Since the last release we have added support for interoperability with other .NET languages, so that components developed using other .NET languages can conveniently use classes implemented using Ruby.NET and vice versa. Please see our home page:
https://plas2003.fit.qut.edu.au/Ruby.NET/
to download installers, full source code or for further details.
This first prototype has a number of limitations with respect to interoperability, including:
1. Ruby programs can only call methods implemented in other
languages where the parameters are passed by value
(ie, we don't yet support calling methods that include
ref or out parameters).
2. Non-Ruby programs can only conveniently make use of Ruby
classes that have no explicit parent class (ie we don't
yet support interop if the Ruby class inherits from
something other than Object).
We will address these and other interoperability issues in our next release and hope to demonstrate development of Forms applications using Ruby.NET in our next release.
Our work on porting Ruby on Rails is progressing well, but is not yet ready for public release.
We still haven't yet performed any optimization on the code we generate.
We will soon be moving to a more traditional open source model of community contribution to our code base and will be calling for volunteer developers. If anyone has any experience in managing that kind of process, we'd be interested in your input.
You are also welcome to submit bug reports to w.kelly@qut.edu.au - please submit a minimal self-contained Ruby snippet that illustrates the bug.
Cheers, Wayne.
(for the Ruby.NET team)
________________________________
Technorati tags:
Ruby.NET
,
QUT
,
Wayne Kelly
Comments
Anonymous
June 05, 2007
PingBack from
http://testsubdomain.netmoviehost.com/announcing-rubynet-interop-support-in-beta-08/
Additional resources
Last updated on
2007-06-05
