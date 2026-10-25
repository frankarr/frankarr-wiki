---
title: "I Spent a Weekend Archiving 23 Years of My Digital Life. Here's What I Found."
platform: "frankarr-com"
era: "now"
source_url: "https://frankarr.com/2026/08/10/i-spent-a-weekend-archiving-23-years-of-my-digital-life-heres-what-i-found/"
date: "2026-08-10"
---

## 1/ Why

My digital memory is scattered across platforms I don't fully control. Posts, tweets, connections, and half-finished drafts spread across twenty-three years of being online as a tech person in Australia, and some of it is already gone.

I started blogging in May 2003 on Radio UserLand, back when blogging was still a weird niche thing that tech people did. Dave Winer's platform. Permalinks were a new idea. RSS was exciting. I was a Microsoft Technical Evangelist in Sydney and I had thoughts about .NET, cricket, and whatever else was happening that week. The tagline on my Radio UserLand page, which is somehow still live: *"an AFL loving geek in sydney."* (The current version has been updated to Seattle, it evolved as I did.)

I've been online in some form ever since. Radio UserLand until 2008. weblogs.asp.net, a homebrew Microsoft employee blog platform that predated MSDN blogs. Then MSDN blogs from December 2003 to 2013. Blogspot running in parallel. LinkedIn since December 2003. Twitter from December 2006. frankarr.com since 2011. LinkedIn Pulse articles. 45,867 tweets.

Five of those LinkedIn Pulse articles don't exist anywhere else. 474,000 words on Twitter. 1,709 MSDN posts. But those six articles, the ones I dashed off to LinkedIn as an afterthought, are the only copies left.

