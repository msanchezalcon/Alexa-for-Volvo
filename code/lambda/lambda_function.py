# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK for Python.
# Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
# session persistence, api calls, and more.
# This sample is built using the handler classes approach in skill builder.
import logging
import json
import random
import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# open and read the speech output file
with open("speech_strings.json") as speech_prompts:
    speech_data = json.load(speech_prompts)
with open("help_strings.json") as help_prompts:
    help_data = json.load(help_prompts)
help_speech = help_data['help']
#################


def has_subdialogue(handler_input):
    attr = handler_input.attributes_manager.session_attributes
    intent_name = attr['intent']
    state_number = str(attr['state'])
    has_substate = False
    try:
        substate = speech_data[intent_name][state_number]['subdialogue']
        has_substate = True

        return has_substate
    except KeyError:
        print("State has no subdialogue")

        return has_substate


def set_substate_attr(handler_input):
    """ Sets the session attributes for a substate when an intent is triggered """
    attr = handler_input.attributes_manager.session_attributes
    intent_name = handler_input.request_envelope.request.intent.name
    state_number = str(attr['state'])
    intent_name = attr['intent']

    # set attributes
    attr['substate'] = 1
    attr['maxsubstate'] = len(speech_data[intent_name]
                              [state_number]['subdialogue'])

    substate_number = str(attr['substate'])
    speak_output = speech_data[intent_name][state_number]['subdialogue'][substate_number]['speech']

    return speak_output


def set_attr(handler_input):
    """ Sets all session attributes when an intent is triggered """
    attr = handler_input.attributes_manager.session_attributes
    intent_name = handler_input.request_envelope.request.intent.name

    # set attributes
    attr['intent'] = intent_name
    attr['state'] = 1
    attr['maxstate'] = len(speech_data[intent_name])

    state_number = str(attr['state'])
    speak_output = speech_data[intent_name][state_number]['speech']

    return speak_output


def get_attr(handler_input):
    """ Gets the speech output for the current state"""
    attr = handler_input.attributes_manager.session_attributes
    intent_name = attr['intent']
    state_number = str(attr['state'])

    print("state number!! ", attr['state'])
    print("is type ", type(state_number))

    print("data-intentname-number:")
    print(speech_data[intent_name][state_number])
    print("data-intentname-number-speech:")
    print(speech_data[intent_name][state_number]['speech'])

    speak_output = speech_data[intent_name][state_number]['speech']

    return speak_output


def print_errors(handler_input):
    """ Print handler logs, errors etc """
    current_intent = handler_input.request_envelope.request.intent
    attr = handler_input.attributes_manager.session_attributes
    print("In handler for ")
    print(current_intent)
    print("Attributes")
    print(attr)


class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        speak_output = "Welcome to the driver's handbook. What would you like help with?"

        return (
            handler_input.response_builder
            .set_should_end_session(False)
            .speak(speak_output)
            .ask(speak_output)
            .response
        )


class ConnectToBluetoothIntentHandler(AbstractRequestHandler):
    """Handler for Connect to Bluetooth Intent."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_intent_name("ConnectToBluetoothIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        print_errors(handler_input)

        speak_output = set_attr(handler_input)

        return (
            handler_input.response_builder
            .set_should_end_session(False)
            .speak(speak_output)
            .response
        )


class CleanInformationDisplayIntentHandler(AbstractRequestHandler):
    """Handler for Connect to Clean Information Display Intent."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_intent_name("CleanInformationDisplayIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        print_errors(handler_input)

        speak_output = set_attr(handler_input)

        return (
            handler_input.response_builder
            .set_should_end_session(False)
            .speak(speak_output)
            .response
        )


class SetTargetFuelConsumptionIntentHandler(AbstractRequestHandler):
    """Handler for Set Target Fuel Consumption Intent."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_intent_name("SetTargetFuelConsumptionIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        print_errors(handler_input)

        speak_output = set_attr(handler_input)

        return (
            handler_input.response_builder
            .set_should_end_session(False)
            .speak(speak_output)
            .response
        )


class TurnOffHaloLightsIntentHandler(AbstractRequestHandler):
    """Handler for Turn Off Halo Lights Intent."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_intent_name("TurnOffHaloLightsIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        print_errors(handler_input)

        speak_output = set_attr(handler_input)

        return (
            handler_input.response_builder
            .set_should_end_session(False)
            .speak(speak_output)
            .response
        )


