from uuid import uuid4
from django.db import models
from core.models import CustomUser

from lecturer.models import Lecturer




class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return f"{self.user.name}| {self.user.school_id}"
        

class StudentsStaffEvaluation(models.Model):
    OPTIONS = [
        ("Poor", "Poor"),
        ("Satisfactory", "Satisfactory"),
        ("Below Average", "Below Average"),
        ("Good", "Good"),
        ("Excellent", "Excellent"),
    ]

    id = models.UUIDField(
        unique=True,
        default=uuid4,
        editable=False,
        primary_key=True
    )

    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)

    rate_learning_experience = models.CharField(
        max_length=20,
        choices=OPTIONS,
        verbose_name="How would you rate the learning experience and the lecture delivery for this course?"
    )

    stimulation_of_interest_in_this_subject = models.CharField(
        max_length=200,
        choices=[
            ("Lecturer develops a reading atmosphere for students through homework assignments",
             "Lecturer develops a reading atmosphere for students through homework assignments"),
            ("Shows the relevance of the topic to students' future careers",
             "Shows the relevance of the topic to students' future careers"),
            ("Lets students participate in the learning process to understand students interests",
             "Lets students participate in the learning process to understand students interests"),
            ("Give examples and relates topic to daily real-life occurrences",
             "Give examples and relates topic to daily real-life occurrences"),
            ("Lecture is depressing and Lecturer does not stimulate my interest in the subject",
             "Lecture is depressing and Lecturer does not stimulate my interest in the subject"),
        ],
        verbose_name="How does the Lecturer stimulate your interest in the subject?"
    )

    method_of_explaining_difficult_topics = models.CharField(
        max_length=200,
        choices=[
            ("Lecturer gives examples, uses visuals and defines difficult words.",
             "Lecturer gives examples, uses visuals and defines difficult words."),
            ("Creates time for students to reflect individually or as a group on what they learned",
             "Creates time for students to reflect individually or as a group on what they learned"),
            ("Encourage students to listen, share their views and ask questions.",
             "Encourage students to listen, share their views and ask questions."),
            ("Lecturer listens attentively without interrupting or belittling the student",
             "Lecturer listens attentively without interrupting or belittling the student"),
            ("No strategy is adopted by lecturer to explain difficult topics.",
             "No strategy is adopted by lecturer to explain difficult topics."),
        ],
        verbose_name="How does the Lecturer teach and explain difficult topics?"
    )

    rate_ability_to_meet_course_objectives = models.CharField(
        max_length=20,
        choices=OPTIONS,
        verbose_name="How would you rate the ability of the lecturer to meet the course objectives and outline?"
    )

    rate_ability_for_interaction = models.CharField(
        max_length=20,
        choices=OPTIONS,
        verbose_name="How would you rate the lecturer's availability for discussion/interaction with the students?"
    )

    relevance_of_tests_assignments_and_exams = models.CharField(
        max_length=20,
        choices=OPTIONS,
        verbose_name="How would you rate the relevance of tests, assignments and exams in relation to the course learning outcomes?"
    )

    rate_lecturers_feedback_on_assignments_and_tests_given = models.CharField(
        max_length=200,
        choices=[
            ("Lecturer gives feedback that is positive, reference specific knowledge and educative in nature",
             "Lecturer gives feedback that is positive, reference specific knowledge and educative in nature"),
            ("Lecturer gives feedback that is adequate enough to keep students on target for improved performance.",
             "Lecturer gives feedback that is adequate enough to keep students on target for improved performance."),
            ("Feedback is given in a timely manner to allow student connect the feedback to learning experience",
             "Feedback is given in a timely manner to allow student connect the feedback to learning experience"),
            ("Feedbacks of the lecturer are negative and does not provide guidance for improved learning",
             "Feedbacks of the lecturer are negative and does not provide guidance for improved learning"),
            ("Lecturer does not give feedback on assignments nor discuss performance of CA with students",
             "Lecturer does not give feedback on assignments nor discuss performance of CA with students"),
        ],
        verbose_name="How would you rate the lecturer's feedback on assignments and tests given?"
    )

    rate_the_lecturer_preparedness_before_class = models.CharField(
        max_length=20,
        choices=OPTIONS,
        verbose_name="How would you rate the lecturer's preparedness for the course before lecturing in the class?"
    )

    rate_ability_to_give_clear_answers_to_questions = models.CharField(
        max_length=20,
        choices=OPTIONS,
        verbose_name="How would you rate the lecturer's ability to give clear answers to questions asked by students?"
    )

    describe_teaching_method = models.CharField(
        max_length=95,
        choices=[
            ("Lecturer asks students for contributions, gives examples and reading references",
             "Lecturer asks students for contributions, gives examples and reading references"),
            ("Lecturer does not encourage questions and spends more time teaching",
             "Lecturer does not encourage questions and spends more time teaching"),
            ("Lecturer asks students lots of questions and spends less time teaching",
             "Lecturer asks students lots of questions and spends less time teaching"),
            ("Lecturer jokes a lot in class and tells students stories about his personal affairs",
             "Lecturer jokes a lot in class and tells students stories about his personal affairs"),
            ("Lecturer mostly dictates long notes in the class and spends less time interacting with students",
             "Lecturer mostly dictates long notes in the class and spends less time interacting with students"),
        ],
        verbose_name="Which of these best describes how the lecturer teaches in class?"
    )

    rate_punctuality = models.CharField(
        max_length=70,
        choices=[
            ("Lecturer always come on time and stays till end of class",
             "Lecturer always come on time and stays till end of class"),
            ("Lecturer always come on time and leaves before end of class",
             "Lecturer always come on time and leaves before end of class"),
            ("Lecturer mostly come late to class but stays till the end of the class",
             "Lecturer mostly come late to class but stays till the end of the class"),
            ("Lecturer mostly come late and will leave before the end of the class",
             "Lecturer mostly come late and will leave before the end of the class"),
            ("Lecturer barely come to class", "Lecturer barely come to class"),
        ],
        verbose_name="How would you rate the punctuality to your classes?"
    )

    rate_requirements_text_books_and_learning_materials = models.CharField(
        max_length=94,
        choices=[
            ("The course workload and requirements were appropriate for the course level",
             "The course workload and requirements were appropriate for the course level"),
            ("The lectures, readings, and assignments complemented each other.",
             "The lectures, readings, and assignments complemented each other."),
            ("Exams and assignments were reflective of the course content",
             "Exams and assignments were reflective of the course content"),
            ("The course did not follow the syllabus and lecture keeps repeating lectures already delivered.",
             "The course did not follow the syllabus and lecture keeps repeating lectures already delivered."),
            ("The requirements, text books and learning materials used in the course were inadequate",
             "The requirements, text books and learning materials used in the course were inadequate"),
        ],
        verbose_name="How would you rate the requirements, text books and learning materials used in the course?"
    )

    was_the_practical_aspect_of_the_course_met = models.CharField(
        max_length=33,
        choices=[
            ("Yes", "Yes"),
            ("No", "No"),
            ("Course does not require practical", "Course does not require practical"),
        ],
        verbose_name="Was the practical aspect of the course met"
    )

    rate_this_lecturer = models.CharField(
        max_length=33,
        choices=[
            ("Yes", "Yes"),
            ("No", "No"),
            ("Course does not require practical",
             "Course does not require practical"),
        ],
        verbose_name="Overall, how would you rate the lecturer who taught this course?"
    )

    should_this_lecturer_be_replaced = models.CharField(
        max_length=3,
        choices=[
            ("Yes", "Yes"),
            ("No", "No")
        ],
        verbose_name="Would you prefer that the lecturer who taught this course to be replaced by another lecturer"
    )

    favorite_aspect_of_teaching = models.TextField(
        max_length=20,
        verbose_name="Which aspect of the teaching did you dislike the most?"
    )

    least_favorite_aspect_of_teaching = models.TextField(
        verbose_name="Which aspect of the teaching did you dislike the most?"
    )

    suggestions_for_improvement = models.TextField(
        max_length=200, verbose_name="What can be done to improve the teaching of the course?")

    created_at = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return super().__str__()
