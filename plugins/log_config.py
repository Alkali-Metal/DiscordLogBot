from data import storage
from data import responses as response
from data.functions import load_config
from data.functions import is_allowed

from disco.bot import Plugin
import disco


admin_events = {"GUILD_CREATE", "GUILD_DELETE", "GUILD_LEAVE"}
user_events = {
"BOT_LOG_CREATE","BOT_LOG_DELETE","BOT_EVENT_ADD","BOT_EVENT_REMOVE",
"BOT_EVENT_DATA","GUILD_UPDATE","USER_JOIN","USER_LEAVE","USER_UPDATE",
"MESSAGE_EDIT","MESSAGE_DELETE","MENTION_EVERYONE","TTS_USAGE","REACTION_ADD",
"REACTION_REMOVE","REACTION_REMOVE_ALL","INVITE_CREATE","INVITE_DELETE",
"VOICE_CHANNEL_CREATE","VOICE_CHANNEL_UPDATE","VOICE_CHANNEL_DELETE",
"TEXT_CHANNEL_CREATE","TEXT_CHANNEL_UPDATE","TEXT_CHANNEL_DELETE","PINS_UPDATE",
"BAN_ADD","BAN_REMOVE","EMOJI_UPDATE","INTEGRATION_UPDATE", "ROLE_CREATE",
"ROLE_UPDATE","ROLE_DELETE","USER_PRESENCE_UPDATE","USER_VOICE_JOIN",
"USER_VOICE_LEAVE","VOICE_SERVER_UPDATE","WEBHOOK_CREATE","WEBHOOK_UPDATE",
"WEBHOOK_DELETE","NON-BOT_EMBED","USER_JOIN_RANDOM"
}



