from data.storage import load
from data.storage import delete_guild
#from data.storage import create_guild
from data.functions import load_config
from data.functions import create_log_embed
from data.functions import response_to_class
#from data.functions import create_custom_message
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
    @Plugin.listen("GuildMemberAdd")
    def member_join_static(self, event):
        log_event = "USER_JOIN"
        guilds = load()
        guild_id = str(event.member.guild_id)
        user = event.member
        send_message = self.bot.client.api.client.channels_messages_create
        
        
        if guild_id not in guilds:
            return
        
        
        if len(guilds[guild_id]) == 0:
            return
        
        
        for log in guilds[guild_id]:
            if log_event in log["events"]:
                if log_event in log["data"]:
                    return
                    #TODO: Custom data handling as per custom processing
                    #create_custom_message(log)
            else:
                #TODO: Default event handling
                if log["type"] == "rich":
                    response = create_log_embed(log_event, event)
                    
                    send_message(int(log),
                                 content=response[0],
                                 embed=response[1])
                else:
                    send_message(int(log),
                                 response_to_class(log["type"], log_event))



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