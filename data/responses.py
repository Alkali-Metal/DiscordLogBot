class variables:
    docs_link = "https://www.logbot.rtfd.io"
    join_emoji = ":inbox_tray:"
    leave_emoji = ":outbox_tray:"
    update_emoji = ":printer:"
    delete_emoji = ":waste_basket:"
    plus_one = "<:increase:363848505024053248>"
    minus_one = "<:decrease:363848504990367744>"



class compact:
    GUILD_CREATE = variables.inbox_emoji + "Guild Joined: {e.guild.name} (`{e.guild.id}`)"
    GUILD_DELETE = variables.leave_emoji + "Guild Removed: {e.guild.name} (`{e.guild.id}`) ```{data[guild_data]}```"
    GUILD_LEAVE = variables.leave_emoji + "Guild left: {e.guild.name} (`{e.guild.id}`) ```{data[guild_data]}```"
    BOT_LOG_CREATE = variables.plus_one + "<#{e.msg.channel_id}> was added as a log channel. (`{e.msg.author.id}`)"
    BOT_LOG_DELETE = variables.minus_one + "<#{e.msg.channel_id}> was removed as a log channel. (`{e.msg.author.id}`)"
    BOT_EVENT_ADD = variables.plus_one + "Event(s) `{log_events}` was added to <#{e.msg.channel_id}>."
    BOT_EVENT_REMOVE = variables.minus_one + "Event(s) `{log_events}` were removed from <#{e.msg.channel_id}>."
    BOT_DATA_ADD = variables.inbox_emoji + "Data added for event `{log_event}` in <#{e.msg.channel_id}>. Run `data {log_event}` in the log to find out the specific data."
    BOT_DATA_REMOVE = variables.leave_emoji + "Data removed for event `{log_event}` in <#{e.msg.channel_id}>."
    GUILD_UPDATE = ""
    USER_JOIN = ""
    USER_LEAVE = ""
    USER_UPDATE = ""
    MESSAGE_EDIT = ""
    MESSAGE_DELETE = variables.delete_emoji + "Message removed by {} (`{}`) in <#{}>. Content: `{}`. [Attachment]({})"
    MENTION_EVERYONE = ""
    TTS_USAGE = ""
    REACTION_ADD = ""
    REACTION_REMOVE = ""
    REACTION_REMOVE_ALL = ""
    INVITE_CREATE = ""
    INVITE_DELETE = ""
    VOICE_CHANNEL_CREATE = ""
    VOICE_CHANNEL_UPDATE = ""
    VOICE_CHANNEL_DELETE = ""
    TEXT_CHANNEL_CREATE = ""
    TEXT_CHANNEL_UPDATE = ""
    TEXT_CHANNEL_DELETE = ""
    PINS_UPDATE = ""
    BAN_ADD = ""
    BAN_REMOVE = ""
    EMOJI_UPDATE = ""
    INTEGRATION_UPDATE = ""
    ROLE_CREATE = variables.plus_one + "Role created with ID: `{e.role.id}`"
    ROLE_UPDATE = variables.update_emoji + "Role: `{e.role.name}` (`{e.role.id}`) had it's settings changed."
    ROLE_DELETE = variables.minus_one + "Role **{e.role.name}** deleted. (ID: `{e.role.id}`)"
    USER_PRESENCE_UPDATE = ""
    USER_VOICE_STATE = ""
    VOICE_SERVER_UPDATE = ""
    WEBHOOK_CREATE = ""
    WEBHOOK_UPDATE = ""
    WEBHOOK_DELETE = ""
    NON_BOT_EMBED = ""
    USER_JOIN_RANDOM = ""
    
