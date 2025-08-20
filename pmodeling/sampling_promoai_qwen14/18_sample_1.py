import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
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
confirm_deadline = Transition(label='Confirm deadline')
send_orientation = Transition(label='Send orientation materials')
set_up_it_accounts = Transition(label='Set up IT accounts')
assist_with_visa = Transition(label='Assist with visa processing')
obtain_student_id = Transition(label='Obtain student ID card')
meet_academic_advisor = Transition(label='Meet with academic advisor')
select_courses = Transition(label='Select courses')
resolve_schedule_conflicts = Transition(label='Resolve schedule conflicts')
add_drop_courses = Transition(label='Add/drop courses')
begin_classes = Transition(label='Begin attending classes')
post_grades = Transition(label='Post grades')
review_grades = Transition(label='Review grades online')
file_appeal = Transition(label='File an appeal')
submit_appeal_form = Transition(label='Submit appeal form')
meet_appeals_committee = Transition(label='Meet with appeals committee')
await_decision = Transition(label='Await decision')
graduate = Transition(label='Graduate')
withdraw = Transition(label='Withdraw')

# Define silent transitions
skip = SilentTransition()

# Define loops
enrollment_loop = OperatorPOWL(operator=Operator.LOOP, children=[add_drop_courses, begin_classes])
semester_loop = OperatorPOWL(operator=Operator.LOOP, children=[enrollment_loop, post_grades, review_grades])

# Define choices
international_choice = OperatorPOWL(operator=Operator.XOR, children=[assist_with_visa, skip])
appeal_choice = OperatorPOWL(operator=Operator.XOR, children=[submit_appeal_form, skip])
withdraw_choice = OperatorPOWL(operator=Operator.XOR, children=[withdraw, skip])

# Define partial orders
pre_admission_order = StrictPartialOrder(nodes=[submit_application, review_application])
admission_order = StrictPartialOrder(nodes=[evaluate_application, process_fees])
enrollment_order = StrictPartialOrder(nodes=[confirm_enrollment, confirm_deadline, send_orientation, set_up_it_accounts])
study_plan_order = StrictPartialOrder(nodes=[meet_academic_advisor, select_courses, resolve_schedule_conflicts])
semester_order = StrictPartialOrder(nodes=[study_plan_order, semester_loop])
appeal_order = StrictPartialOrder(nodes=[file_appeal, appeal_choice])
withdraw_order = StrictPartialOrder(nodes=[withdraw_choice, graduate])

# Connect orders
pre_admission_order.order.add_edge(submit_application, review_application)
admission_order.order.add_edge(evaluate_application, process_fees)
enrollment_order.order.add_edge(confirm_enrollment, confirm_deadline)
enrollment_order.order.add_edge(confirm_deadline, send_orientation)
enrollment_order.order.add_edge(send_orientation, set_up_it_accounts)
study_plan_order.order.add_edge(meet_academic_advisor, select_courses)
study_plan_order.order.add_edge(select_courses, resolve_schedule_conflicts)
semester_order.order.add_edge(study_plan_order, semester_loop)
appeal_order.order.add_edge(file_appeal, appeal_choice)
withdraw_order.order.add_edge(withdraw_choice, graduate)

# Define main order
root = StrictPartialOrder(nodes=[pre_admission_order, admission_order, enrollment_order, international_choice, semester_order, appeal_order, withdraw_order])

# Connect main order
root.order.add_edge(pre_admission_order, admission_order)
root.order.add_edge(admission_order, enrollment_order)
root.order.add_edge(enrollment_order, international_choice)
root.order.add_edge(international_choice, semester_order)
root.order.add_edge(semester_order, appeal_order)
root.order.add_edge(appeal_order, withdraw_order)