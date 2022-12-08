# Programing Python WebSockets

## Background
I always wondered how hardware devices, motion detectors, heat sensors, etc gave live updates to the client (frontend). 

Before, I only worked with standard HTTP requests. If a user wanted information, it would send a request to the server, the server would then parse that request, prepare some information, and send something back to the client. HTTP is not meant for continious connections between a client and a server. HTTP are short-lived.

So what if you wanted to create something like a chatroom, or in this case, take live data gathered from sensors, and continiously send data to the client as long as the client is connected. 

Previously, most websites implement something called long polling, but here we introduce WebSockets. Websockets are used to implement long-lived connections, better for real-time, ongoing connections.

So why not just make repeated HTTP requests at intervals? The main reason is that they are event-driven, less latency, and less overhead. 

Instead of implementing a chatroom, the "Hello World!" of websockets, I system that would continously track mouse movement, and send it to the client. The details can be found in the post here 