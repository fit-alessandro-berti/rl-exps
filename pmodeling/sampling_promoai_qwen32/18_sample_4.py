import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
submit_application = Transition(label='Submit application online')
review_application = Transition(label='Review application and documents')
notify_missing_docs = Transition(label='Notify applicant of missing documents')
process_fees = Transition(label='Process fees or waivers')
evaluate_application = Transition(label='Evaluate application by admissions committee')
send_acceptance = Transition(label='Send acceptance letter')
send_rejection = Transition(label='Send rejection letter')
confirm_enrollment = Transition(label='Confirm enrollment')
cancel_application = Transition(label='Cancel application')
withdraw = Transition(label='Withdraw')
assist_visa = Transition(label='Assist with visa processing')
begin_attending = Transition(label='Begin attending classes')
post_grades = Transition(label='Post grades')
review_grades = Transition(label='Review grades online')
submit_appeal = Transition(label='Submit appeal form')
meet_appeals = Transition(label='Meet with appeals committee')
await_decision = Transition(label='Await decision')
add_drop = Transition(label='Add/drop courses')
meet_advisor = Transition(label='Meet with academic advisor')
select_courses = Transition(label='Select courses')
resolve_conflicts = Transition(label='Resolve schedule conflicts')
set_up_accounts = Transition(label='Set up IT accounts')
send_orientation = Transition(label='Send orientation materials')
obtain_id_card = Transition(label='Obtain student ID card')
graduate = Transition(label='Graduate')

# Define the silent transition for the loop
skip = SilentTransition()

# Define the choice between sending an acceptance or rejection letter
choice_accept_reject = OperatorPOWL(operator=Operator.XOR, children=[send_acceptance, send_rejection])

# Define the loop for the student's enrollment and semester activities
loop_enrollment = OperatorPOWL(operator=Operator.LOOP, children=[confirm_enrollment, cancel_application])

# Define the choice between confirming enrollment or canceling the application
choice_confirm_cancel = OperatorPOWL(operator=Operator.XOR, children=[loop_enrollment, withdraw])

# Define the choice between international or domestic student
choice_international_domestic = OperatorPOWL(operator=Operator.XOR, children=[assist_visa, skip])

# Define the choice between adding/dropping courses or not
choice_add_drop = OperatorPOWL(operator=Operator.XOR, children=[add_drop, skip])

# Define the choice between filing an appeal or not
choice_appeal = OperatorPOWL(operator=Operator.XOR, children=[submit_appeal, skip])

# Define the choice between meeting with the appeals committee or not
choice_meet_appeals = OperatorPOWL(operator=Operator.XOR, children=[meet_appeals, skip])

# Define the choice between awaiting a decision or not
choice_await_decision = OperatorPOWL(operator=Operator.XOR, children=[await_decision, skip])

# Define the choice between reviewing grades or not
choice_review_grades = OperatorPOWL(operator=Operator.XOR, children=[review_grades, skip])

# Define the choice between adding/dropping courses or not
choice_add_drop = OperatorPOWL(operator=Operator.XOR, children=[add_drop, skip])

# Define the choice between graduating or withdrawing
choice_graduate_withdraw = OperatorPOWL(operator=Operator.XOR, children=[graduate, withdraw])

# Define the choice between meeting with an academic advisor or not
choice_meet_advisor = OperatorPOWL(operator=Operator.XOR, children=[meet_advisor, skip])

# Define the choice between selecting courses or not
choice_select_courses = OperatorPOWL(operator=Operator.XOR, children=[select_courses, skip])

# Define the choice between resolving schedule conflicts or not
choice_resolve_conflicts = OperatorPOWL(operator=Operator.XOR, children=[resolve_conflicts, skip])

# Define the choice between setting up IT accounts or not
choice_set_up_accounts = OperatorPOWL(operator=Operator.XOR, children=[set_up_accounts, skip])

# Define the choice between sending orientation materials or not
choice_send_orientation = OperatorPOWL(operator=Operator.XOR, children=[send_orientation, skip])

# Define the choice between obtaining a student ID card or not
choice_obtain_id_card = OperatorPOWL(operator=Operator.XOR, children=[obtain_id_card, skip])

# Define the choice between beginning attending classes or not
choice_begin_attending = OperatorPOWL(operator=Operator.XOR, children=[begin_attending, skip])

# Define the choice between posting grades or not
choice_post_grades = OperatorPOWL(operator=Operator.XOR, children=[post_grades, skip])

# Define the choice between reviewing grades or not
choice_review_grades = OperatorPOWL(operator=Operator.XOR, children=[review_grades, skip])

# Define the choice between filing an appeal or not
choice_appeal = OperatorPOWL(operator=Operator.XOR, children=[submit_appeal, skip])

