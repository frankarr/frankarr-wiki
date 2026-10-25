---
title: "Making Buttons"
platform: "msdn"
era: "microsoft"
source_url: "https://learn.microsoft.com/en-us/archive/blogs/frankarr/making-buttons"
date: "2006-09-15"
---

Note
signing in
or
changing directories
.
changing directories
.
Making Buttons
I had a play this evening making a
custom button
for
Windows Live Toolbar
Windows Live Toolbar Custom Buttons
The Windows Live Toolbar can easily be customized by adding and creating buttons for your favorite web sites.
Make a button to search within any web site, provide convenient shortcuts and links, or keep your users informed through an RSS feed or a mini-browser window that displays your own web content.
Custom buttons are easy to make and can be shared through Windows Live Gallery. Each custom button is as simple, declarative XML file. That XML file is packaged with button icons into a single .cab file.
This
link
provides you detailed information about how to make custom buttons for the Windows Live Toolbar.
This is the XML for my button
<?xml version="1.0" standalone="yes"?>
<button>
<buttonNamespace>MSDN.MSDN</buttonNamespace>
<locale language="*">
<buttonText>MSDN Australia</buttonText>
<tooltip>MSDN Australia</tooltip>
<icon src="msdn.bmp" />
<shortcuts>
<url href="
https://microsoft.com/australia/msdn/"
/>
</shortcuts>
<menu>
<feeds>
<feed href="
https://blogs.msdn.com/ausdev/rss.aspx"
/>
<feed href="
https://blogs.msdn.com/annali/rss.aspx"
/>
<feed href="
https://blogs.msdn.com/acoat/rss.aspx"
/>
<feed href="
https://blogs.msdn.com/charles_sterling/rss.aspx"
/>
<feed href="
https://blogs.msdn.com/dglover/rss.aspx"
/>
<feed href="
https://blogs.msdn.com/davidlem/rss.aspx"
/>
<feed href="
https://blogs.msdn.com/frankarr/rss.aspx"
/>
<feed href="
https://blogs.msdn.com/nigelwat/rss.aspx"
/>
<feed href="
https://blogs.msdn.com/nilsv/rss.aspx"
/>
<feed href="
https://blogs.technet.com/mkleef/rss.aspx"
/>
<feed href="
https://blogs.technet.com/jeffa36/rss.aspx"
/>
</feeds>
<links>
<link name="Top 10 Downloads" href="
https://www.microsoft.com/communities/rss"
/>
<link name="MSDN Australia News" href="
https://blogs.msdn.com/ausdev/"
/>
<link name="Channel 9 " href="
https://channel9.msdn.com/"
/>
</links>
</menu>
</locale>
</button>
Which makes it look like this in the Windows Live Toolbar
Pretty neat huh? I've got links and live feeds.
I'll tweak it a bit more and if there is any interest, I will publish it out to the
Windows Live Toolbar Gallery
.
[
Current Listening to
:
Andy, You're a Star
by
The Killers
from
Hot Fuss [Limited Edition]
]
Comments
Anonymous
September 15, 2006
Wow that looks ridiculously easy with XML. Although having a feeds-reader already, it is kind of redundant.
Anonymous
September 15, 2006
End of the week points of interest:New York Times are working on a WPF tool to improve readability :
Additional resources
Last updated on
2006-09-15
