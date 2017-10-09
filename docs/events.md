#Events:

## `ROLE_CREATE`:
When a role gets created within a guild. Logs the ID and whether or not the role is managed by an OAuth2 application or not.


## `ROLE_UPDATE`:
When a role's settings get updated. (Doesn't specify what settings were changed at this point in time)


## `ROLE_DELETE`:
When a role gets deleted. Logs the ID, name, and if the role was managed by an OAuth2 application.


## `USER_JOIN`:
Triggers when a user joins the guild. Logs their name and ID and a clickable profile card if in rich mode.


## `USER_JOIN_RANDOM`:
Triggers when a user joins the guild. Logs their name with a random Discord join message. (Most of them are identical to ones that Discord has built-in but there are additional ones.)