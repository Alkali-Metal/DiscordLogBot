## `USER_JOIN` + `USER_JOIN_RANDOM`:
Triggers when a user joins the server. There are two variants of this event as `USER_JOIN` has a consistent log message (useful for uniform logging) and `USER_JOIN_RANDOM` has a random join message of which matches those from the built-in notifications of Discord. This event logs the name and ID of the user, as well as containing a user-mention in `rich` styling only. The message logged upon joining the server can be modified if using the `USER_JOIN` event by running `event data user_join response <Response Message...>` in the desired log that you would like to modify the message in, keep in mind, that this can be modified per-channel, but if you abuse this feature it can be disabled for your server entirely.


## `USER_LEAVE`:
Triggers when a user leaves the server. Can be customized the same way as [USER_JOIN](). This event does not have a randomized variant.


## `USER_NICKNAME`:
Triggers when a user changes or resets their nickname. Logs what they changed it to and the user's ID.


## `USER_PRESENCE_UPDATE`:
Triggers when a user updates their presence, this includes the "playing" game, as well as visual status. This event will only be allowed to trigger in guilds with 200 or fewer members.


## `USER_VOICE_JOIN`:
Triggers when a user connects to a voice channel. Logs what channel as well as the user's ID and name.


## `USER_VOICE_LEAVE`:
Triggers when a user leaves a voice channel. Logs what channel as well as the user's ID and name.