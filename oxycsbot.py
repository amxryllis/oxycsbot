#!/usr/bin/env python3
"""A simple chatbot that utilizes Cognitive Behavioral Therapy to help first-generation students
with distressing thoughts of their first year of college."""

from chatbot import ChatBot
import secrets
import random


class CBTBot(ChatBot):
    """A chatbot that uses CBT techniques to unravel discomforting thoughts."""

    "CD = Cognitive Distortion"
    "CB = Core Belief"

    STATES = [
        'waiting',
        'specific_emotion',
        'unknown_emotion',
        'specific_scenario',
        'unknown_scenario',
        'confused_scenario',
        'find_campus_help',
        'breathing1',
        'breathing2',
        'breathing3',
        'breathing_confused2',
        'breathing_confused3',
        'unknown_cd',
        'specific_cd',
        'challenge_emotion',
        'cd_wave2',
        'cd_wave3',
        'find_campus_help',
        'confused_campus_help',
        'specific_area',
        'check_feeling',
        'breathing'
    ]

    TAGS = {
        # intent
        'help': 'help',
        'feel': 'help',
        'am': 'help',
        '': 'help',
        'hello':'help',
        'hi':'help',

        'roommate': 'moment',
        'roommates': 'moment',
        'homesick': 'moment',
        'home': 'moment',
        'lost': 'moment',
        'academic': 'moment',
        'hard': 'moment',
        'alone': 'moment',

        # emotions
        'anxiety': 'anxious',
        'anxious': 'anxiety',
        'homesick': 'homesick',
        'isolated': 'isolation',
        'isolation': 'isolated',
        'worthless': 'worthless',
        'worried': 'worry',
        'worry': 'worried',
        'sad': 'sad',
        'depressed': 'depressed',
        'scared': 'scared',
        'tired': 'tired',
        'annoyed': 'annoyed',
        'angry': 'angry',
        'unprepared': 'unprepared',
        'emptiness': 'empty',
        'empty': 'emptiness',
        'lost': 'lost',

        #cogntive distortions
        'filtering': 'filtering',
        'polarized thinking': 'polarized thinking',
        'control fallacies': 'control fallacies',
        'fallacy of fallacies': 'fallacy of fallacies',
        'overgeneralization': 'overgeneralization',
        'emotional reasoning': 'emotional reasoning',
        'fallacy of change': 'fallacy of change',
        'shoulds': 'should statement',
        'catastrophizing': 'catastrophizing',
        'heavens reward fallacy': 'heavens reward fallacy',
        'always being right': 'always being right',
        'personalization': 'personalization',
        'jump to conclusions': 'jump to conclusions',
        'blaming': 'blaming',
        'global labeling': 'global labeling',
        # filtering, interpersonal fallacy, catastrophizing, overgeneralization, personalization,
        # emotional reasoning, should statement

        # generic
        'thanks': 'thanks',
        'okay': 'success',
        'bye': 'success',
        'yes': 'yes',
        'yep': 'yes',
        'no': 'no',
        'nope': 'no',
        "y": "y",
        "I am": "I am",
        "i am": "I am",
        "iam": "I am",
        "Iam": "I am",

        #scenarios
        'roommates': 'roommate',
        'room mate': 'roommate',
        'roommate': 'roommate',
        'living': 'roommate',
        'homesick': 'homesick',
        'home': 'home',
        'lost': 'lost',
        'academic': 'academic',
        'hard': 'hard',
        'alone': 'alone',
        'imposter': 'imposter',
        'not smart': 'imposter',
        'dumb': 'imposter',
        'deserve': 'imposter',

        #cognitive distortion
        'class': 'filtering',
        'classes': 'filtering',
        'grade': 'filtering',
        'grades': 'filtering',
        'friends': 'interpersonal fallacy',
        'other people': 'interpersonal fallacy',
        'never':'catastrophizing',
        'everyone': 'overgeneralization',
        'different': 'interpersonal fallacy',
        'stupid': 'interpersonal fallacy',
        'smarter': 'personalization',
        'not enough': 'emotional reasoning',
        'not prepared': 'emotional reasoning',
        'imposter': 'filtering',
        'unlovable': 'personalization',
        'abnormal': 'personalization',
        'not confident': 'emotional reasoning',
        'should': 'should statement',
        'succeed': 'catastrophizing',
        'success': 'catastrophizing',
        'job': 'catastrophizing',
        'internship': 'catastrophizing',
        'weird': 'interpersonal fallacy',
        'judge': 'interpersonal fallacy',
        'drop out': 'catastrophizing',
        'wrong': 'personalization',
        'undermine': 'emotional reasoning',
        'not capable': 'overgeneralization',
        "don't believe": 'emotional reasoning',

        'religious': 'religious',
        'cultural': 'cultural',
        'academic': 'academic',
        'personal': 'personal',
        'residential': 'residential',

        'religious': 'religious',
        'race': 'race' ,
        'different': 'different',
        'academic': 'academic',
        'social': 'social',
        'friends': 'friends',
        'cultural': 'cultural',


    }

    EMOTIONS = [
        'anxiety',
        'homesick',
        'isolated',
        'worthless',
        'worried',
        'sad',
        'scared',
        'tired',
        'annoyed',
        'angry',
        'unprepared',
        'empty',
        'lost'
    ]

    SCENARIOS = [
        'roommate',
        'homesick',
        'class',
        'home',
        'lost',
        'academic',
        'hard',

        'religious',
        'race',
        'different',
        'academic',
        'social',
        'friends',
        'cultural',


    ]

    CD = {
        'filtering',
        'polarized thinking',
        'control fallacies',
        'fallacy of fallacies',
        'overgeneralization',
        'emotional reasoning',
        'fallacy of change',
        'shoulds',
        'catastrophizing',
        'heavens reward fallacy',
        'always being right',
        'personalization',
        'jump to conclusions',
        'blaming',
        'global labeling',


    }

    ASSIGNMENTS = {'going to a place of worship.', 'volunteering for a cause you believe in.', 'going to the park.',
                   'going for a walk.', 'going out for dinner.', 'calling friends and/or family.',
                   'going out with friends and/or family.', 'working out.', 'getting immersed in art.', 'dancing.',
                   'singing.', 'watching your favorite movie.', 'journaling your thoughts.'}


    def __init__(self):
        """Initialize the OxyCSBot.

        The `emotion` member variable stores whether the target emotion has
        been identified.
        """
        super().__init__(default_state='waiting')
        self.emotion = None

    def get_emotion(self, emotion):
        """Find the office hours of a professor.

        Arguments:
            emotion (str): The emotion of interest.

        Returns:
            str: The office hours of that professor.
        """
        responses = {
            'anxiety': 'Im sorry that you feel this way. Can you give us an example of when you felt anxious?',
            'homesick': "Being away from your support system is challenging. What about campus life makes you miss home?",
            'isolated': "I hear your point; college is very different from what we're used to. What are times that you feel isolated?",
            'worthless': "I know that this isn't an easy topic. I appreciate you for sharing. What makes you feel this way? ",
            'worried': "This is a stressful time for many students. What makes you worry?",
            'sad': "Why?",
            'scared': "I want you to know that your feelings are valid. What makes you scared?",
            'tired': "There are many adjustments when transitioning to college that can make people feel worn down. Do you find yourself constantly tired or only after certain events?",
            'annoyed': "What are some things that makes you feel this way?",
            'angry': "It is understandable to have moments of anger, but remember that it is healthy to get rid of this anger. What makes you angered?",
            'unprepared': '\n'.join
                    ("Transitioning to college can be a big step up, so it is common to feel like you are not prepared. "
                    "Are there certain times that make you feel unprepared or do you always feel this way?"),
            'empty': "Remember that you are an incredible human being full of unique experiences that make you ‘you’. Have you felt this way before or did something happen that made you feel empty?",
            'lost': "You don’t need to have every aspect of your life planned out, remember that college is a time of exploration and discovery. What makes you feel lost?",
            'bad': "It is normal to feel bad sometimes, but remember to not let it define your day. Did a certain event happen that made you feel bad?",

        }
        return responses[emotion]

    # filtering, interpersonal fallacy, catastrophizing, overgeneralization, personalization,
    # emotional reasoning, should statement

    def get_cd(self, cd):
        """Find the office hours of a professor.

        Arguments:
            cd (str): The emotion of interest.

        Returns:
            str: The office hours of that professor.
        """
        responses = {
            'filtering': 'I understand. Its important to remember that theres a wider scope to things. Do you think that you often forget about the positive aspects of day to day frustrations?',
            'interpersonal fallacy': 'You seem to be a hard worker. Its easy to forget to direct energy back to your wellbeing. Is comparing yourself to others a common occurrence?',
            'catastrophizing': 'I see. When things dont go our way, we often question if this happened because of us. These moments arent bad nor are they wrong. Do you often overthink worst scenarios?',
            'overgeneralization': 'Your feelings are valid. Theres a Japanese saying, ichi-go ichi-e. Every moment is unique and unrepeatable. Not all mistakes are bad and can predict other unique scenarios you find yourself in. Do you often think that one mistake is indicative of your abilities?',
            'personalization': 'Sometimes things are out of your control. And that is completely ok. No one deserves to take on the weight of the world singlehandedly. Do you often find yourself blaming yourself for external occurrences?',
            'emotional reasoning': 'A key part of Cognitive Behavioral Therapy is shaping your thoughts to healthily affect your actions and behavior. Do you often feel like you negatively assume others intentions?',
            'should statement': 'Setting healthy goals is important. If you feel like you SHOULD always be doing something, your thoughts may end up punishing yourself beforehand. Do you often set up strict expectations for yourself?',
        }
        return responses[cd]

    def get_campus_help(self, area):
        responses = {
        'religious': 'The folks over at the Herrick Interfaith Center host several groups that foster a community within different religions and beliefs.',
        'cultural': 'If you head over to SLICE, Student Leadership, Involvement, & Community Engagement, they can redirect you to clubs on campus that foster communities within cultural groups. You can also reach out to Oxy students of an interest you dont find represented.',
        'academic': 'Your professor is a great resource. Oxys education emphasizes the bond between student and professor. If you cant find help from them, there are student peer learners that can help you with a class your struggling.',
        'personal': 'The Emmons center houses professional therapists and workers that serve as helpful, confidential ears. Theyre here to help. They offer FREE sessions.',
        'residential': 'The Office of Residential Education can help you sort out any insecurities you may have with your housing. Room swap is a process several Oxy students utilize to switch to different dorms that better fit them.',
        }
        return responses[area]



    # "waiting" state functions

    def respond_from_waiting(self, message, tags):
        """Decide what state to go to from the "waiting" state.

        Parameters:
            message (str): The incoming message.
            tags (Mapping[str, int]): A count of the tags that apply to the message.

        Returns:
            str: The message to send to the user.
        """
        self.emotion = None
        if 'help' in tags:
            for emotion in self.EMOTIONS:
                if emotion in tags:
                    self.emotion = emotion
                    return self.go_to_state('specific_emotion')
            return self.go_to_state('unknown_emotion')
        else:
            return self.finish('confused')

    # "specific_emotion" state functions

    def on_enter_specific_emotion(self):
        """Send a message when entering the "specific_emotion" state."""
        response = [
            f"{self.get_emotion(self.emotion)}"
        ]
        return response

    def respond_from_specific_emotion(self, message, tags):
        """Decide what state to go to from the "specific_faculty" state.

        Parameters:
            message (str): The incoming message.
            tags (Mapping[str, int]): A count of the tags that apply to the message.

        Returns:
            str: The message to send to the user.
        """
        self.scenario = None
        for scenario in self.SCENARIOS:
            if scenario in tags:
                self.scenario = scenario
                return self.go_to_state('specific_scenario')
            else:
                return self.finish_confused()

            return self.finish_confused()


    def on_enter_unknown_emotion(self):
        """Send a message when entering the "unknown_faculty" state."""
        return "I see. Could you elaborate on what you're feeling now?"

    def respond_from_unknown_emotion(self, message, tags):
        """Decide what state to go to from the "unknown_faculty" state.

        Parameters:
            message (str): The incoming message.
            tags (Mapping[str, int]): A count of the tags that apply to the message.

        Returns:
            str: The message to send to the user.
        """

        for emotion in self.EMOTION:
            if emotion in tags:
                self.emotion = emotion
                return self.go_to_state('specific_scenario')
        return self.go_to_state('specific_scenario')

    # "unrecognized_faculty" state functions

    def on_enter_specific_scenario(self):
        """Send a message when entering the "specific_scenario" state."""
        response = '\n'.join([
            " Ok. It is good to understand a specific time that you felt this way."
            ' Lets dive into what makes you feel this way. '
            ' What core beliefs are instilled in these times in your life?'
            # f"{self.professor.capitalize()}'s office hours are {self.get_office_hours(self.professor)}",
            # 'Do you know where their office is?',
        ])
        return response

    def respond_from_specific_scenario(self, message, tags):
        for cd in self.CD:
            if cd in tags:
                self.cd = cd
                return self.go_to_state('specific_cd')
        return self.go_to_state('cd_wave2')


    def on_enter_specific_cd(self):
        """Send a message when entering the "unrecognized_faculty" state."""
        return self.get_cd(self.cd)

    def respond_from_specific_cd(self, message, tags):
        """Decide what state to go to from the "unrecognized_faculty" state.

        Parameters:
            message (str): The incoming message.
            tags (Mapping[str, int]): A count of the tags that apply to the message.

        Returns:
            str: The message to send to the user.
        """

        if 'yes' in tags:
            return self.go_to_state('challenge_emotion')
        else:
            return self.go_to_state('cd_wave2')

    def on_enter_challenge_emotion(self):
        """Send a message when entering the "unrecognized_faculty" state."""
        return ' '.join([
            "Think of a time of where you felt the opposite. You felt loved, confident, and you felt others saw you in this light. Describe any time where you felt smart, capable and loved. ",
            "Or describe a time where you felt loved and respected by others. Start with 'I am'.",
        ])

    def respond_from_challenge_emotion(self, message, tags):
        """Decide what state to go to from the "unrecognized_faculty" state.

        Parameters:
            message (str): The incoming message.
            tags (Mapping[str, int]): A count of the tags that apply to the message.

        Returns:
            str: The message to send to the user.
        """
        if "I am" in tags:
            return self.go_to_state('check_feeling')
        else:
            return self.finish('breathing')

    def on_enter_cd_wave2(self):
        """Send a message when entering the "unrecognized_faculty" state."""
        return "Expanding on our core beliefs can help expose what thought patterns sway us to feel bad about ourselves. Could you state a belief you hold close to you? Such as comparing yourself or undermining your capabilities?"

    def respond_from_cd_wave2(self, message, tags):
        """Decide what state to go to from the "unrecognized_faculty" state.

        Parameters:
            message (str): The incoming message.
            tags (Mapping[str, int]): A count of the tags that apply to the message.

        Returns:
            str: The message to send to the user.
        """
        for cd in self.CD:
            if cd in tags:
                self.cd = cd
                return self.go_to_state('specific_cd')
        return self.go_to_state('unknown_cd')

    def on_enter_unknown_cd(self):
        """Send a message when entering the "unrecognized_faculty" state."""
        return "Thank you for sharing your feelings. I am here to listen. Could you explain a certain scenario that is making you feel uncomfortable?"

    def respond_from_cd_wave3(self, message, tags):
        """Decide what state to go to from the "unrecognized_faculty" state.

        Parameters:
            message (str): The incoming message.
            tags (Mapping[str, int]): A count of the tags that apply to the message.

        Returns:
            str: The message to send to the user.
        """
        for scenario in self.SCENARIOS:
            if scenario in tags:
                self.scenario = scenario
                return self.go_to_state('specific_scenario')
            else:
                return self.go_to_state('confused_scenario')

    def on_enter_confused_scenario(self):
        return "I can see that this is discomforting to you. What is another time you felt this way?"

    def respond_from_confused_scenario(self, message, tags):
        for scenario in self.SCENARIOS:
            if scenario in tags:
                self.scenario = scenario
                return self.go_to_state('specific_scenario')
            else:
                return self.go_to_state('find_campus_help')

    def on_enter_find_campus_help(self):
        return "Thank you for sharing your feelings. This is the first step towards molding more positive thought patterns for your day to day life. I think that other campus resources will monumentally help you work through these feelings. Would you like to someone about religious, cultural, personal, residential, or academic matters?"

    def respond_find_campus_help(self, message, tags):
        for area in self.AREAS:
            if area in tags:
                self.area = area
                return self.go_to_state('specific_area')
            else:
                return self.go_to_state('confused_campus_help')

    def on_enter_specific_area(self):
        return f"{self.get_campus_help(self.area)}. Did you find what you're looking for?"

    def respond_from_specific_area(self, message, tags):
        if 'yes' in tags:
            return self.finish('success')
        else:
            return self.go_to_state('breathing')


    def on_enter_confused_campus_help(self):
        return "I'm sorry. I don't understand. Would you like to reach out to an Oxy resource about religious, cultural, personal, residential, or academic matters?"

    def respond_from_confused_campus_help(self, message, tags):
        if 'yes' in tags:
            return self.finish('success')
        else:
            return self.go_to_state('breathing')

    def on_enter_check_feeling(self):
        return "It is helpful to take in moments in our life in a positive light. And to remember to practice self-compassion. Do you feel better?"

    def respond_from_check_feeling(self, message, tags):
        if 'yes' in tags:
            return self.finish('success')
        else:
            return self.go_to_state('breathing1')



    #breathing exercise
    def on_enter_breathing1(self):
        return "I'm sorry I couldn't be of any help. When feeling distressed, breathing is important. Can you slowly inhale and exhale with me? Inhale for 2 seconds. (Respond with 'y' when you have)"

    def respond_from_breathing1(self, message, tags):
        if 'y' in tags:
            return self.go_to_state('breathing2')
        else:
            return self.go_to_state('breathing_confused2')

    def on_enter_breathing_confused2(self):
        return "Respond with 'y' to proceed with breathing exercise."

    def respond_from_breathing_confused2(self, message, tags):
        if 'y' in tags:
            return self.go_to_state('breathing3')
        else:
            return self.go_to_state('breathing_confused2')

    def on_enter_breathing2(self):
        return "Good. Now exhale for two seconds. (Respond with 'y' when you have)"

    def respond_from_breathing2(self, message, tags):
        if 'y' in tags:
            return self.go_to_state('breathing3')
        else:
            return self.go_to_state('breathing_confused3')

    def on_enter_breathing_confused3(self):
        return "Respond with 'y' to proceed with breathing exercise."

    def respond_from_breathing_confused3(self, message, tags):
        if 'y' in tags:
            return self.finish('homework')
        else:
            return self.go_to_state('breathing_confused3')

    def on_enter_breathing3(self):
        return "Great! Now do the same two more times. Do you feel more calm? "

    def respond_from_breathing3(self, message, tags):
        if 'yes' in tags:
            return self.finish('homework')
        else:
            return self.finish('homework_fail')




    # "finish" functions

    def finish_confused(self):
        """Send a message and go to the default state."""
        return "Sorry, I'm confused. Could you explain more?"

    def finish_homework(self):
        return "Great! The process of understanding our feelings takes time. Come back again if you feel distressed again. Reflecting on our feelings can help us understand unhealthy thought patterns and change them for the better. For now, I suggest " + (random.choice(tuple(self.ASSIGNMENTS))) + "I appreciate your vulnerability."

    def finish_homework_fail(self):
        return "I'm sorry you feel that way. The process of understanding our feelings takes time. Come back again if you feel distressed again. Reflecting on our feelings can help us understand unhealthy thought patterns and change them for the better. For now, I suggest " + (random.choice(tuple(self.ASSIGNMENTS))) + "I appreciate your vulnerability."

    def finish_success(self):
        """Send a message and go to the default state."""
        return "Great, that is so good to hear! Reflecting on our feelings can help us understand unhealthy thought patterns and change them for the better. If you want to talk some more, O-team leaders, the Emmons center, and RAs are confidential sources of help. Your feelings are valid. For now, I suggest " + (random.choice(tuple(self.ASSIGNMENTS))) + "I appreciate your vulnerability."


    def finish_thanks(self):
        """Send a message and go to the default state."""
        return "You're welcome!"


if __name__ == '__main__':
    CBTBot().chat()
