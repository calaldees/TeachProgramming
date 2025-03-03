So you want to run a Hack-a-thon?
=================================

I can't think of anything more human and amazing than a hack day. However; many people have heard they are great and want to jump on the hip and trendy bandwagon. All the right buzzwords are there "community" "young people". But so many people don't get it. And when they try to mimic the idea and call it hackday it can cause more long term harm disenfranchising people.
This is my notes on what the pitfalls are and how to do it with some degree of success.

* Prerequisites
    * Before you decide to run one - go to one (if you are not a technologist but an organizer, still attend and observe the event) - preferably 3 of them and speak to some of the attendees and organizers.
    * If you don't understand the event, how will you convince people to attend? If you do convince people to attend, they will probably have the wrong skill-set because you did not understand the event yourself.
* Routes/Themes/Style
    * Creative route
        * Demo-scene Font greets
        * Demo-group Team
        * Physical space (movement, lights, interacting with the real world)
    * Real Route - Meaningful community engagement (solving a real problem with real data)
        * Office for national statistics
        * Canterbury council data?
        * Kent council data?
        * Geo-relevant?
* Has to have meaningful output
    * Not just ducktaping cardboard together or making a mockup from powerpoint slides
* Need time to produce that meaningful output
    * This can't be done in 3 hours. Overnight of a weekend gives the minimum possible time to build anything
    * Sleeping bags under desks
    * Social - food pizzas in the evening - present on Sunday lunchtime to a wider set of spectators
    * Stop the pests - don't let non skilled people wonder and distract the hackers from the focus of the event. Have the metal to ask people to move to the separate 'party room' or leave
* Prerequisite skills of attendees
    * Never processed data before, never created a dynamic webpage, never ...
    * Demo
        * Heatmap on maps
        * Google sheets for storage
    * You may need multiple months of crash course session leading up to the event to demo and develop skills for processing real data
* Attendees need to know what the event is and have the concepts modeled/explained
    * Picking young people and expecting them to perform is foolish
    * They need to see the output of a real hack day to see what's possible and whats expected
    * You need 20% of your attendees minimum to know what they are doing and be role models for what is possible and model the approach
    * The reality is that most young people (even studying computing) will not have the skills required for this by just attending their course. Actually producing something practically in a constrained time and in a team is not the same as passing an exam or doing coursework.
    * The reason why people applaud and clap is because its genuinely impressive what people can do in 24 hours. If you don't have enough understanding of what development is, you won't know how amazing it is, you will just clap hollowly. There is a real difference of an audience in awe and and just some hollow noise
    * Have a local community of people building projects (BarCamp)
    * going from zero to hack day is not possible
    * Quality - Your event is only as good as your attendees. Weak attendees == Weak event. This is not an event for "everyone". Trying to involve everyone blindly will create problems.
    * Social media is good for raising the profile of your event, but it will not attract your skilled attendees. Your mindset should be a 'recruiting' skilled attendees. (look at the curriculum list below). If you can't find them, you need to make them, and that process could take years of support sessions before you run your first hackathon. Maybe your first hackathons are only with a small selected cohort of 12 people as a test?
* You can have good intentions and have an inverse effect
    * coding is hard - "anyone can code" is bullshit. If you open up a hack day for everyone you could just demoralize the weak attendees
    * Unskilled attendees hurt the event - they provide distractions
    * Anyone that thinks "just run a hack day" is going to have a disappointing event and even put people off attending any future hack days organized by other people that might be good. Beware of the damage you can cause.
    * A related example
        * ICT club for girls in 2004 was just an embarrassment - purple spreadsheets about ponies.
* If the event can run regularly for 3 years, you will have enough snowball momentum for work of mouth to attract more people. What could be important is the length of time the event has been established. Potentially you may have you first 2 years as a buildup for the 3rd+ year being productive.
    * You know the winners (everyone wins because you've got a great set of awards). Contact them individually about the next event. Show you're aware of the hack they did. Make them feel valued and remember and that their contribution was important. You can have a template and notes from the previous year and back these out in an hour to 30 people.
* Publish the results and have awards
    * Many young people use these days as CV material. Have a public website that describes each of the hacks and showcases them. This leads to the value of years of accolades enshrined on a page that can be linked to for years (see length in the game above)
    * When you judge the awards - it's not dragons den. Award creativity, skill, approach, passion
    * It is NOT competitive. Participation is the key. I advise against awards like "Best in Show". I also advice against meaningless awards "Most likely to go to the moon".
        * Some ideas "Best Technology", "Best Team", "Local Hero's"
    * (One of the prizes I won once was an engineering day where we build HexaYerts and GridBeam furniture to put in the yert, solar power wiring and a composting toilet. Can you create prizes that further engagement)


Hackathon Prerequisites/Curriculum
-----------------------

The description above got me think about what would actually be needed beyond the basics taught by normal computing courses (if statements, functions and for loops, etc)

Here is a question - if you want a program to do anything and produce some meaningful output .. what do you need? You need to be able to:
* work with data
    * get data from somewhere
        * (api's? files?) know what formats to work in
        * input devices (events)
    * store some data in some way (memory? disk? structure?)
    * output data (charts? transcode? graphics? devices (rgb strips? speakers?))

With that in mind, here is a of core skills to allow that to happen.

* Git (required to collaborate - if you want ANYONE to be able to work in a team)
    * push, pull, resolve merge conflicts
* Data formats (and libraries to read+write them)
    * csv, json
* http (GET, POST)
    * request headers and response
    * query string, hash
    * apis
        * know how to pass an authentication token
        * read docs autonomously (implement discord bots)
    * Use a cookie
* ssh rsa key generation (at least an understanding)
    * Prerequisite for git setup
* ssh, ftp (get file onto servers)
* javascript
    * fetch
    * programmatic generation of html
    * layout framework?
* canvas drawing
    * shapes from code
* commandline tools to leverage data
    * ffmpeg (video encoding/decoding)
    * pandoc (document conversion)
* graph generation
    * on any platform (Plotly? Chart.js?)
* encoding
    * base64
    * gzip
* use of tcp and udp
* use of structured database
    * sqlite

The list is huge. This takes years to acquire the core skills to produce anything meaningful.
You attendees need to at least know what most of these things are, even if they can't use them autonomously yet.
If you run a hackathon and 90% of your attendees can't do this, it's going to be a very weak hackathon.
I would say that 50% of your attendees needs to have the capacity to create even simple pieces of software autonomously in a massively constrained time period.

Realize what is required.

I you do not understand what the items are above, then you will not in a position to recruit the right people or be in position to help them build the relevant skills in preparation for the event.


References
----------

I was asked for advice on setting up a hackathon for girls with local schools and undergrads. I waxed lyrical about my advice and wrote this document.
