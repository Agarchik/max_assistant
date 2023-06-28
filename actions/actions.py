import json
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionShowCourses(Action):

    def name(self) -> Text:
        return "action_show_courses"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        with open('./scenario/screp_info.json', 'r', encoding='utf-8') as f:
            data = json.load(f)

        buttons = []
        for course in data["courses"]:
            course_name = course['name']
            buttons.append(
                {"title": course_name, 
                 "payload": f'/select_course{{"course_name":"{course_name}"}}'}
            )

        dispatcher.utter_message(text="Выберите направление:", buttons=buttons, button_type = "reply")

        return []

class ActionShowCourseInfo(Action):

    def name(self) -> Text:
        return "action_show_course_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        with open('./scenario/screp_info.json', 'r', encoding='utf-8') as f:
            data = json.load(f)

        selected_course = tracker.get_slot('course_name')

        buttons = []
        for course in data['courses']:
            if course['name'] == selected_course:
                course_info = f"Название курса: {course['name']}\n" \
                              f"Бюджетные места: {course['budget_place']}\n" \
                              f"Платные места: {course['paid_place']}\n" \
                              f"Цена: {course['price']}\n" \
                              f"Проходной балл прошлого года: {course['cut_off']}\n" 
                dispatcher.utter_message(text=course_info)
                return []

        dispatcher.utter_message(text=f"Извините, информация о курсе {selected_course} не найдена.")

        return []

class ActionShowExams(Action):

    def name(self) -> Text:
        return "action_show_exams"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        with open('./scenario/exam.json', 'r', encoding='utf-8') as f:
            data = json.load(f)

        buttons = []
        for exams in data["exams"]:
            exam_name = exams['name']
            buttons.append(
                {"title": exam_name, 
                 "payload": f'/select_exam{{"exam_name":"{exam_name}"}}'}
            )

        dispatcher.utter_message(text="Выберите интересующий Вас экзамен:", buttons=buttons, button_type = "reply")

        return []

class ActionShowCourseInfo(Action):

    def name(self) -> Text:
        return "action_show_exams_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        with open('./scenario/exam.json', 'r', encoding='utf-8') as f:
            data = json.load(f)

        selected_exam = tracker.get_slot('exam_name')

        buttons = []
        for exam in data['exams']:
            if exam['name'] == selected_exam:
                exam_info = f"По предмету {exam['name']} минимальный балл  - 40\n" \
                            f"Демо-вариант: {exam['link']}\n" 
                dispatcher.utter_message(text=exam_info)
                return []

        dispatcher.utter_message(text=f"Извините, информация о экзамене {selected_exam} не найдена.")

        return []