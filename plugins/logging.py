from data.storage import load
from data.storage import delete_guild
from data.functions import load_config
from data.functions import create_log_embed
from data.functions import response_to_class

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
    @Plugin.listen("WebhooksUpdate")
    def on_mention_everyone(self, event):


        #Assigning some variables.
        guilds = load()
        admin_event = False
        user_event = False
        event_type = ""
        guild_id = str(event.guild.id)
        send_message = self.bot.client.api.channels_messages_create
        #data = {"guild_data":guilds[guild_id]}


        #Checking if user event
        if user_event:
            
            #Checking the guilds
            if guild_id in guilds:
                guild_logs = guilds[guild_id]
                
                #Cycling through the guild logs
                for channel in guild_logs:
                    
                    #Making sure the log actually logs the event
                    if event_type in guild_logs[channel]["events"]:
                        log_type = guild_logs[channel]["type"]
                        
                        #Check the log type
                        if log_type != "rich":
                            
                            #log it
                            send_message(int(channel),
                                         response_to_class(log_type,
                                                           event_type).format(
                                                                          event,
                                                                          data))
                        else:
                            
                            #get the response list
                            response = create_log_embed(event_type,
                                                        event)
                            
                            #log it
                            send_message(int(channel),
                                         content=response[0],
                                         embed=response[1])


        #Checking admin event
        if admin_event:
            
            #Cycling through the admin logs
            for log in guilds["admin_logs"]:
                
                #checking if the log logs it.
                if event_type in guilds["admin_logs"][log]:
                    log_type = guilds["admin_logs"][log]["type"]
                    
                    #Check the log type
                    if log_type != "rich":
                        
                        #log it
                        send_message(int(channel),
                                     response_to_class(log_type,
                                                       event_type).format(
                                                                      event,
                                                                      data))
                    else:
                        
                        #get the response list
                        response = create_log_embed(event_type,
                                                    event)
                        
                        #log it
                        send_message(int(channel),
                                     content=response[0],
                                     embed=response[1])


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
    @Plugin.listen("GuildRoleCreate")
    def on_role_create(self, event):


        #Assigning some variables.
        guilds = load()
        admin_event = False
        user_event = True
        event_type = "ROLE_CREATE"
        guild_id = str(event.guild.id)
        send_message = self.bot.client.api.channels_messages_create
        #data = {"guild_data":guilds[guild_id]}


        #Checking if user event
        if user_event:
            
            #Checking the guilds
            if guild_id in guilds:
                
                guild_logs = guilds[guild_id]
                
                #Cycling through the guild logs
                for channel in guild_logs:
                    
                    #Making sure the log actually logs the event
                    if event_type in guild_logs[channel]["events"]:
                        
                        log_type = guild_logs[channel]["type"]
                        
                        #Check the log type
                        if log_type != "rich":
                            
                            #log it
                            send_message(int(channel),
                                         response_to_class(log_type,
                                                           event_type).format(
                                                                          event,
                                                                          data))
                        else:
                            
                            
                            #get the response list
                            response = create_log_embed(event_type,
                                                        event)
                            
                            #log it
                            send_message(int(channel),
                                         content=response[0],
                                         embed=response[1])


        #Checking admin event
        if admin_event:
            
            #Cycling through the admin logs
            for log in guilds["admin_logs"]:
                
                #checking if the log logs it.
                if event_type in guilds["admin_logs"][log]:
                    log_type = guilds["admin_logs"][log]["type"]
                    
                    #Check the log type
                    if log_type != "rich":
                        
                        #log it
                        send_message(int(channel),
                                     response_to_class(log_type,
                                                       event_type).format(
                                                                      event,
                                                                      data))
                    else:
                        
                        #get the response list
                        response = create_log_embed(event_type,
                                                    event)
                        
                        #log it
                        send_message(int(channel),
                                     content=response[0],
                                     embed=response[1])
    
    
    
    #TODO: Role Updated
    #TODO: Role Deleted
    @Plugin.listen("GuildRoleDelete")
    def on_role_delete(self, event):


        #Assigning some variables.
        guilds = load()
        admin_event = False
        user_event = True
        event_type = "ROLE_DELETE"
        guild_id = str(event.guild.id)
        send_message = self.bot.client.api.channels_messages_create
        #data = {"guild_data":guilds[guild_id]}


        #Checking if user event
        if user_event:
            
            #Checking the guilds
            if guild_id in guilds:
                
                guild_logs = guilds[guild_id]
                
                #Cycling through the guild logs
                for channel in guild_logs:
                    
                    #Making sure the log actually logs the event
                    if event_type in guild_logs[channel]["events"]:
                        
                        log_type = guild_logs[channel]["type"]
                        
                        #Check the log type
                        if log_type != "rich":
                            
                            #log it
                            send_message(int(channel),
                                         response_to_class(log_type,
                                                           event_type).format(
                                                                          event,
                                                                          data))
                        else:
                            
                            
                            #get the response list
                            response = create_log_embed(event_type,
                                                        event)
                            
                            #log it
                            send_message(int(channel),
                                         content=response[0],
                                         embed=response[1])


        #Checking admin event
        if admin_event:
            
            #Cycling through the admin logs
            for log in guilds["admin_logs"]:
                
                #checking if the log logs it.
                if event_type in guilds["admin_logs"][log]:
                    log_type = guilds["admin_logs"][log]["type"]
                    
                    #Check the log type
                    if log_type != "rich":
                        
                        #log it
                        send_message(int(channel),
                                     response_to_class(log_type,
                                                       event_type).format(
                                                                      event,
                                                                      data))
                    else:
                        
                        #get the response list
                        response = create_log_embed(event_type,
                                                    event)
                        
                        #log it
                        send_message(int(channel),
                                     content=response[0],
                                     embed=response[1])
    
    
    
    #TODO: Member Presence Update
    #TODO: Voice State Updated
    #TODO: Voice Server Updated
    #TODO: Webhooks Updated
    #TODO: Non-Bot Embeds