# Define the choice between meeting with the appeals committee or not
choice_meet_appeals = OperatorPOWL(operator=Operator.XOR, children=[meet_appeals, skip])

# Define the choice between awaiting a decision or not
choice_await_decision = OperatorPOWL(operator=Operator.XOR, children=[await_decision, skip])

# Define the choice between adding/dropping courses or not
choice_add_drop = OperatorPOWL(operator=Operator.XOR, children=[add_drop, skip])

# Define the choice between graduating or withdrawing
choice_graduate_withdraw = OperatorPOWL(operator=Operator.XOR, children=[graduate, withdraw])

# Define the choice between meeting with an academic advisor or not
choice_meet_advisor = OperatorPOWL(operator=Operator.XOR, children=[meet_advisor, skip])

# Define the choice between selecting courses or not
choice_select_courses = OperatorPOWL(operator=Operator.XOR, children=[select_courses, skip])

# Define the choice between resolving schedule conflicts or not
choice_resolve_conflicts = OperatorPOWL(operator=Operator.XOR, children=[resolve_conflicts, skip])

# Define the choice between setting up IT accounts or not
choice_set_up_accounts = OperatorPOWL(operator=Operator.XOR, children=[set_up_accounts, skip])

# Define the choice between sending orientation materials or not
choice_send_orientation = OperatorPOWL(operator=Operator.XOR, children=[send_orientation, skip])

# Define the choice between obtaining a student ID card or not
choice_obtain_id_card = OperatorPOWL(operator=Operator.XOR, children=[obtain_id_card, skip])

# Define the choice between beginning attending classes or not
choice_begin_attending = OperatorPOWL(operator=Operator.XOR, children=[begin_attending, skip])

# Define the choice between posting grades or not
choice_post_grades = OperatorPOWL(operator=Operator.XOR, children=[post_grades, skip])

# Define the choice between reviewing grades or not
choice_review_grades = OperatorPOWL(operator=Operator.XOR, children=[review_grades, skip])

# Define the choice between filing an appeal or not
choice_appeal = OperatorPOWL(operator=Operator.XOR, children=[submit_appeal, skip])

# Define the choice between meeting with the appeals committee or not
choice_meet_appeals = OperatorPOWL(operator=Operator.XOR, children=[meet_appeals, skip])

# Define the choice between awaiting a decision or not
choice_await_decision = OperatorPOWL(operator=Operator.XOR, children=[await_decision, skip])

# Define the choice between adding/dropping courses or not
choice_add_drop = OperatorPOWL(operator=Operator.XOR, children=[add_drop, skip])

# Define the choice between graduating or withdrawing
choice_graduate_withdraw = OperatorPOWL(operator=Operator.XOR, children=[graduate, withdraw])

# Define the choice between meeting with an academic advisor or not
choice_meet_advisor = OperatorPOWL(operator=Operator.XOR, children=[meet_advisor, skip])

# Define the choice between selecting courses or not
choice_select_courses = OperatorPOWL(operator=Operator.XOR, children=[select_courses, skip])

# Define the choice between resolving schedule conflicts or not
choice_resolve_conflicts = OperatorPOWL(operator=Operator.XOR, children=[resolve_conflicts, skip])

# Define the choice between setting up IT accounts or not
choice_set_up_accounts = OperatorPOWL(operator=Operator.XOR, children=[set_up_accounts, skip])

# Define the choice between sending orientation materials or not
choice_send_orientation = OperatorPOWL(operator=Operator.XOR, children=[send_orientation, skip])

# Define the choice between obtaining a student ID card or not
choice_obtain_id_card = OperatorPOWL(operator=Operator.XOR, children=[obtain_id_card, skip])

# Define the choice between beginning attending classes or not
choice_begin_attending = OperatorPOWL(operator=Operator.XOR, children=[begin_attending, skip])

# Define the choice between posting grades or not
choice_post_grades = OperatorPOWL(operator=Operator.XOR, children=[post_grades, skip])

# Define the choice between reviewing grades or not
choice_review_grades = OperatorPOWL(operator=Operator.XOR, children=[review_grades, skip])

# Define the choice between filing an appeal or not
choice_appeal = OperatorPOWL(operator=Operator.XOR, children=[submit_appeal, skip])

# Define the choice between meeting with the appeals committee or not
choice_meet_appeals = OperatorPOWL(operator=Operator.XOR, children=[meet_appeals, skip])

# Define the choice between awaiting a decision or not
choice_await_decision = OperatorPOWL(operator=Operator.XOR, children=[await_decision, skip])

# Define the choice between adding/dropping courses or not
choice_add_drop = OperatorPOWL(operator=Operator.XOR, children=[add_drop, skip])

