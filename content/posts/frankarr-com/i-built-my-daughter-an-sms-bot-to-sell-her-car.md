---
title: "I Built My Daughter an SMS Bot to Sell Her Car"
platform: "frankarr-com"
era: "now"
source_url: "http://frankarr.com/2026/07/30/i-built-my-daughter-an-sms-bot-to-sell-her-car/"
date: "2026-07-30"
---

Emma is moving to London next week.

She finished her Masters of Data Science, [joined AWS](https://frankarr.com/2019/12/09/700-days-with-an-unexpected-twist/), built her career. Now she's off. London, new job, new chapter. We're proud of her.

[](https://frankarr.wordpress.com/wp-content/uploads/2026/07/0b9f6f80-0809-4a17-9127-73632e17fa18.jpg)

Before she goes, she needs to sell her car. A 2014 Fiat 500c, light blue, convertible. Emma's brief: put a sign on the car with a phone number, and have a mechanism to handle whatever comes in, because she didn't want to manually field every enquiry while also wrapping up her Melbourne life and preparing for a move to the other side of the world. She asked me to build it. More specifically, she asked me to get my AI friend Claw to build it. Which I think says something about where we are with this stuff, my daughter's instinct wasn't "Dad can probably figure this out." It was "Dad knows someone who can."

So I built her a Twilio IVR system.

## Back in 2014 I was at Telstra, working on opening up the SMS API to developers.

It sounds simple now. It wasn't. Carrier-grade SMS meant navigating carrier agreements, ACMA compliance, message routing infrastructure, spam controls, rate limiting, provisioning systems. There were meetings about meetings. There were people whose entire job was one slice of the message delivery pipeline. We were essentially building a platform so developers could send a text message without thinking about any of that.

It took months. Teams of people. Enterprise procurement. A lot of PowerPoint.

This week I did the same thing in an afternoon.

## Here's what Emma's car listing actually needed

A buyer texts a number. They get the car details back automatically – year, kms, price, condition. If they want to inspect it, they say so and get prompted to share their name and some times that suit. If they give a day and time, they get a booking confirmation. Every enquiry fires me an alert SMS, and the whole log goes into a Google Sheet.

That's it. That's the brief.

Emma reminded me on Sunday. Monday I signed up for Twilio and hit the first speed bump: ACMA requires identity verification before you can provision an Australian number. Upload your ID, submit the bundle, wait. It took about 48 hours to clear.

Which felt mildly ironic, given that I'd spent years on the Telstra side of that exact compliance process.

Wednesday the approval came through. From there it was plain sailing, buy a number, point the webhook at an endpoint, done. The carrier infrastructure, the message routing, the compliance layer, the delivery receipts, all of it is Twilio's problem now. You pay a few cents per message and get the thing that cost Telstra engineering months to build.

## The webhook lives inside a WordPress Code Snippet

This is the constraint-led part. Emma's car listing is hosted on my blog, which runs on shared hosting. No EC2 instance. No persistent Python process. No cron-able server. Just PHP on shared infrastructure.

So the webhook is a WordPress REST endpoint registered inside a Code Snippet, about 200 lines of PHP. Twilio POSTs to it when a message arrives, the snippet classifies the intent, builds a TwiML response, and returns it. WP exits. Twilio sends the SMS. Nobody's server stays awake waiting for anything.

It works. It's not elegant. It's exactly the right tool for the situation.

The intent classification took a few iterations to get right. First version just returned car details for everything. Then I added inspection keyword detection – "inspect", "test drive", "want to view", that sort of thing. Then I hit the edge case: someone says "I want to inspect" after getting the details reply, and then a few hours later texts "Frank, Tuesday at 10am", which has zero inspection keywords. So I added booking intent detection, looking for a day word plus a time word in the same message. That covered it.

One thing I didn't see coming: the word "INFO" is a reserved keyword in Twilio. Regulatory compliance, carriers intercept it globally. You can't override it, whitelist it, or route around it regardless of account type. So the first iteration that asked buyers to reply INFO for details just silently failed. Switched it to "Reply DETAILS" and moved on.

## The Google Sheets piece was easier than I expected

I wanted a log of every enquiry. The cleanest solution: a Google Apps Script web app with a single doPost() function that appends a row to a spreadsheet. The WordPress snippet fires a non-blocking POST to the Apps Script URL on every enquiry. No OAuth on the WP side. No credentials to manage. I deployed the Apps Script, grabbed the URL, dropped it into the snippet, done.

The sheet has four columns: Timestamp (AEST), Type, From, Note. Every SMS and every call goes in. Emma doesn't need to watch it, I do. I'll report back to her in London on how the sale is going. She's got enough to worry about. Dad's got the spreadsheet.

## The voice IVR runs off the same infrastructure

Callers get an automated menu in Australian Nicole's voice – Press 1 for car details, Press 2 to request a callback. Press 1 reads the details aloud and also sends an SMS. Press 2 fires me an alert. The whole thing is another 30 lines of TwiML inside the same snippet.

I remember when building an IVR meant Avaya, or Cisco, or a specialist integrator, and a budget with five figures in it. Now it's a PHP function and an afternoon.

## The whole thing took one afternoon

SMS auto-responder, voice IVR, intent classification, Google Sheets logging – one afternoon and a few iterations to iron out the edge cases.

Ten years ago at Telstra I was in rooms full of smart people working for months to give developers access to the same building block. The infrastructure didn't get simpler. It just became someone else's problem. Twilio's problem. Which means I get to spend my afternoon on the bit that matters: does the buyer get useful information, and do I know about it when they text.

The car is a 2014 Fiat 500c in Celeste Blue. Convertible roof. Italian flag on the door. 50,000 km, AU$14,000, rego until September. Emma bought it herself before she got her drivers license, drove it for years, loved it. Data the Dachshund has been in the back seat more times than I can count. It's a Melbourne car.

Emma boards her flight next week. The Twilio number stays active. Somewhere out there is a buyer who's going to text +61 485 085 685 and get an instant reply from a PHP snippet running on a shared hosting plan, built on infrastructure it took a telco months to open up to developers. 

[](https://frankarr.wordpress.com/wp-content/uploads/2026/07/img_1413.jpg)

I hope they like the car
