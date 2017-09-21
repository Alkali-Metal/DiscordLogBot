from data.guild_handling import load_guilds
import data.responses as log

from disco.bot import Plugin
from disco.api.client.APIClient import channels_messages_create as send


class LoggingPlugin(Plugin):
    
    
    #NOTE: Member Join Event
    @Plugin.listen("MessageDelete")
    def on_message_delete(self, event):
        guild_configs = load_guilds()
        guild_id = str(event.guild_id)
        channel_id = event.msg.channel_id
        log_event = "MESSAGE_DELETE"
        if guild_id in guild_configs.keys():
            guild_logs = guild_configs[guild_id]
            for channel in guild_logs:
                channel_settings = channel["events"]
                if log_event in channel_settings:
                    try:
                        send(self,
                             channel_id,
                             log.message_delete.format(
                                event.msg.author.name,
                                event.msg.author.id,
                                str(channel_id)
                                event.msg.content))
                    except:
                        print("Couldn't find log channel")
            global_log = guild_configs["global"]
            for channel in global_log["admin_logs"]:
                global_log = global_log["admin_logs"][str(channel)]
                if log_event in global_log["events"]:
                    try:
                        send(self,
                             channel_id,
                             log.message_delete.format(
                                event.msg.author.name,
                                event.msg.author.id,
                                str(channel_id)
                                event.msg.content))
                    except:
                        print("Couldn't find log channel")