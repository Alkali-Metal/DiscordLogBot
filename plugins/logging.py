from data.storage import load
from data.storage import delete_guild
from data.functions import load_config
from data.functions import create_log_embed
from data.functions import response_to_class
from data.custom_event_data import custom_data

from holster.emitter import Priority

from disco.bot import Plugin


#TODO: Auto-delete a guild from database upon leaving or being kicked/banned.


class LoggingPlugin(Plugin):
    
    #NOTE: Log to Channels:
    #self.bot.client.api.client.channels_messages_create(int(channel_id),
                        #                                content=log_message,
                        #                                embed=embed)
    
    
    
    #NOTE: Leave guilds upon joining if they're not whitelisted
    #TODO: Leave non-whitelisted guilds if enabled.
    #TODO: Guild Created
    #TODO: Guild Deleted
    #TODO: Guild Left
    #TODO: Message Delete
    #TODO: Message Edit
    #TODO: Mention Everyone
    #TODO: Send a TTS Message
    #TODO: Reaction Added
    #TODO: Reaction Removed
    #TODO: Reaction All Remove
    #TODO: Invite Created
    #TODO: Invite Deleted
    #TODO: Guild Updated
    #TODO: Guild Updated a log channel in the bot
    #TODO: Channel Created
    #TODO: Channel Deleted
    #TODO: Channel Updated
    #TODO: Channel Pins Updated
    #TODO: Ban Add
    #TODO: Ban Remove
    #TODO: Emojis Updated
    #TODO: Integrations Updated
    #TODO: Member Joined (And random string variant)
    #TODO: Member Leave
    #TODO: Member Updated
    #TODO: Role Created
    #TODO: Role Updated
    #TODO: Role Deleted
    #TODO: Member Presence Update
    #TODO: Voice State Updated
    #TODO: Voice Server Updated
    #TODO: Webhooks Updated
    #TODO: Non-Bot Embeds