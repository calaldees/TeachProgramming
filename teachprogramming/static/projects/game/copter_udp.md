Copter Network
==============

Long term concept for copter expansion

Async queue

Protocol simple
---------------
(every other frame - because udp 60fps to too much)

udp - peer to peer
channelServer - multiple peers (more latency)

Recv x,y
Send x,y

No colision
same code + graphics



Network Approach 1: Protocol Enhanced (predictive)
-----------------

The next frame will be somewhat similar to the previous one.
We can most of the time give a reasonable result with minor glitching

predictive
frame,x,y,keys

Apply input for multiple frames to a player


Network Approach 2: Protocol Exchange
-----------------

Only apply the inputs if all client acknowledge input


SideQuest 1: Timesync start/catchup?
----------------------------

Timestamp? or frame number? every communication?
Raise desync error? notify user
Resync/restart?

Pull cable out + put back in


SideQuest 2: Sending graphics files
-----------------------------------
