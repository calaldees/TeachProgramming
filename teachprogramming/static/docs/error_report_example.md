Reporter:
Global Player App | Apple CarPlay Issue

Hello all,

Hope you are well.

We have a user who is having trouble with using Global Player with Apple CarPlay. When they click on Global Player app on CarPlay on the cars built in display, they receive a blank screen. They are connected to CarPlay via wired connection. If they open the app on their phone first and then connect to CarPlay, it works fine.

The customer is on an older version of Global Player, as their iPhone 8 does not support iOS 17. This may be the reason why this isn't working as normal.

We've walked through some troubleshooting questions and steps and these are outlined below.

Device information:
Device Make and Model - iPhone 8
Device Software Version - iOS 16.7.12
About the Global Player App:
App version - (Latest version available for iOS 16)

---

ProductOwner: @Allan Callaghan Not sure if you know of any issues supporting older versions of the car bff at all?

---

Allan Callaghan:
> any issues supporting older versions of the car bff at all
There may be issues. We don't know.
@ProductOwner We've done our best efforts to preserve the old api versions for bff-car. However, the reality is:
* We don't have a framework or process for formally testing releases with older released versions of the app. We have no repository of previous stores of released APK/APP to test with (and it's very hard to build previous versions from code, especially on iOS). (Changing the api version header for the current app build is insufficient to verify old versions)
* We have no real server side production api snapshots for old versions. It would be good if we could verify our api outputs 'now' vs '6 months ago' to see if the structure has been damaged.
Summary:
* We don't have the tooling to verify our support for old versions. We just 'do our best efforts'. We think it works ...

I've attached a screenshot of the "Requests Per minuet per bff-car api version". It's 99% the current version (v6) with a couple of requests for V1 and v5 (very very few v2,v3,v4)
Screenshot 2025-10-24 at 10.30.42.png

---

Reporter:
If someone could clarify what this means, that would be helpful :sweat_smile: Thanks!