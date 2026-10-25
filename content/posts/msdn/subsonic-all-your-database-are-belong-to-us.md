---
title: "Subsonic : All your database are belong to us"
platform: "msdn"
era: "microsoft"
source_url: "https://learn.microsoft.com/en-us/archive/blogs/frankarr/subsonic-all-your-database-are-belong-to-us"
date: "2007-04-29"
---

Note
signing in
or
changing directories
.
changing directories
.
Subsonic : All your database are belong to us
During my travels, I caught up with
Brenton Webster
(dude, no blog?), who put me onto
Subsonic
.
About Subsonic
SubSonic is a toolset that helps a website build itself. At it's core it's:
A Data Access Layer (DAL) builder that requires no code on your part, it builds itself at compile-time with a full object layer and strongly-typed collections
A complete utility toolset, complete with Rails-like scaffolding, migrations (DB Versioning), and code generators
A dynamic query tool, that lets you use SQL Server and the Enterprise Library without having to know SQL
An OR Mapper that extends to views and stored procedures so you're not locked into the OR/M thing
What SubSonic does for you:
Trim hours from your DEV cycle. This not only happens because the code is generated for you initially, but it's also maintained by SubSonic whenever you change your database.
Gives you the option to go full-tilt OR/M, or use SPs/Views. We don't want to tell you what to do, you already know best. We just want to help.
Help your application build itself. With our generators (class, scaffold, and batch-class) your site can build itself in no time. The scaffolding will help you work with your data quickly.
A solid foundation from which to extend. Our starter site comes pre-wired with ASP.NET membership built in, AJAX, full 3-column elastic XHTML theme, and user administration pages from which you can administer your site's membership. That's at least a week's worth of work - already done!
Get your project from idea to prototype in a fraction of the time. That's the strength of this project - using our starter kit you can have a sharp prototype up and running in the merest fraction of what it used to take.
Tasty!
See more here:
https://www.wekeroad.com/actionpackintro.html
This is one of the more
popular projects over at Codeplex
. Here's the top 10
AJAX Control Toolkit
patterns & practices - Smart Client Guidance
SameDesk
SubSonic: All your database are belong to us
.NET Reflector Add-Ins
SharpMap - OpenSource Map Engine for .NET 2.0
patterns & practices - Web Client Software Factory
patterns & practices â Enterprise Library
IronPython
XML Notepad
Technorati tags:
Subsonic
,
ASP.NET
,
Codeplex
Comments
Anonymous
April 29, 2007
Does it allow us to implement the Domain Model pattern (
http://udidahan.weblogs.us/2007/04/21/domain-model-pattern/
), in other words, use our own classes to represent business logic?
Anonymous
April 29, 2007
I used subsonic on one of my recent projects - it's great (providing you want to use ActiveRecord). It would also be nice if it could work with things other than ASP.NET "sites" (like real ASP.NET web application projects) but I believe it has a dependency on the custom build providers which are only supported with web sites.
Anonymous
April 30, 2007
You're kidding. You're saying that you can't use it either for smart clients or for non-ASP.NET servers?
Anonymous
May 04, 2007
Of course you can! The BuildProvider is in there for convenience only - we have a full-blown console app that works just like the Rails one in terms of generating code and even versioning your DB (schema and data) to file!
We're getting our docs in order - come take a look!
Additional resources
Last updated on
2007-04-29
