# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"
from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import sqlite3
import smtplib
class LossWeightExercise(Action):
     def name(self) -> Text:
         return "lwe_exercise_chart"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         user_message = str((tracker.latest_message)['text'])

         if "Male" in user_message:
             exe_str = "These are some of your exercises that can help loss your weight-Deadlift,Situps,Burfees,Skipping,Barbell Squats, Clean and press,and normal cardio workout."
         elif 'Female' in user_message:
             exe_str = "These are some of your exercises that can help loss your weight-Cardio Endurance Workout, Treadmill,Cycling,skipping,pushupand many more."
         context_text=exe_str
         dispatcher.utter_message(text=context_text)

         return []

class GainWeightExercise(Action):

     def name(self) -> Text:
         return "gwe_exercise_chart"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

         user_message = str((tracker.latest_message)['text'])

         if "Male" in user_message:
             exe_str = "These are some of your exercises that can help loss your weight-Pull ups,tricep dips,Squats,Lunges,Bench-press,Over-head press."
         elif 'Female' in user_message:
             exe_str = "These are some of your exercises that can help loss your weight-Jumping Jacks,triceps dips,pushups,pullups."
         context_text=exe_str
         dispatcher.utter_message(text=context_text)

         return []

class BuildMuscleExercise(Action):

    def name(self) -> Text:
        return "bme_exercise_chart"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_message = str((tracker.latest_message)['text'])

        if "Male" in user_message:
            exe_str = "These are some of your exercises that can help loss your weight- chinups,Dumbell exercises,push ups,pull ups,Barbell bench Press."
        elif 'Female' in user_message:
            exe_str = "These are some of your exercises that can help loss your weight-Pushups,chinups,Dumbell exercise,pullups."
        context_text=exe_str
        dispatcher.utter_message(text=context_text)

        return []

class OrderReceivedFromUser(Action):

    def name(self) -> Text:

        return "details_received"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        user_message = str((tracker.latest_message)['text'])

        fromaddr = 'niraj81014@gmail.com'
        toaddrs = 'studyniraj123@gmail.com'
        msg = "Hello Royal Fitness club,This guy wants to know about your club.\n Here is the name and number please conact help whenever you are available:\n {} ".format(user_message)
        username = 'niraj81014@gmail.com'
        obj = open('pass.txt')
        password = obj.read()
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(username, password)
        server.sendmail(fromaddr, toaddrs, msg)
        server.quit()
        content_text = "Details Received. We will Contact you soon!!"
        dispatcher.utter_message(text=content_text)
        

        return []