# Define the choice between graduating or withdrawing
choice_graduate_withdraw = OperatorPOWL(operator=Operator.XOR, children=[graduate, withdraw])

# Define the choice between meeting with an academic advisor or not
choice_meet_advisor = OperatorPOWL(operator=Operator.XOR, children=[meet_advisor, skip])

# Define the choice between selecting courses or not
choice_select_courses = OperatorPOWL(operator=Operator.XOR, children=[select_courses, skip])

# Define the choice between resolving schedule conflicts or not
choice_resolve_conflicts = OperatorPOWL(operator=Operator.XOR, children=[resolve_conflicts, skip])

# Define the choice between setting up IT accounts or not
choice_set_up_accounts = OperatorPOWL(operator=Operator.XOR, children=[set_up_accounts, skip])

# Define the choice between sending orientation materials or not
choice_send_orientation = OperatorPOWL(operator=Operator.XOR, children=[send_orientation, skip])

# Define the choice between obtaining a student ID card or not
choice_obtain_id_card = OperatorPOWL(operator=Operator.XOR, children=[obtain_id_card, skip])

# Define the choice between beginning attending classes or not
choice_begin_attending = OperatorPOWL(operator=Operator.XOR, children=[begin_attending, skip])

# Define the choice between posting grades or not
choice_post_grades = OperatorPOWL(operator=Operator.XOR, children=[post_grades, skip])

# Define the choice between reviewing grades or not
choice_review_grades = OperatorPOWL(operator=Operator.XOR, children=[review_grades, skip])

# Define the choice between filing an appeal or not
choice_appeal = OperatorPOWL(operator=Operator.XOR, children=[submit_appeal, skip])

# Define the choice between meeting with the appeals committee or not
choice_meet_appeals = OperatorPOWL(operator=Operator.XOR, children=[meet_appeals, skip])

# Define the choice between awaiting a decision or not
choice_await_decision = OperatorPOWL(operator=Operator.XOR, children=[await_decision, skip])

# Define the choice between adding/dropping courses or not
choice_add_drop = OperatorPOWL(operator=Operator.XOR, children=[add_drop, skip])

# Define the choice between graduating or withdrawing
choice_graduate_withdraw = OperatorPOWL(operator=Operator.XOR, children=[graduate, withdraw])

# Define the choice between meeting with an academic advisor or not
choice_meet_advisor = OperatorPOWL(operator=Operator.XOR, children=[meet_advisor, skip])

# Define the choice between selecting courses or not
choice_select_courses = OperatorPOWL(operator=Operator.XOR, children=[select_courses, skip])

# Define the choice between resolving schedule conflicts or not
choice_resolve_conflicts = OperatorPOWL(operator=Operator.XOR, children=[resolve_conflicts, skip])

# Define the choice between setting up IT accounts or not
choice_set_up_accounts = OperatorPOWL(operator=Operator.XOR, children=[set_up_accounts, skip])

# Define the choice between sending orientation materials or not
choice_send_orientation = OperatorPOWL(operator=Operator.XOR, children=[send_orientation, skip])

# Define the choice between obtaining a student ID card or not
choice_obtain_id_card = OperatorPOWL(operator=Operator.XOR, children=[obtain_id_card, skip])

# Define the choice between beginning attending classes or not
choice_begin_attending = OperatorPOWL(operator=Operator.XOR, children=[begin_attending, skip])

# Define the choice between posting grades or not
choice_post_grades = OperatorPOWL(operator=Operator.XOR, children=[post_grades, skip])

# Define the choice between reviewing grades or not
choice_review_grades = OperatorPOWL(operator=Operator.XOR, children=[review_grades, skip])

# Define the choice between filing an appeal or not
choice_appeal = OperatorPOWL(operator=Operator.XOR, children=[submit_appeal, skip])

# Define the choice between meeting with the appeals committee or not
choice_meet_appeals = OperatorPOWL(operator=Operator.XOR, children=[meet_appeals, skip])

# Define the choice between awaiting a decision or not
choice_await_decision = OperatorPOWL(operator=Operator.XOR, children=[await_decision, skip])

# Define the choice between adding/dropping courses or not
choice_add_drop = OperatorPOWL(operator=Operator.XOR, children=[add_drop, skip])

# Define the choice between graduating or withdrawing
choice_graduate_withdraw = OperatorPOWL(operator=Operator.XOR, children=[graduate, withdraw])

# Define the choice between meeting with an academic advisor or not
choice_meet_advisor = OperatorPOWL(operator=Operator.XOR, children=[meet_advisor, skip])

# Define the choice between selecting courses or not
choice_select_courses = OperatorPOWL(operator=Operator.XOR, children=[select_courses, skip])

