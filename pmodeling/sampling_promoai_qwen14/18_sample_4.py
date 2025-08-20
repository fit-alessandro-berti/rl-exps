import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
submit_application = Transition(label='Submit application online')
review_application = Transition(label='Review application and documents')
notify_missing_docs = Transition(label='Notify applicant of missing documents')
provide_missing_docs = Transition(label='Provide missing documents')
evaluate_application = Transition(label='Evaluate application by admissions committee')
process_fees = Transition(label='Process fees or waivers')
accept_application = Transition(label='Send acceptance letter')
reject_application = Transition(label='Send rejection letter')
cancel_application = Transition(label='Cancel application')
confirm_enrollment = Transition(label='Confirm enrollment')
send_orientation = Transition(label='Send orientation materials')
setup_it_accounts = Transition(label='Set up IT accounts')
assist_with_visa = Transition(label='Assist with visa processing')
obtain_id_card = Transition(label='Obtain student ID card')
meet_with_advisor = Transition(label='Meet with academic advisor')
select_courses = Transition(label='Select courses')
resolve_schedule_conflicts = Transition(label='Resolve schedule conflicts')
begin_classes = Transition(label='Begin attending classes')
add_drop_courses = Transition(label='Add/drop courses')
post_grades = Transition(label='Post grades')
review_grades = Transition(label='Review grades online')
submit_appeal = Transition(label='Submit appeal form')
meet_with_appeals = Transition(label='Meet with appeals committee')
await_decision = Transition(label='Await decision')
graduate = Transition(label='Graduate')
withdraw = Transition(label='Withdraw')

# Define exclusive choice for missing documents
missing_docs_choice = OperatorPOWL(operator=Operator.XOR, children=[provide_missing_docs, cancel_application])

# Define loop for add/drop courses
add_drop_loop = OperatorPOWL(operator=Operator.LOOP, children=[add_drop_courses])

# Define exclusive choice for application outcome
application_outcome = OperatorPOWL(operator=Operator.XOR, children=[accept_application, reject_application])

# Define concurrent steps for accepted application
accepted_application = StrictPartialOrder(nodes=[send_orientation, setup_it_accounts, assist_with_visa])
accepted_application.order.add_edge(send_orientation, setup_it_accounts)
accepted_application.order.add_edge(setup_it_accounts, assist_with_visa)

# Define exclusive choice for international student
international_student = OperatorPOWL(operator=Operator.XOR, children=[assist_with_visa, SilentTransition()])

# Define exclusive choice for student ID card
obtain_id_card_choice = OperatorPOWL(operator=Operator.XOR, children=[obtain_id_card, SilentTransition()])

# Define concurrent steps for creating study plan
create_study_plan = StrictPartialOrder(nodes=[meet_with_advisor, select_courses, resolve_schedule_conflicts])
create_study_plan.order.add_edge(meet_with_advisor, select_courses)
create_study_plan.order.add_edge(select_courses, resolve_schedule_conflicts)

# Define concurrent steps for semester
semester = StrictPartialOrder(nodes=[begin_classes, add_drop_loop])
semester.order.add_edge(begin_classes, add_drop_loop)

# Define exclusive choice for grievance resolution
grievance_resolution = OperatorPOWL(operator=Operator.XOR, children=[submit_appeal, SilentTransition()])

# Define exclusive choice for appeal outcome
appeal_outcome = OperatorPOWL(operator=Operator.XOR, children=[await_decision, SilentTransition()])

# Define loop for semester
semester_loop = OperatorPOWL(operator=Operator.LOOP, children=[semester, grievance_resolution, appeal_outcome])

# Define concurrent steps for accepted application
accepted_application = StrictPartialOrder(nodes=[obtain_id_card_choice, create_study_plan, semester_loop])
accepted_application.order.add_edge(obtain_id_card_choice, create_study_plan)
accepted_application.order.add_edge(create_study_plan, semester_loop)

# Define exclusive choice for application outcome
application_outcome = OperatorPOWL(operator=Operator.XOR, children=[accepted_application, SilentTransition()])

# Define root POWL model
root = StrictPartialOrder(nodes=[submit_application, review_application, missing_docs_choice, evaluate_application, process_fees, application_outcome, confirm_enrollment, cancel_application])
root.order.add_edge(submit_application, review_application)
root.order.add_edge(review_application, missing_docs_choice)
root.order.add_edge(missing_docs_choice, evaluate_application)
root.order.add_edge(evaluate_application, process_fees)
root.order.add_edge(process_fees, application_outcome)
root.order.add_edge(application_outcome, confirm_enrollment)
root.order.add_edge(confirm_enrollment, cancel_application)