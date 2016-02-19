from alexa.ask.utils import VoiceHandler, ResponseBuilder as r
import riot as riot

"""
In this file we specify default event handlers which are then populated into the handler map using metaprogramming
Copyright Anjishnu Kumar 2015

Each VoiceHandler function receives a Request object as input and outputs a Response object 
A response object is defined as the output of ResponseBuilder.create_response()
"""

default_message = "Welcome to Summoner's Rift. What champion are you 
thinking of?"
default_message_reprompt = "What champion was that?"

help_message = "I will give you the title a League of Legends champion."
no_champion_message = "There is no champion by that name."

goodbye_message = "Goodbye!"

def default_handler(request):
    """ The default handler gets invoked if no handler is set for a request """
    return r.create_response(message=default_message, 
reprompt_message=default_message_reprompt)


@VoiceHandler(request_type="LaunchRequest")
def launch_request_handler(request):
    """
    Annoatate functions with @VoiceHandler so that they can be automatically mapped 
    to request types.
    Use the 'request_type' field to map them to non-intent requests
    """
    return r.create_response(message=default_message, 
reprompt_message=default_message_reprompt)


@VoiceHandler(request_type="SessionEndedRequest")
def session_ended_request_handler(request):
    return r.create_response(message=goodbye_message)


@VoiceHandler(intent='League')
def get_recipe_intent_handler(request):
    """
    Use the 'intent' field in the VoiceHandler to map to the respective intent.
    You can insert arbitrary business logic code here    
    """

    # Get variables like userId, slots, intent name etc from the 'Request' object
    champion_name = request.get_slot_value("ChampName") 
    title = riot.get_lore(champion_name)

    if(title = ''):
      return r.create_response(message=no_champion_message, 
end_session=True)
    else:
      return r.create_response(message=title, end_session=True)

    
@VoiceHandler(intent="AMAZON.HelpIntent")
def get_help_intent_handler(request):
  return r.create_response(message=help_message)
