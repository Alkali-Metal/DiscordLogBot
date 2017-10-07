@Plugin.listen("")
def on_mention(self, event):


    #Assigning some variables.
    guilds = load()
    admin_event = False
    user_event = False
    event_type = ""
    guild_id = str(event.guild.id)
    send_message = self.bot.client.api.channels_messages_create
    data = {"guild_data":guilds[guild_id]}


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