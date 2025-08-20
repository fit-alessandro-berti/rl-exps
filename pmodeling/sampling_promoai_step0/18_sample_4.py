import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
add_drop_courses = Transition(label='Add/drop courses')
assist_with_visa = Transition(label='Assist with visa processing')
await_decision = Transition(label='Await decision')
begin_attending_classes = Transition(label='Begin attending classes')
cancel_application = Transition(label='Cancel application')
confirm_enrollment = Transition(label='Confirm enrollment')
evaluate_application = Transition(label='Evaluate application by admissions committee')
graduate = Transition(label='Graduate')
meet_with_advisor = Transition(label='Meet with academic advisor')
meet_with_appeals = Transition(label='Meet with appeals committee')
notify_missing_docs = Transition(label='Notify applicant of missing documents')
obtain_id_card = Transition(label='Obtain student ID card')
post_grades = Transition(label='Post grades')
process_fees = Transition(label='Process fees or waivers')
provide_missing_docs = Transition(label='Provide missing documents')
resolve_conflicts = Transition(label='Resolve schedule conflicts')
review_documents = Transition(label='Review application and documents')
review_grades = Transition(label='Review grades online')
select_courses = Transition(label='Select courses')
send_acceptance = Transition(label='Send acceptance letter')
send_orientation = Transition(label='Send orientation materials')
send_rejection = Transition(label='Send rejection letter')
setup_it = Transition(label='Set up IT accounts')
submit_appeal = Transition(label='Submit appeal form')
submit_application = Transition(label='Submit application online')
withdraw = Transition(label='Withdraw')

# Define transitions
xor = OperatorPOWL(operator=Operator.XOR, children=[graduate, withdraw])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[notify_missing_docs, provide_missing_docs])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[send_acceptance, send_rejection])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[add_drop_courses, select_courses, resolve_conflicts, review_documents, review_grades])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[process_fees, setup_it])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[meet_with_advisor, meet_with_appeals])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[submit_appeal, submit_application])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[confirm_enrollment, cancel_application])
xor9 = OperatorPOWL(operator=Operator.XOR, children=[await_decision, begin_attending_classes])
xor10 = OperatorPOWL(operator=Operator.XOR, children=[evaluate_application, assist_with_visa])
xor11 = OperatorPOWL(operator=Operator.XOR, children=[review_grades, review_documents])

loop = OperatorPOWL(operator=Operator.LOOP, children=[xor, xor2, xor3, xor4, xor5, xor6, xor7, xor8, xor9, xor10, xor11])

xor12 = OperatorPOWL(operator=Operator.XOR, children=[loop, xor])
xor13 = OperatorPOWL(operator=Operator.XOR, children=[xor12, xor10])

root = StrictPartialOrder(nodes=[xor13, xor10])
root.order.add_edge(xor12, xor13)
root.order.add_edge(xor13, xor10)

# Print the model
print(root)