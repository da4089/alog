wlog
----
A simple sampling work time recorder.

- Two components: server and client.
  - Server runs centrally, and records everything.
  - Clients can run anywhere, and more than one of them.
  - Server has three web UIs:
    - Journal report, which reports the comments in journal format
    - Time report, which reports hours/project
    - Editing mode, where you can hack the database
      - Alter recorded times
      - Add new projects
      - Remove projects
      - etc
- Every 15 minutes, server pings all clients, and they pop up a window
  asking what you've done for the last 15 minutes.
  - Time period is tunable.
- First client to answer wins, and pops-down the other clients.
- If no answer within a timeout, it'll record an "AFK" entry.
- The default is what you said last time (sent by server).
- You can change it to something else.
- It does completion, so switching tasks is simple.
- There's a drop-down list if you want that instead.
- Optional notes with each time entry too.  They're appended to the
  journal with a timestamp.
- You can add a journal entry at any time.
- There's a command-line client to produce a time tracking report:
  default to latest day, with options for any start/end dates.


Use Python for server
Write Linux client (Qt? Athena? Wx? Gtk?)
Write OSX client (Qt? ObjC+Cocoa? Wx?)
Write iOS client (ObjC+Cocoa)
Write Android client (Java)

Connectivity from client to server is SSL, with HTTPS proxy option.
Messages use protobuf marshalling.

So server daemon
- loops, with timer every n minutes
- pings all active clients, suggesting last task name
- records response, if any
- if no response, records AFK
- tells all clients to hide again
- if new task, send to all clients


Protocol
- LoginRequest (C->S)
- LoginResponse (S->C)
- GetKnownTasks (C->S)
- JournalEntry (C->S)
- CurrentTaskRequest (S->C)
- CurrentTaskResponse (C->S)
- CurrentTaskUpdate (S->C)
 