# Define the choice between resolving schedule conflicts or not
choice_resolve_conflicts = OperatorPOWL(operator=Operator.XOR, children=[resolve_conflicts, skip])

# Define the choice between setting up IT accounts or not
choice_set_up_accounts = OperatorPOWL(operator=Operator.XOR, children=[set_up_accounts, skip])

# Define the choice between sending orientation materials or not
choice_send_orientation = OperatorPOWL(operator=Operator.XOR, children=[send_orientation, skip])

# Define the choice between obtaining a student ID card or not
choice_obtain_id_card = OperatorPOWL(operator=Operator.XOR, children=[obtain_id_card, skip])

# Define the choice between beginning attending classes or not
choice_begin_attending = OperatorPOWL(operator=Operator.XOR, children=[begin_attending, skip])

# Define the choice between posting grades or not
choice_post_grades = OperatorPOWL(operator=Operator.XOR, children=[post_grades, skip])

# Define the choice between reviewing grades or not
choice_review_grades = OperatorPOWL(operator=Operator.XOR, children=[review_grades, skip])

# Define the choice between filing an appeal or not
choice_appeal = OperatorPOWL(operator=Operator.XOR, children=[submit_appeal, skip])

# Define the choice between meeting with the appeals committee or not
choice_meet_appeals = OperatorPOWL(operator=Operator.XOR, children=[meet_appeals, skip])

# Define the choice between awaiting a decision or not
choice_await_decision = OperatorPOWL(operator=Operator.XOR, children=[await_decision, skip])

# Define the choice between adding/dropping courses or not
choice_add_drop = OperatorPOWL(operator=Operator.XOR, children=[add_drop, skip])

# Define the choice between graduating or withdrawing
choice_graduate_withdraw = OperatorPOWL(operator=Operator.XOR, children=[graduate, withdraw])

# Define the choice between meeting with an academic advisor or not
choice_meet_advisor = OperatorPOWL(operator=Operator.XOR, children=[meet_advisor, skip])

# Define the choice between selecting courses or not
choice_select_courses = OperatorPOWL(operator=Operator.XOR, children=[select_courses, skip])

# Define the choice between resolving schedule conflicts or not
choice_resolve_conflicts = OperatorPOWL(operator=Operator.XOR, children=[resolve_conflicts, skip])

# Define the choice between setting up IT accounts or not
choice_set_up_accounts = OperatorPOWL(operator=Operator.XOR, children=[set_up_accounts, skip])

# Define the choice between sending orientation materials or not
choice_send_orientation = OperatorPOWL(operator=Operator.XOR, children=[send_orientation, skip])

# Define the choice between obtaining a student ID card or not
choice_obtain_id_card = OperatorPOWL(operator=Operator.XOR, children=[obtain_id_card, skip])

# Define the choice between beginning attending classes or not
choice_begin_attending = OperatorPOWL(operator=Operator.XOR, children=[begin_attending, skip])

# Define the choice between posting grades or not
choice_post_grades = OperatorPOWL(operator=Operator.XOR, children=[post_grades, skip])

# Define the choice between reviewing grades or not
choice_review_grades = OperatorPOWL(operator=Operator.XOR, children=[review_grades, skip])

# Define the choice between filing an appeal or not
choice_appeal = OperatorPOWL(operator=Operator.XOR, children=[submit_appeal, skip])

# Define the choice between meeting with the appeals committee or not
choice_meet_appeals = OperatorPOWL(operator=Operator.XOR, children=[meet_appeals, skip])

# Define the choice between awaiting a decision or not
choice_await_decision = OperatorPOWL(operator=Operator.XOR, children=[await_decision, skip])

# Define the choice between adding/dropping courses or not
choice_add_drop = OperatorPOWL(operator=Operator.XOR, children=[add_drop, skip])

# Define the choice between graduating or withdrawing
choice_graduate_withdraw = OperatorPOWL(operator=Operator.XOR, children=[graduate, withdraw])

# Define the choice between meeting with an academic advisor or not
choice_meet_advisor = OperatorPOWL(operator=Operator.XOR, children=[meet_advisor, skip])

# Define the choice between selecting courses or not
choice_select_courses = OperatorPOWL(operator=Operator.XOR, children=[select_courses, skip])

# Define the choice between resolving schedule conflicts or not
choice_resolve_conflicts = OperatorPOWL(operator=Operator.XOR, children=[resolve_conflicts, skip])

# Define the choice between setting up IT accounts or not
choice_set_up_accounts = OperatorPOWL(operator=Operator.XOR, children=[set_up_accounts, skip])

# Define the choice between sending orientation materials or not
choice_send_orientation