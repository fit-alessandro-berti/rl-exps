import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
artifact_intake = Transition(label='Artifact Intake')
initial_survey = Transition(label='Initial Survey')
material_test = Transition(label='Material Test')
historical_check = Transition(label='Historical Check')
registry_search = Transition(label='Registry Search')
owner_interview = Transition(label='Owner Interview')
condition_report = Transition(label='Condition Report')
forger_scan = Transition(label='Forgery Scan')
digital_tagging = Transition(label='Digital Tagging')
ledger_entry = Transition(label='Ledger Entry')
expert_review = Transition(label='Expert Review')
legal_verify = Transition(label='Legal Verify')
provenance_draft = Transition(label='Provenance Draft')
client_approval = Transition(label='Client Approval')
final_certificate = Transition(label='Final Certificate')
archive_storage = Transition(label='Archive Storage')

# Define silent transitions
skip = SilentTransition()

# Define the POWL model
loop_1 = OperatorPOWL(operator=Operator.LOOP, children=[artifact_intake, initial_survey])
loop_2 = OperatorPOWL(operator=Operator.LOOP, children=[material_test, historical_check])
loop_3 = OperatorPOWL(operator=Operator.LOOP, children=[registry_search, owner_interview])
loop_4 = OperatorPOWL(operator=Operator.LOOP, children=[condition_report, forger_scan])
loop_5 = OperatorPOWL(operator=Operator.LOOP, children=[digital_tagging, ledger_entry])
loop_6 = OperatorPOWL(operator=Operator.LOOP, children=[expert_review, legal_verify])
loop_7 = OperatorPOWL(operator=Operator.LOOP, children=[provenance_draft, client_approval])
loop_8 = OperatorPOWL(operator=Operator.LOOP, children=[final_certificate, archive_storage])

# Construct the root POWL model
root = StrictPartialOrder(nodes=[
    loop_1,
    loop_2,
    loop_3,
    loop_4,
    loop_5,
    loop_6,
    loop_7,
    loop_8
])

# Add dependencies between loops
root.order.add_edge(loop_1, loop_2)
root.order.add_edge(loop_2, loop_3)
root.order.add_edge(loop_3, loop_4)
root.order.add_edge(loop_4, loop_5)
root.order.add_edge(loop_5, loop_6)
root.order.add_edge(loop_6, loop_7)
root.order.add_edge(loop_7, loop_8)

# Print the POWL model
print(root)