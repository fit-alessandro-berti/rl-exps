from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL nodes
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

# Define the POWL operators
xor = OperatorPOWL(operator=Operator.XOR, children=[provenance_review, material_test])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[stylistic_analysis, expert_consult])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[archive_search, ledger_verification])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[secondary_review, cross_check])
loop = OperatorPOWL(operator=Operator.LOOP, children=[conservation_prep, documentation])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[report_creation, database_update])

# Define the POWL partial order
root = StrictPartialOrder(nodes=[intake_check, condition_log, xor, xor2, xor3, xor4, loop, xor5])
root.order.add_edge(intake_check, condition_log)
root.order.add_edge(condition_log, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, loop)
root.order.add_edge(loop, xor5)
root.order.add_edge(xor5, root)

# Print the POWL model
print(root)