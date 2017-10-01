import yaml
from data import responses
from data.storage import load
from data import storage

from disco.types.message import MessageEmbed
from datetime import datetime



log_types = {"rich":responses.fancy, "compact":responses.compact,
"fanceh":responses.fanceh}

def load_config():
    with open("config.yaml", 'r') as file:
        data = yaml.load(file)
    return data



def response_to_class(log_type, class_name):
    c = getattr(log_types[log_type], class_name)
    return c



def create_log_embed(event_type, event):
    guilds = load()
    log_message = response_to_class("rich", event_type)
    embed = MessageEmbed()
    
    content = log_message[0]
    if log_message[0] != None:
        content = log_message[0].format(e=event)
    
    embed.title = log_message[1]
    if log_message != None:
        embed.title = log_message[1].format(e=event)
    
    embed.description = log_message[2]
    if log_message[2] != None:
        embed.description = log_message[2].format(e=event)
    
    embed.footer.text = log_message[3]
    if log_message[3] != None:
        embed.footer.text = log_message[3].format(e=event)
    
    embed.url = log_message[4]
    if log_message[4] != None:
        embed.url = log_message[4].format(e=event)
    embed.color = log_message[5]
    return [content, embed]
    

        
#NOTE: permission checking #TODO: Add a role option.
def is_allowed(guild, user, perm_type="default", role="logger"):
    
    #Loading storage & config
    guilds = storage.load()
    config = load_config()
    
    #Assigning some variables
    guild_id = str(guild.id)
    user_id = user.id
    
    if perm_type == "default":
        if user_id == guild.owner.id:
            return True
        elif guild.get_permissions(user).to_dict()["manage_channels"]:
            return True
        return False
    elif perm_type == "global":
        if user_id in config["user"]["admin_ids"]:
            return True
        return False


#NOTE: silenced checking
def is_hushed(log_event, guild_id, channel_id, user_id):
    
    #loading storage
    guilds = storage.load()
    current_log_data = guilds[guild_id][channel_id]["data"]
    
    if log_event in current_log_data:
        if user_id in current_log_data[log_event]["ignored_users"]:
            return True
    else:
        if user_id in current_log_data["ignored_users"]:
            return True
        else:
            return False