class AccessFusesAndRelaysForBodyworkIntentHandler(AbstractRequestHandler):
    """Handler for Access Fuses And Relays For Body work Intent."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_intent_name("AccessFusesAndRelaysForBodyworkIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        print_errors(handler_input)

        speak_output = set_attr(handler_input)

        return (
            handler_input.response_builder
            .set_should_end_session(False)
            .speak(speak_output)
            .response
        )


class ChangeFuseForRelayCentreIntentHandler(AbstractRequestHandler):
    """Handler for Change Fuse For Relay Centre Intent."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_intent_name("ChangeFuseForRelayCentreIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        print_errors(handler_input)

        speak_output = set_attr(handler_input)

        return (
            handler_input.response_builder
            .set_should_end_session(False)
            .speak(speak_output)
            .response
        )


class EmergencyStopIntentHandler(AbstractRequestHandler):
    """Handler for Emergency Stop Intent."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_intent_name("EmergencyStopIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        print_errors(handler_input)

        speak_output = set_attr(handler_input)

        return (
            handler_input.response_builder
            .set_should_end_session(False)
            .speak(speak_output)
            .response
        )


class CleanHeadlightsIntentHandler(AbstractRequestHandler):
    """Handler for Clean Headlights Intent."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_intent_name("CleanHeadlightsIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        print_errors(handler_input)

        speak_output = set_attr(handler_input)

        return (
            handler_input.response_builder
            .set_should_end_session(False)
            .speak(speak_output)
            .response
        )


class AcknowledgementIntentHandler(AbstractRequestHandler):
    """Handler for Acknowledgement Intent."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AcknowledgementIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        print_errors(handler_input)

        # Got next state
        attr = handler_input.attributes_manager.session_attributes
        attr['state'] += 1

        speak_output = get_attr(handler_input)

        if attr['state'] == attr['maxstate']:
            return (
                handler_input.response_builder
                .set_should_end_session(True)
                .speak(speak_output)
                .response
            )

        return (
            handler_input.response_builder
            .set_should_end_session(False)
            .speak(speak_output)
            .response
        )


class RepeatIntentHandler(AbstractRequestHandler):
    """Handler for Repeat Intent."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.RepeatIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In RepeatIntentHandler")
        print("In RepeatIntentHandler")

        speak_output = get_attr(handler_input)

        return (
            handler_input.response_builder
            .set_should_end_session(False)
            .speak(speak_output)
            .response
        )


class HowIntentHandler(AbstractRequestHandler):
    """Handler for How Intent."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("HowIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In HowIntentHandler")
        print("In HowIntentHandler")

        #speak_output = get_attr(handler_input)
        subdialogue = has_subdialogue(handler_input)

        if subdialogue == False:
            speak_output = "Sorry, I couldn't find an explaination for that."

        else:
            speak_output = set_substate_attr(handler_input)

        return (
            handler_input.response_builder
            .set_should_end_session(False)
            .speak(speak_output)
            .response
        )


class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        rand_help = (random.sample(help_speech, 3))
        speak_output = "You can ask me how to {}, {}, or {}".format(
            rand_help[0], rand_help[1], rand_help[2])

        return (
            handler_input.response_builder
            .speak(speak_output)
            .set_should_end_session(True)
            .ask(speak_output)
            .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        speak_output = "Closing the handbook."

        return (
            handler_input.response_builder
            .speak(speak_output)
            .set_should_end_session(True)
            .response
        )


class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.

        return (
            handler_input.response_builder
            .set_should_end_session(True)
            .response
        )


class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.
    """

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "You just triggered " + intent_name + "."

        return (
            handler_input.response_builder
            .speak(speak_output)
            # .ask("add a reprompt if you want to keep the session open for the user to respond")
            .response
        )


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """

    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speak_output = "Sorry, I had trouble doing what you asked. Please try again."

        return (
            handler_input.response_builder
            .speak(speak_output)
            .ask(speak_output)
            .response
        )

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.


sb = SkillBuilder()

# Launches the skill Driver's Handbook
sb.add_request_handler(LaunchRequestHandler())

# Handlers for intents we build from tasks
sb.add_request_handler(ConnectToBluetoothIntentHandler())
sb.add_request_handler(CleanInformationDisplayIntentHandler())
sb.add_request_handler(SetTargetFuelConsumptionIntentHandler())
sb.add_request_handler(TurnOffHaloLightsIntentHandler())
sb.add_request_handler(AccessFusesAndRelaysForBodyworkIntentHandler())
sb.add_request_handler(ChangeFuseForRelayCentreIntentHandler())
sb.add_request_handler(EmergencyStopIntentHandler())
sb.add_request_handler(CleanHeadlightsIntentHandler())

# Handler for when user replies
sb.add_request_handler(AcknowledgementIntentHandler())
sb.add_request_handler(RepeatIntentHandler())
sb.add_request_handler(HowIntentHandler())


sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
# make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers
sb.add_request_handler(IntentReflectorHandler())

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()
