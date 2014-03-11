Linux alog client
=================
Basically, this program runs in the background and every configurable
period, it pops up an annoying window asking what you've been doing
for the last period.

That window should ideally not grab the focus, but it should be
obvious, and it should deal with tvtwm's virtual desktop as well as
GNOME-style multi-paned desktops.

The window itself doesn't need much smarts: it'd be good to have a
drop-down entry-box widget that did auto-completion, which probably
means it's not standard Athena widgets.  Other than that, it just
needs Ok & Cancel buttons and maybe a link to the web pages?


The harder part is how to make it work well.  In an ideal world, it
would be constantly connected to the backend, and the backend would
ping it when it needed to ask again.  That doesn't work well for
laptops on planes though.

So, while it could have a connected mode as the primary, it needs to
have some fallback mode where it can operate correctly whilst
disconnected, and when it succeeds in connecting again, it can submit
its information.

It'll need to acquire the configured period, and sleep for that
duration itself.  If it gets a ping, great.  Otherwise just assume the
saved period remains correct and use that interval.

So, that's a timer, which can be hooked into the XtAppMainLoop.  No
worries.  The server connection can use XtAppAddInput for its
socket too, all good.


Next Steps
----------
- Get basic window with button and input field displayed
- Show and hide window with timer
- Connect socket to server and integrate with Xt event loop
- Add protobuf parser to encode/decode server messages
- Replace input field with useful widget doing completion, etc