class fancy:
    GUILD_CREATE = [None, "Guild Joined", "Name: {e.guild.name}\nID: `{e.guild.id}`", "Triggered by: GUILD_CREATE", docs_link, None]
    GUILD_DELETE = [None, "Guild Removed", "Name: {e.guild.name}\nID: `{e.guild.id}`\nData: ```{data[guild_data]}```", "Triggered by: GUILD_DELETE", docs_link, None]
    GUILD_LEAVE = [None, "Guild Left", "Name: {e.guild.name}\n ID: `{e.guild.id}`\n Data: ```{data[guild_data]}```", "Triggered by: GUILD_LEAVE", docs_link, None]
    BOT_LOG_CREATE = [None, "Log Created", "Channel: <#{}>\nType: `{}`\nResponsable User: {} (`{}`)", "Triggered by: BOT_LOG_CREATE", docs_link, None]
    BOT_LOG_DELETE = [None, "Log Deleted", "Channel: <#{}>\nResponsable User: {} (`{}`)", "Triggered by: BOT_LOG_DELETE", docs_link, None]
    BOT_EVENT_ADD = [None, "Event Added To Log", "Log Channel: <#{}>\nEvent(s): `{}`\nResponsable User: `{}`", "Triggered by: BOT_EVENT_ADD", docs_link, None]
    BOT_EVENT_REMOVE = [None, "Event Removed from Log", "Log Channel: <#{}>\nEvent(s): `{}`\n Responsable User: {} (`{}`)", "Triggered by: BOT_EVENT_REMOVE", docs_link, None]
    BOT_EVENT_DATA = [None, "Event Data Modified", "Log Channel: <#{}>\nEvent: `{}`\nResponsable User: {} (`{}`)", "Triggered by: BOT_EVENT_DATA", docs_link, None]
    GUILD_UPDATE = [None, "Guild Updated", "Guild Settings have been updated.", "Triggered by: GUILD_UPDATE", docs_link, None]
    USER_JOIN = [None, "User Joined", "{} joined the server!", "Triggered by: USER_JOIN", docs_link, None]
    USER_LEAVE = [None, "User Left${} left the server.", "Triggered by: USER_LEAVE", docs_link, None]
    USER_UPDATE = [None, "", "", None, docs_link, None]
    MESSAGE_EDIT = [None, "", "", None, docs_link, None]
    MESSAGE_DELETE = [None, "Message Deleted", "A message from: {} (`{}`) was deleted in <#{}> with the content: ```{}```\n\n[Attachment]({})", "Triggered by: MESSAGE_DELETE", docs_link, None]
    MENTION_EVERYONE = [None, "", "", None, docs_link, None]
    TTS_USAGE = [None, "", "", None, docs_link, None]
    REACTION_ADD = [None, "", "", None, docs_link, None]
    REACTION_REMOVE = [None, "", "", None, docs_link, None]
    REACTION_REMOVE_ALL = [None, "", "", None, docs_link, None]
    INVITE_CREATE = [None, "", "", None, docs_link, None]
    INVITE_DELETE = [None, "", "", None, docs_link, None]
    VOICE_CHANNEL_CREATE = [None, "", "", None, docs_link, None]
    VOICE_CHANNEL_UPDATE = [None, "", "", None, docs_link, None]
    VOICE_CHANNEL_DELETE = [None, "", "", None, docs_link, None]
    TEXT_CHANNEL_CREATE = [None, "", "", None, docs_link, None]
    TEXT_CHANNEL_UPDATE = [None, "", "", None, docs_link, None]
    TEXT_CHANNEL_DELETE = [None, "", "", None, docs_link, None]
    PINS_UPDATE = [None, "", "", None, docs_link, None]
    BAN_ADD = [None, "", "", None, docs_link, None]
    BAN_REMOVE = [None, "", "", None, docs_link, None]
    EMOJI_UPDATE = [None, "", "", None, docs_link, None]
    INTEGRATION_UPDATE = [None, "", "", None, docs_link, None]
    ROLE_CREATE = [None, "Role Created", "ID: `{e.role.id}`\nManaged By Application: {e.role.managed}", "Triggered by: ROLE_CREATE", docs_link, 0x00AA00]
    ROLE_UPDATE = [None, "Role Updated", "ID: `{e.role.id}`", None, docs_link, None]
    ROLE_DELETE = [None, "Role Deleted", "Name: \nID: `{e.role_id}`", "Triggered by ROLE_DELETE", docs_link, None]
    USER_PRESENCE_UPDATE = [None, "", "", None, docs_link, None]
    USER_VOICE_STATE = [None, "", "", None, docs_link, None]
    VOICE_SERVER_UPDATE = [None, "", "", None, docs_link, None]
    WEBHOOK_CREATE = [None, "", "", None, docs_link, None]
    WEBHOOK_UPDATE = [None, "", "", None, docs_link, None]
    WEBHOOK_DELETE = [None, "", "", None, docs_link, None]
    NON_BOT_EMBED = [None, "", "", None, docs_link, None]
    USER_JOIN_RANDOM = [None, "", "", None, docs_link, None]

