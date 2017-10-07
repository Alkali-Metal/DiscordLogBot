import json


guild_json_path = "data/guild_channels.json"



def load():
    with open(guild_json_path, 'r') as file:
        data = json.load(file)
    return data



def write(data):
    with open(guild_json_path, 'w') as file:
        file.write(json.dumps(data, indent=2))



def add_guild(guild_id):
    guilds = load()
    guilds[guild_id] = {}
    write(guilds)



def add_log(guild_id, channel_id, log_type="compact", events=[]):
    guilds = load()
    guilds[guild_id][channel_id] = {"type":log_type,
                                    "events":events,
                                    "data":{}
                                    }
    write(guilds)



def remove_log(guild_id, channel_id):
    guilds = load()
    guilds[guild_id].pop(channel_id)
    write(guilds)



def add_event(guild_id, channel_id, event, data=None):
    guilds = load()
    guilds[guild_id][channel_id].append(event)
    if data != None:
        guilds[guild_id][channel_id]["data"] = data
    write(guilds)



def delete_guild(guild_id):
    guilds = load()
    guild_id = str(guild_id)
    if guild_id in guilds:
        guild_data = guilds[guild_id]
        guilds.pop(guild_id)
        return guild_data