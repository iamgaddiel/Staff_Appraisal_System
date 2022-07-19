from uuid import uuid4
from django.db import models

from core.models import CustomUser


class Lecturer(models.Model):
    ACADEMIC_RANK = (
        ("Assistant lecturer", "Assistant lecturer"),
        ("Lecturer II", "Lecturer II"),
        ("Lecturer I", "Lecturer I"),
        ("Senior lecturer", "Senior lecturer"),
        ("Professor", "Professor"),
    )

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    academic_rank = models.CharField(max_length=20, choices=ACADEMIC_RANK)

    def __str__(self) -> str:
        return f"{self.user.username}"


class PeerPerformanceEvaluation(models.Model):
    OPTIONS = [
        ("Poor", "Poor"),
        ("Satisfactory", "Satisfactory"),
        ("Below Average", "Below Average"),
        ("Good", "Good"),
        ("Excellent", "Excellent"),
    ]
    
    id = models.UUIDField(unique=True, default=uuid4, editable=False, primary_key=True)
    lecturer = models.ForeignKey(Lecturer,on_delete=models.CASCADE)
    employee_name = models.CharField(max_length=20)
    evaluators_name = models.CharField(max_length=20)
    created_at = models.DateField(auto_now=True)
    good_attitude = models.CharField(max_length=20, choices=OPTIONS, help_text="comes to work with a good attitude")
    communication = models.CharField(max_length=20, choices=OPTIONS, help_text="Communicates well with others")
    helpful = models.CharField(max_length=20, choices=OPTIONS, help_text="Willingness to help others")
    punctuality = models.CharField(max_length=20, choices=OPTIONS)
    work_by_book = models.CharField(max_length=20, choices=OPTIONS, help_text="Performs job duties as described in the Employee Handbook")
    teachability = models.CharField(max_length=20, choices=OPTIONS, help_text="Willingness to learn")
    efficiency = models.CharField(max_length=20, choices=OPTIONS, help_text="Efficiency/work flow")
    knowledgeable = models.CharField(max_length=20, choices=OPTIONS, help_text="Knowledge/skill set in relation to position")
    role_fulfillment = models.CharField(max_length=300)
    cooperates_with_others = models.CharField(max_length=300)
    performance_comments = models.TextField()
    objectives = models.TextField()
    suggestions = models.TextField(help_text="Suggestions to successfully achieve objectives")


    def __str__(self) -> str:
        return f"{self.evaluators_name} => {self.lecturer.user.name}"


class SelfEvaluation(models.Model):
    OPTIONS = [
        ("always", "always"),
        ("Often", "Often"),
        ("Rarely", "Rarely"),
        ("Never", "Never"),
    ]

    lecturer = models.OneToOneField(Lecturer, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    dob = models.DateField(null=True)

    I_encourage_my_students_to_reach_new_information = models.CharField(max_length=20, choices=OPTIONS)
    I_teach_my_students_how_to_reach_new_information_and_transfer_that_information_to_others = models.CharField(max_length=20, choices=OPTIONS)
    I_review_past_classes = models.CharField(max_length=20, choices=OPTIONS)
    I_prepare_course_plans_for_my_classes = models.CharField(max_length=20, choices=OPTIONS)
    I_use_daily_life_examples_for_my_students_to_help_them_understand_more_easily = models.CharField(max_length=20, choices=OPTIONS)
    I_use_teaching_aids = models.CharField(max_length=20, choices=OPTIONS)
    I_encourage_both_individual_pair_and_group_studies_in_my_classes = models.CharField(max_length=20, choices=OPTIONS,)
    I_use_different_activities_in_my_classes_to_increase_attention = models.CharField(max_length=20, choices=OPTIONS)
    I_know_all_of_my_students_names = models.CharField(max_length=20, choices=OPTIONS)
    I_try_to_find_out_abilities_of_every_student = models.CharField(max_length=20, choices=OPTIONS)
    I_communicate_with_my_students_about_their_problems_and_try_to_find_solutions_to_them = models.CharField(max_length=20, choices=OPTIONS)
    I_regularly_make_updates_about_my_students_progress_to_them_and_their_parents = models.CharField(max_length=20, choices=OPTIONS)
    I_try_to_improve_my_teaching_by_learning_new_things_about_my_field = models.CharField(max_length=20, choices=OPTIONS)
    I_work_with_colleagues_to_overcome_different_issues_and_problems_and_to_learn_new_staff = models.CharField(max_length=20, choices=OPTIONS)
    I_make_observations_on_how_colleagues_teach_to_improve_myself = models.CharField(max_length=20, choices=OPTIONS)
    I_try_to_improve_my_language_to_teach_more_effectively = models.CharField(max_length=20, choices=OPTIONS)
    I_attend_trainings_about_my_teaching_field = models.CharField(max_length=20, choices=OPTIONS)
    My_course_plans_are_regular_and_up_to_date = models.CharField(max_length=20, choices=OPTIONS)
    I_keep_records_of_my_students_learning_progress = models.CharField(max_length=20, choices=OPTIONS)

    Please_write_down_what_you_are_good_at = models.TextField()
    What_do_you_need_to_do_to_improve_yourself = models.TextField()
    What_strategies_will_you_use_to_improve_yourself = models.TextField()
    created_at = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.name} | {self.lecturer.user.school_id}"