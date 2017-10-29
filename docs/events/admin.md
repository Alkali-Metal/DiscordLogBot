## `GUILD_CREATE`:
Called when a server is joined by the bot. Can **only** be added via the `admin-event` command.

This logs the guild name and ID.


## `GUILD_DELETE`:
Called when the bot is removed from a server. (Banned, kicked, etc.)

This logs the guild name, ID, and any log data that they had in the guild if it doesn't reach the character limit (Data only in rich styling).


## `GUILD_LEAVE`:
Called when the bot leaves the server on it's own accord. (via the `leave [server ID]` command or when whitelisted guilds is enabled.)

This logs the guild name, ID, and any log data that they had in the guild if it doesn't reach the character limit (Data only in rich styling).