class fanceh:
    GUILD_CREATE = "===========================\n**Guild Joined**\nName: {}\nID: `{}`"
    GUILD_DELETE = ""
    GUILD_LEAVE = "===========================\n**Guild Left**\nName: {}\nID: `{}`"
    BOT_LOG_CREATE = ""
    BOT_LOG_DELETE = ""
    BOT_EVENT_ADD = ""
    BOT_EVENT_REMOVE = ""
    BOT_EVENT_DATA = ""
    GUILD_UPDATE = ""
    USER_JOIN = ""
    USER_LEAVE = ""
    USER_UPDATE = ""
    MESSAGE_EDIT = ""
    MESSAGE_DELETE = "===========================\n**Message Deleted**\nA message authored by: {} (`{}`) was deleted in <#{}> with the content: ```{}```\n\nAttachments: {}"
    MENTION_EVERYONE = ""
    TTS_USAGE = ""
    REACTION_ADD = ""
    REACTION_REMOVE = ""
    REACTION_REMOVE_ALL = ""
    INVITE_CREATE = ""
    INVITE_DELETE = ""
    VOICE_CHANNEL_CREATE = ""
    VOICE_CHANNEL_UPDATE = ""
    VOICE_CHANNEL_DELETE = ""
    TEXT_CHANNEL_CREATE = ""
    TEXT_CHANNEL_UPDATE = ""
    TEXT_CHANNEL_DELETE = ""
    PINS_UPDATE = ""
    BAN_ADD = ""
    BAN_REMOVE = ""
    EMOJI_UPDATE = ""
    INTEGRATION_UPDATE = ""
    ROLE_CREATE = "===========================\n**Role Created**\nID: `{e.role.id}`\nManaged: `{e.role.managed}`"
    ROLE_UPDATE = "===========================\n**Role Updated**\nName: {e.role.name}\nID: `{e.role.id}`"
    ROLE_DELETE = "===========================\n**Role Deleted**\nName: {e.role.name}\nID: `{e.role.id}`\nManaged: `{e.role.managed}`"
    USER_PRESENCE_UPDATE = ""
    USER_VOICE_STATE = ""
    VOICE_SERVER_UPDATE = ""
    WEBHOOK_CREATE = ""
    WEBHOOK_UPDATE = ""
    WEBHOOK_DELETE = ""
    NON_BOT_EMBED = ""
    USER_JOIN_RANDOM = ""

class command:
    already_log = "This channel is already a logging channel."
    log_added = "Added this channel as a log."
    log_removed = "Removed this channel as a log."
    no_guild_data = "This server has no data!"
    not_log = "This channel isn't a log."
    not_log_remove = "This channel isn't a log, so I can't remove it."
    cannot_add_event = "Can't add an event to a non-log channel. Run the create command to create a log channel."
    added_log_events = "Added event `{}` to this logging channel."
    not_log_events = "Events: `{}` do not exist, go to https://logbot.rtfd.io to find a list of valid events."
    already_logging = "This channel is already set to log `{}`."
    not_enough_arguments = "Not enough arguments."
    no_event_list = "This channel doesn't have an event list because it isn't a logging channel!"
    event_list = "The events this channel are logging are: ```{}```"
    log_list = "The log channels are: {}"
    invalid_permissions = "You don't have permission to use that commmand. The `Manage Channels` permission is required to be able to manage logs."
    changed_log_type = "Changed log type to: `{}`"
    already_log_type = "This log is already that log type."