class LoggingCommands(Plugin):    
    
    #NOTE: event add command
    @Plugin.command("add", group="event")
    def add_event(self, event):
        if len(event.args) >= 1:
            
            #Loading the storage
            guilds = storage.load()
            
            #Setting some variables
            guild_id = str(event.guild.id)
            channel_id = str(event.msg.channel_id)
            not_log_events = []
            already_logging = []
            added_log_events = []
            
            #Checking permissions
            if not is_allowed(guild=event.msg.guild, user=event.msg.author):
                return event.msg.reply(response.command.invalid_permissions)
            
            #Make sure the channel is a log channel
            if channel_id not in guilds[guild_id]:
                return event.msg.reply(response.command.not_log_event)
            
            #Make sure the log event is valid
            for log_event in event.args:
                log_event = log_event.upper()
                if log_event not in user_events:
                    not_log_events.append(log_event)
                elif log_event in guilds[guild_id][channel_id]["events"]:
                    already_logging.append(log_event)
                else:
                    guilds[guild_id][channel_id]["events"].append(log_event)
                    added_log_events.append(log_event)
            storage.write(guilds)
            if len(added_log_events) > 0:
                event.msg.reply(response.command.added_log_events.format(
                                                 "`, `".join(added_log_events)))
            if len(already_logging) > 0:
                event.msg.reply(response.command.already_logging.format(
                                                  "`, `".join(already_logging)))
            if len(not_log_events) > 0:
                event.msg.reply(response.command.not_log_events.format(
                                                   "`, `".join(not_log_events)))
        else:
            return event.msg.reply(response.not_enough_arguments)


    #NOTE: event list command
    @Plugin.command("list", group="event")
    def list_events(self, event):
        
        #Loading the storage
        guilds = storage.load()
        
        #Assigning some variables
        guild_id = str(event.guild.id)
        channel_id = str(event.msg.channel_id)
        
        #Checking permissions
        if not is_allowed(guild=event.msg.guild, user=event.msg.author):
            return event.msg.reply(response.command.invalid_permissions)
        
        #Ensuring the channel is a logging channel
        if channel_id not in guilds[guild_id]:
            return event.msg.reply(response.command.no_event_list)
        
        #Sending the channel list to chat.
        events = ", ".join(guilds[guild_id][channel_id]["events"])
        return event.msg.reply(response.command.event_list.format(events))


    #NOTE: log type command
    @Plugin.command("type", group="log", aliases=["style"])
    def log_type(self, event):
        
        #Assigning some variables
        guilds = storage.load()
        guild_id = str(event.guild.id)
        channel_id = str(event.msg.channel_id)
        log_types = {"simple":"compact",
        "plain":"compact",
        "boring":"compact",
        "compact":"compact",
        "worst":"compact",
        "better":"fanceh",
        "fanceh":"fanceh",
        "fancy-ish":"fanceh",
        "fancy":"rich",
        "rich":"rich",
        "best":"rich"}
        
        #Permission checking
        if not is_allowed(guild=event.msg.guild, user=event.msg.author):
            event.msg.reply(response.command.invalid_permissions)
        
        #Checking the guild for data
        if guild_id not in guilds:
            return event.msg.reply(response.command.no_guild_data)
        
        #Checking if the channel is a log
        if channel_id not in guilds[guild_id]:
            return event.msg.reply(response.command.not_log)
        
        #Make sure they supplied an argument
        if len(event.args):
            if event.args[0] in log_types:
                
                #Check if the log is already that style
                if log_types[event.args[0]] == guilds[guild_id][channel_id]["type"]:
                    return event.msg.reply(response.command.already_log_type)
                
                
                guilds[guild_id][channel_id]["type"] = log_types[event.args[0]]
                storage.write(guilds)
                event.msg.reply(response.command.changed_log_type.format(
                                                      log_types[event.args[0]]))
        else:
            event.msg.reply(response.command.not_enough_arguments)
    

    #NOTE: log create command
    @Plugin.command("create", group="log", aliases=["add"])
    def add_log(self, event):
        
        #Load the storage
        guilds = storage.load()
        
        #Setting some variables
        guild_id = str(event.msg.guild.id)
        channel_id = str(event.msg.channel_id)
        
        #Checking permissions
        if not is_allowed(guild=event.msg.guild, user=event.msg.author):
            return event.msg.reply(response.command.invalid_permissions)
        
        #Add the guild if they are not in the database then reload the database
        if guild_id not in guilds:
            storage.add_guild(guild_id)
        guilds = storage.load()
        
        #Erroring if the channel is already a log
        if channel_id in guilds[guild_id]:
            return event.msg.reply(response.command.already_log)
        else:
            storage.add_log(guild_id, channel_id)
            return event.msg.reply(response.command.log_added)




    #NOTE: log delete command
    @Plugin.command("delete", group="log", aliases=["remove", "rem"])
    def remove_log(self, event, channel_id=None):
        
        #Load the storage
        guilds = storage.load()
        
        #Setting some variables
        guild_id = str(event.guild.id)
        channel_id = str(event.msg.channel_id)
        
        #Checking permissions
        if not is_allowed(guild=event.msg.guild, user=event.msg.author):
            return event.msg.reply(response.command.invalid_permissions)
        
        #Make sure the guild is in the database
        if guild_id not in guilds:
            return event.msg.reply(response.command.no_guild_data)
        
        if channel_id not in guilds[guild_id]:
            return event.msg.reply(response.command.not_log_remove)
        else:
            storage.remove_log(guild_id, channel_id)
            return event.msg.reply(response.command.log_removed)
    
    
    #NOTE: log list command
    @Plugin.command("list", group="log")
    def log_list(self, event):
        
        #loading storage
        guilds = storage.load()
        
        #Assigning some variables
        guild_id = str(event.guild.id)
        
        #Checking permissions
        if not is_allowed(guild=event.msg.guild, user=event.msg.author):
            return event.msg.reply(response.command.invalid_permissions)
        
        #Creating and sending the message
        logs = "<#" + ">, <#".join(guilds[guild_id].keys()) + ">"
        event.msg.reply(response.command.log_list.format(logs))