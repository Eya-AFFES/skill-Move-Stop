# Copyright 2016 Mycroft AI, Inc.
#
# This file is part of Mycroft Core.
#
# Mycroft Core is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Mycroft Core is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Mycroft Core.  If not, see <http://www.gnu.org/licenses/>.

__author__ = 'Eya-AFFES'

from adapt.intent import IntentBuilder
#Import the IntentBuilder class from Adapt. 
#Adapt is an Intent-handling engine. Its job is to understand what a user Speaks to Mycroft, 
#and to pass that information to a Skill for handling.
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger
#Importing the required libraries. These 3 libraries will be required on every Skill

import serial
ser00 = serial.Serial ("/dev/ttyS0", 9600)    #Open port with baud rate

LOGGER = getLogger(__name__)
#This section starts logging of the Skill in the mycroft-skills.log file. 
#If you remove this line, your Skill will not log any errors, and you will have difficulty debugging.

class MoveStopSkill(MycroftSkill):
    def __init__(self):
        #This method is the constructor, and the key function it has is to define the name of the Skill.
        super(MoveStopSkill, self).__init__(name="MoveStopSkill")
        
    def initialize(self):
        #initialize()function defines each of the Intents of the Skill. Note that there are three Intents defined
        
        #three Intents defined in vocab files
        thank_you_intent = IntentBuilder("ThankYouIntent").require("ThankYouKeyword").build()
        self.register_intent(thank_you_intent, self.handle_thank_you_intent)

        how_are_you_intent = IntentBuilder("HowAreYouIntent").require("HowAreYouKeyword").build()
        self.register_intent(how_are_you_intent,self.handle_how_are_you_intent)

        hello_world_intent = IntentBuilder("HelloWorldIntent").require("HelloWorldKeyword").build()
        self.register_intent(hello_world_intent ,self.handle_hello_world_intent)

    def handle_hello_world_intent(self, message):
        # A method that handles the Intent hello_world_intent
        #2 parameters
        #self is the reference to the object itself
        #message is an incoming message from the messagebus
        self.speak_dialog("hello.world")
        #hello.world dialog is passed to the  speak_dialog() method
        #this is defined in the file “hello.world.dialog”
        msg="MVF"
        ser00.write(bytes(msg, 'utf-8')) 

    def handle_how_are_you_intent(self, message):
        # A method that handles the Intent how_are_you_intent
        self.speak_dialog("how.are.you")
        msg="MVB"
        ser00.write(bytes(msg, 'utf-8'))
        
    def handle_thank_you_intent(self, message):
        # A method that handles the Intent thank_you_intent
        self.speak_dialog("welcome")
        msg="ST"
        ser00.write(bytes(msg, 'utf-8')) 

    

    def stop(self):
        #This method tells Mycroft what to do if a stop intent is detected.
        #the pass statement is used as a placeholder; it doesn’t actually have any function. 
        #However, if the Skill had any active functionality, the stop() method would terminate 
        #the functionality, leaving the *Skill** in a known good state.
        pass


def create_skill():
    return MoveStopSkill()
