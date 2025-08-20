import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
submit_application = Transition(label='Submit application online')
review_documents = Transition(label='Review application and documents')
notify_missing = Transition(label='Notify applicant of missing documents')
provide_missing = Transition(label='Provide missing documents')
evaluate_app = Transition(label='Evaluate application by admissions committee')
process_fees = Transition(label='Process fees or waivers')
accept_app = Transition(label='Send acceptance letter')
reject_app = Transition(label='Send rejection letter')
cancel_app = Transition(label='Cancel application')
confirm_enrollment = Transition(label='Confirm enrollment')
set_up_it = Transition(label='Set up IT accounts')
send_orientation = Transition(label='Send orientation materials')
assist_visa = Transition(label='Assist with visa processing')
obtain_id_card = Transition(label='Obtain student ID card')
meet_advisor = Transition(label='Meet with academic advisor')
select_courses = Transition(label='Select courses')
resolve_conflicts = Transition(label='Resolve schedule conflicts')
begin_classes = Transition(label='Begin attending classes')
add_drop = Transition(label='Add/drop courses')
post_grades = Transition(label='Post grades')
review_grades = Transition(label='Review grades online')
submit_appeal = Transition(label='Submit appeal form')
meet_appeals = Transition(label='Meet with appeals committee')
await_decision = Transition(label='Await decision')
graduate = Transition(label='Graduate')
withdraw = Transition(label='Withdraw')

# Define loops and choices
enrollment_loop = OperatorPOWL(operator=Operator.LOOP, children=[begin_classes, add_drop])
semester_loop = OperatorPOWL(operator=Operator.LOOP, children=[enrollment_loop, post_grades, review_grades, submit_appeal, meet_appeals, await_decision])
international_choice = OperatorPOWL(operator=Operator.XOR, children=[assist_visa, SilentTransition()])
grievance_choice = OperatorPOWL(operator=Operator.XOR, children=[submit_appeal, SilentTransition()])
study_plan = OperatorPOWL(operator=Operator.SEQUENCE, children=[meet_advisor, select_courses, resolve_conflicts])
enrollment_process = OperatorPOWL(operator=Operator.SEQUENCE, children=[confirm_enrollment, study_plan, international_choice, obtain_id_card])
acceptance_process = OperatorPOWL(operator=Operator.XOR, children=[enrollment_process, SilentTransition()])
admissions_process = OperatorPOWL(operator=Operator.SEQUENCE, children=[review_documents, notify_missing, provide_missing, evaluate_app, process_fees, acceptance_process])
final_process = OperatorPOWL(operator=Operator.XOR, children=[graduate, withdraw])

# Define the root POWL model
root = StrictPartialOrder(nodes=[submit_application, admissions_process, final_process])
root.order.add_edge(submit_application, admissions_process)
root.order.add_edge(admissions_process, final_process)