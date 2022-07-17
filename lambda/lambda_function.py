# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK for Python.
# Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
# session persistence, api calls, and more.
# This sample is built using the handler classes approach in skill builder.
import logging
import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_model.interfaces.audioplayer import (
    PlayDirective, PlayBehavior, AudioItem, Stream, AudioItemMetadata,
    StopDirective, ClearQueueDirective, ClearBehavior)

from ask_sdk_model import Response
from ask_sdk_model import Request, Response
import utils, data

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = str(data.WELCOME_MESSAGE) + str(data.GAMES)

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class AvantiUnAltroIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AvantiUnAltroIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Respons

        # logger.info("Avanti un altro Handler")
        session_attr = handler_input.attributes_manager.session_attributes
        session_attr["counter"] = 0
        session_attr["game_type"] = 0
        session_attr['questions'] = []
        session_attr['questions'] = utils.get_random_list_question()

        speak_output = str(data.START_1_GAME) + str(session_attr['questions'][session_attr['counter']]['question'])
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class SemanticGameIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("SemanticGameIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Respons
        session_attr = handler_input.attributes_manager.session_attributes
        session_attr['game_type'] = 1
        session_attr['counter'] = 0
        session_attr['score'] = 0
        session_attr['semantic_list'] = []
        session_attr['wrong_list'] = []
        quiz_list = []
        wrong_list = []
        i = 0
        while i <= data.MAX_QUIZ:
            _, __ = utils.create_semantic_list()
            quiz_list.append(_)
            wrong_list.append(__[0])
            i += 1
        session_attr['semantic_list'] = quiz_list
        session_attr['wrong_list'] = wrong_list

        speak_output = str(data.START_2_GAME)  # Leggo info sul gioco

        for i, _ in enumerate(session_attr['semantic_list'][session_attr['counter']]):
            speak_output += _
            if i < len(session_attr['semantic_list'][session_attr['counter']]) - 1:
                speak_output += ", "
        return (
            handler_input.response_builder
                .speak(str(speak_output))
                .ask(str(speak_output))
                .response
        )


class QuizAnswerHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("QuizAnswerIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Respons

        # logger.info("Avanti un altro Handler")
        session_attr = handler_input.attributes_manager.session_attributes
        if session_attr['game_type'] == 0:
            correct_answer = str(session_attr['questions'][session_attr['counter']]['correct']).lower()
            slot = ask_utils.request_util.get_slot(handler_input, "response")
            if slot.value:
                answer = str(slot.value).lower()
            else:
                answer = "boh"

            if answer == correct_answer:
                session_attr["counter"] += 1
                if session_attr['counter'] >= data.MAX_QUESTIONS:
                    speak = data.EXIT_SUCCESS_SKILL_MESSAGE + data.PLAY_AGAIN
                    session_attr['game_type'] = -1
                    return handler_input.response_builder.speak(speak).ask(speak).response
            else:
                session_attr["counter"] = 0

            return handler_input.response_builder.speak(
                session_attr['questions'][session_attr["counter"]]['question']).ask(
                session_attr['questions'][session_attr["counter"]]['question']).response

        if session_attr['game_type'] == 1:
            correct_answer = str(session_attr['wrong_list'][session_attr['counter']]).lower()
            slot = ask_utils.request_util.get_slot(handler_input, "response")
            if slot.value:
                answer = str(slot.value).lower()
            else:
                answer = "boh"
            speak = ""
            if answer == correct_answer:
                session_attr['score'] += 1
                session_attr['counter'] += 1
                speak = "Corretta! "
            else:
                session_attr['counter'] += 1
                speak = "Sbagliata! "

            if session_attr['counter'] >= data.MAX_QUIZ:
                session_attr['game_type'] = -1
                speak += "Hai risposto correttamente a " + str(session_attr['score']) + " su " + str(data.MAX_QUIZ)
                speak += data.PLAY_AGAIN
            else:
                for word in session_attr['semantic_list'][session_attr['counter']]:
                    speak += word + ", "
                speak = speak[:-2]

            return handler_input.response_builder.speak(speak).ask(speak).response
        if session_attr['game_type'] == -1:
            speak = "A cosa vuoi giocare?"
            return handler_input.response_builder.speak(speak).ask(speak).response


class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        return (
            handler_input.response_builder
                .speak(data.HELP)
                .ask(data.HELP)
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
        return (
            handler_input.response_builder
                .speak("Ciao")
                .response
        )


class FallbackIntentHandler(AbstractRequestHandler):
    """Single handler for Fallback Intent."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.FallbackIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        logger.info("In FallbackIntentHandler")
        speech = "Hmm, I'm not sure. You can say Hello or Help. What would you like to do?"
        reprompt = "I didn't catch that. What can I help you with?"

        return handler_input.response_builder.speak(speech).ask(reprompt).response


class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""

    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.

        return handler_input.response_builder.response


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
        speak_output = "Hai avviato " + intent_name + "."

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
        return (
            handler_input.response_builder
                .speak(data.FALLBACK_ANSWER)
                .ask(data.FALLBACK_ANSWER)
                .response
        )


# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.


sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(AvantiUnAltroIntentHandler())
sb.add_request_handler(SemanticGameIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(FallbackIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(QuizAnswerHandler())
sb.add_request_handler(
    IntentReflectorHandler())  # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()