During the Telstra years (2014–2017), Telstra ran an employee publishing platform called Telstra Exchange, named one of the top 25 corporate blogs in Australia at the time. Employees writing real stories about real work. I wrote about [Techfugees Melbourne](https://www.linkedin.com/pulse/what-happens-when-you-add-humanitarians-hackers-hustlers-frank-arrigo/?trackingId=DOR2XHULRB6G%2B6HIFmuB%2Fg%3D%3D), a [recap of APIdays Australia 2016](https://www.linkedin.com/pulse/its-apis-value-bring-quick-recap-apidays-australia-2016-arrigo/?trackingId=DOR2XHULRB6G%2B6HIFmuB%2Fg%3D%3D), [a week hosting a work experience student named Lara](https://www.linkedin.com/pulse/week-workexperiencelara-frank-arrigo/?trackingId=DOR2XHULRB6G%2B6HIFmuB%2Fg%3D%3D), [TOM:Melbourne, a hackathon for people with disabilities](https://www.linkedin.com/pulse/were-supporting-tommelbourne-frank-arrigo/?trackingId=DOR2XHULRB6G%2B6HIFmuB%2Fg%3D%3D). Good stuff. I cross-posted them to LinkedIn Pulse almost as an afterthought. All to be rescued soon!

Telstra Exchange still exists. It's been reborn as a customer-facing news site. The old employee content is gone. The Wayback Machine doesn't have my author page. The LinkedIn copies, the afterthought ones, are the only surviving versions. You can't predict which copy will be the last one standing, which is why I built the archive.

## 2/ How

I had a lot of help.

**Claw** 🦞 (my AI agent and coordinator) wrote most of the parsing scripts and ran the crawls. **Scout** 🦉 (research agent) dug up the older material, including an [SMH profile from 2002](https://www.smh.com.au/national/the-promise-of-technological-heaven-20020305-gdf4zv.html) that's still live. **Dash** 🐱 (writer) helped shape the narrative once the data was in. **Data** 🐶 (analyst) ran the numbers.

The ingredients:

- **Radio UserLand** — Dave Winer's early blogging platform. First post: 23 May 2003. The site is still fully live at [radio-weblogs.com](http://radio-weblogs.com/0124955/) — every post, every monthly index, all intact. Crawled it directly. 1,421 posts through to January 2008.

- **weblogs.asp.net** — Scott Guthrie's homebrew ASP.NET blog platform for Microsoft employees, which predated MSDN blogs. I was on this too. Not well archived — content mostly unrecoverable.

- **MSDN blogs** — Microsoft's official developer blogging platform, now archived at [learn.microsoft.com](https://learn.microsoft.com/en-us/archive/blogs/frankarr/first-post). First post: 3 December 2003. The opening line: *"Hello and welcome! I have a bunch of sites: frankarr on radio, frankarr on blogspot, fda on eraserver…"* The first comment, same day: *"Hi Frank, think you're going for the record for the most amount of blogs :)"* — which, honestly, still applies. 1,709 posts through to September 2013.

- **Blogspot** — a parallel blog running from mid-2003. 117 posts. Mostly link-blogging and cricket scores.

- **Twitter/X** — full archive download, 4.5GB total. We only needed the JSON data folder. Each year's tweets live in a JavaScript file — the parser strips the window.YTD.tweets.part0 = wrapper and processes the rest.

- **LinkedIn** — "Complete Data Export" from Settings, takes about 24 hours to arrive. CSVs for connections, rendered HTML files for articles. Each source needed its own parser.

- **frankarr.com** — crawled via the WordPress.com public API. Paginated 100 posts per page.

- **Press clippings** — the 2002 Sydney Morning Herald profile (I'm quoted as "*the man with the most bleeding edge experience*"). These go in the archive as documents, not JSON.

A few hours of scripting, checkpoint files for the slow crawls, and it was done.

## 3/ What I found

**The numbers:**

23 years of being online, laid flat:

PlatformPosts / itemsFirst postSpanFlickr4,360 photos7 Apr 2003Apr 2003 → Aug 2026Radio UserLand1,42123 May 2003May 2003 → Jan 2008weblogs.asp.netunknown~mid 2003~2003Blogspot11730 Jun 2003Jun 2003 → Nov 2008MSDN blog1,7093 Dec 2003Dec 2003 → Sep 2013LinkedIn7,609 connections27 Dec 2003Dec 2003 → Aug 2026Twitter/X45,867 tweets15 Dec 2006Dec 2006 → Aug 2026LinkedIn posts & shares10,58725 Mar 2010Mar 2010 → Aug 2026LinkedIn articles18Sep 2017Sep 2017 → Nov 2022frankarr.com65*28 Jan 2011Jan 2011 → Aug 2026**Total****~67,400+****2003 → 2026**

*Plus 664 Fitbit step-count auto-posts from 2012–2014. Not exactly riveting reading. We flagged them and moved on.

The platform timeline:

- **April 2003** — first Flickr photo. Before the first blog post — photos came first.

- **May 2003** — first Radio UserLand post. *"musings by frank arrigo, an AFL loving geek in sydney."* Blogging when most people had never heard the word.

- **~mid 2003** — weblogs.asp.net, the homebrew Microsoft employee blog platform.

- **June 2003** — Blogspot starts. First post: 30 June 2003.

- **December 2003** — MSDN blogs. I joined LinkedIn the same week. (LinkedIn had launched that May — seven months old, 81,000 members.)

- **December 2006** — Twitter. @frankarr, ID 72373. In its first year.

- **2008** — Radio UserLand shuts down as a going concern. The posts survive anyway — the site is still live at radio-weblogs.com.

- **March 2010** — first LinkedIn post: a link to watch college basketball in HD via Silverlight. Very 2010.

- **January 2011** — frankarr.com. MSDN blog winds down through to 2013.

- **2015–2017** — peak Twitter years.

- **2018–2019** — peak LinkedIn. The AWS years.

- **2026** — this blog. Properly. Finally.

**What the gaps say:**

Long-form writing went quiet from around 2015 to 2026. That's not laziness, it's what full-time corporate life looks like from the outside. Twitter kept going (45,000 tweets don't lie), but the long-form thinking stopped. You can see exactly when there was room to write and when there wasn't.

Each platform also has a distinct character that maps directly onto where I was at the time. Radio UserLand and MSDN were the Microsoft years, technical content, developer community, .NET. LinkedIn grew as the career grew. Twitter was always personal, football, tech, Melbourne. frankarr.com is the post-corporate chapter.

**The community I built:**

One thing the data doesn't show in the numbers: I spent a significant chunk of 2004 and 2005 playing community cheerleader for Australian tech bloggers.

In February 2004, I put out a call on my MSDN blog: *"I am keen to create a list of Australian .NET bloggers and make an OPML file available for anyone who wants to add this list to their own RSS reader."* OPML was the file format for sharing RSS subscription lists, a way to say *here are all the people worth reading, importable in one click*.

Within days, the Aussie .NET Developer OPML was live. Every few weeks: a new welcome post, ["Welcome to new Aussie Blogger – Chris Garty"](https://learn.microsoft.com/en-us/archive/blogs/frankarr/welcome-to-new-aussie-blogger-chris-garty), ["Welcome Tatham Oddie"](https://learn.microsoft.com/en-us/archive/blogs/frankarr/welcome-tatham-oddie-another-aussie-net-developer-and-blogger), ["Welcome Bruce McLeod"](https://learn.microsoft.com/en-us/archive/blogs/frankarr/welcome-bruce-mcleod-to-aussie-net-blogger-community). The OPML lived at radio.weblogs.com/0124955/gems/aus-dotnet.opml, maintained by hand, updated constantly.

By its first birthday in February 2005, it had **69 entries**. The NZ developer community liked it so much they started their own Kiwi OPML. There were discussions about merging the two lists.

In March 2005, *The Bulletin* magazine ran a [business blogging feature](https://web.archive.org/web/20050721070045/http://bulletin.ninemsn.com.au/bulletin/site/articleIDs/DF1B65496F6A98E8CA256FB10021E721?open&ui=dom&template=domBulletin). I was in it alongside Lenn Pryor from Microsoft and four other Australian bloggers, Trevor Cook, Mark Jones, Derek Lark, and Neil Napper. The article quoted me: *"It's about creating a community."* and *"People have sophisticated BS meters and if the voice isn't real, they can smell it a mile off."* I was also listed first in the magazine's "Top biz blogs" sidebar, ahead of Robert Scoble. That's the moment the Australian blogosphere crossed into the mainstream business press.

By 2007, the Australian blog index BlogPond was tracking blogs.msdn.com/frankarr at #64 in the country, with a global Alexa rank of 12.

None of that was in my job description. It was just: *these people are doing interesting work, let me shine a light on it.*

**Before the blog: the Napster years**

The archive only goes back to 2003, that's when I started blogging. But the pre-blog career has its own paper trail, recovered mostly from the Wayback Machine.

From 1999 to 2001, I was Microsoft Australia's Business Development Manager for Windows Media Technologies, covering AU, NZ and Singapore. The job was to convince record labels, streaming services, and content providers to build on Windows Media rather than MP3 or RealNetworks. Two years of constant travel across Asia, my own words on the subject: *"I spent 2 years traveling around Asia – it got pretty tiring."*

This was peak Napster. The RIAA and MPAA were suing everyone. Scour, Aimster, KaZaA, new P2P apps launched every few months. The music industry was in full panic. Microsoft's position was that Windows Media Audio, with its embedded DRM technology, was the path to a licensed future for digital music. My job was to make that case with Australian record labels, APRA, and the emerging digital music startups.

One of those startups was ChaosMusic, a Sydney-based CD retailer that had built a free music search engine called Freetracks, and was experimenting with channelling 15% of ad revenues back to artists. In September 2000, I committed Microsoft Australia as a financial backer of the plan. *Wired News* covered it:

> 
*"One high-profile backer is Microsoft Australia, which has kicked in several thousand dollars to help the plan get off the ground, said Frank Arrigo, Microsoft Australia's business development manager for Windows Media Technologies.*

*'As best I can tell, this ChaosMusic plan is novel,' Arrigo said. 'I haven't seen anything like it done elsewhere.'"*

— ["The Future of File Trading"](https://web.archive.org/web/20001120133600/http://wired.com/news/business/0,1367,38597,00.html), Wired News, November 2000

The article also explains the Microsoft logic: WMA's DRM could attribute royalties to individual artists more precisely, so any model that bolstered copyright protection online directly benefited the format. I wasn't just quoted for a soundbite, I was the person who had put Microsoft money behind the idea.

That article sits in a 2003 MSDN post I wrote called [*"Frank's Scrap Book"*](https://learn.microsoft.com/en-us/archive/blogs/frankarr/franks-scrap-book) , along with another one I'd half-forgotten. In May 1999, as nineMSN's technical director, I was quoted in CRN Australia at a Microsoft e-commerce roadmap launch in Sydney: *"We want to be able to integrate merchants [into nineMSN] without having to have any human intervention."* That article, ["Yawns all round as Microsoft hypes e-biz"](https://web.archive.org/web/20000709071502/http://itnews.com.au:80/crn/news/018_1305h.htm) by Simon Hayes, is still on Wayback. The headline sums up the analyst sentiment of the day. I was the one trying to make it sound exciting.

Both sit in the same Scrap Book, a list of every press mention I could find from my career to that point, organised by era. Finding it in the Wayback Machine twenty-five years later, fully intact, was one of the better moments of this archiving project.

**The shirt:**

This one needs its own section.

For reasons I still can't fully explain, a yellow Mambo Hawaiian shirt with enormous red roses became the most documented garment in Australian tech media history. I had worn it to TechEd Australia every year as a personal tradition, it was a collector's item, no longer available at retail. At TechEd 2003 in Brisbane, at the after-party at Family nightclub, another attendee asked if he could try it on. I let him. He ran. I didn't see it, or him, again.

I wrote about it the following year. Then the year after, when TechEd returned to Queensland, I wrote about still looking for it. Then someone listed a suspiciously familiar Mambo shirt on eBay, item location: Queensland, and I bid on it. Got outbid. Bid again. Won. Paid $150, several times the original price, for what may or may not have been my own shirt. It had a small rip on the pocket in exactly the same place as the original. Probably a coincidence. Probably.

I wore it to TechEd 2005 on the Gold Coast. Leon Bambrick ([secretGeek](https://secretgeek.net/loud_frank)) published a cartoon: *"Just met frank arrigo… he really does look like this. He's one hell of a loud shirt guy. Sort of like a bigger version of Danny DeVito."* Cameron Reilly interviewed me about it for the Tech.Ed MediaCast. Then CRN magazine ran a full column about it in their gossip section, **"ShadowRAM: Dude, where's my shirt?"**, with, apparently, an enormous photo of me on the back page. My friend Rob Irwin emailed to let me know.

In August 2006, a reader sent me photos of a man wearing my shirt at the TechEd 2003 after-party. I posted them publicly and asked if anyone recognised him. Nobody confirmed an ID, though one commenter suggested it was Steve Vamos in drag. (Steve Vamos was Microsoft Australia's CEO at the time.)

I tell this story not because it's particularly meaningful, but because it's evidence of something. The community responded to it. People remembered it for years. The trade press wrote it up. When I left Australia, someone thought the correct way to mark the occasion was to photograph a piece of clothing. That doesn't happen unless the storyteller has a real audience, and unless the audience has a real relationship with the story.

The CRN article is now only accessible via Wayback Machine: ["ShadowRAM: Dude, where's my shirt?"](https://web.archive.org/web/20051214134934/http://www.crn.com.au/story.aspx?CIID=24799), CRN Issue 181, 19 September 2005.

**The Wikipedia deletion:**

In May 2007, someone created a Wikipedia article about me. Within days, it was nominated for deletion.

The nominator questioned whether being ranked Australia's 55th most popular blogger met Wikipedia's notability standards. The Australian tech blogging community mobilised, blog posts went up asking people to vote Keep, with instructions on what to say. Wikipedia editors noticed. The closing administrator deleted the article on 28 May 2007 with the note:

> 
*"The result was delete. No substantial, non-trivial, independent and reliable media coverage, no notability, but a heck of a lot of WP:ILIKEIT."*

WP:ILIKEIT. Wikipedia's term for: people like it, but that's not enough.

About a month later, at ReMix Australia in Melbourne, a developer named Will Hughes handed me a custom-made t-shirt printed with the exact phrase from that closing notice: *"This person does not satisfy Wikipedia's Notability Requirements."* A photo of me wearing it, hands on hips, red conference lanyard, full confidence, was taken by Nick Hodge, who had voted Keep in the AfD discussion. The photo lived on Flickr until it didn't. I found a copy in my phone nearly twenty years later.

I have never been re-added to Wikipedia. The page has remained deleted since June 2007.

**The ghost post:**

November 18, 2022. A LinkedIn article draft that was never published. The title: *"59"*. My birthday. I was turning 59 that day, deep in the AWS years, clearly had something on my mind, started typing, and then didn't finish it. The entire content of the article is just that one word and a timestamp. I found it in the data export. I kind of wish I'd written it.

## 4/ What's next

**Flickr:**

I should mention Flickr. 4,360 photos from April 2003 to 2026, peak years were 2007–2009, around 800 photos a year. The first photo predates the first blog post. It was the visual layer that ran alongside the words, and it's all still there.

The archive is the foundation, not the destination.

- **[Digital dossier](https://frankarr.com/frank-arrigo-digital-dossier/)** — a synthesised document that pulls across all sources. Career timeline with actual quotes, first appearances of ideas, the network mapped over time. Useful when AI assistants try to answer questions about you and worth building before you can't write it anymore.

- **RAG-searchable personal memory** — index everything into a vector database so I can query my own history. "What did I write about cloud in 2012?" "When did I first mention startups?" Answers from my own words.

- **Rescue the LinkedIn-only articles** — six pieces that need a permanent home before Pulse has its own "59" moment.

Build your archive before you need it.

*Thanks to the whole team: Claw 🦞, Scout 🦉, Dash 🐱, and Data 🐶 for the heavy lifting.*
