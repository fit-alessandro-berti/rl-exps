import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
intake_check = Transition(label='Intake Check')
condition_log = Transition(label='Condition Log')
provenance_review = Transition(label='Provenance Review')
material_test = Transition(label='Material Test')
spectrometry_scan = Transition(label='Spectrometry Scan')
stylistic_analysis = Transition(label='Stylistic Analysis')
expert_consult = Transition(label='Expert Consult')
archive_search = Transition(label='Archive Search')
ledger_verification = Transition(label='Ledger Verification')
secondary_review = Transition(label='Secondary Review')
cross_check = Transition(label='Cross-Check')
conservation_prep = Transition(label='Conservation Prep')
documentation = Transition(label='Documentation')
report_creation = Transition(label='Report Creation')
database_update = Transition(label='Database Update')

skip = SilentTransition()

# Define the workflow
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[intake_check, provenance_review, secondary_review])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[material_test, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[stylistic_analysis, skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[expert_consult, skip])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[archive_search, skip])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[ledger_verification, skip])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[cross_check, skip])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[conservation_prep, skip])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[documentation, skip])
xor9 = OperatorPOWL(operator=Operator.XOR, children=[report_creation, skip])
xor10 = OperatorPOWL(operator=Operator.XOR, children=[database_update, skip])

root = StrictPartialOrder(nodes=[loop1, xor1, xor2, xor3, xor4, xor5, xor6, xor7, xor8, xor9, xor10])

# Add dependencies
root.order.add_edge(loop1, xor1)
root.order.add_edge(loop1, xor2)
root.order.add_edge(loop1, xor3)
root.order.add_edge(loop1, xor4)
root.order.add_edge(loop1, xor5)
root.order.add_edge(loop1, xor6)
root.order.add_edge(loop1, xor7)
root.order.add_edge(loop1, xor8)
root.order.add_edge(loop1, xor9)
root.order.add_edge(loop1, xor10)

# Print the final result
print(root)