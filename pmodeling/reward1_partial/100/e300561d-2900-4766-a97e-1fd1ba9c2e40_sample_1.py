import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
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

# Define silent transitions
skip1 = SilentTransition()
skip2 = SilentTransition()
skip3 = SilentTransition()

# Define the partial order structure
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[material_test, spectrometry_scan])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[stylistic_analysis, expert_consult, archive_search, ledger_verification])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[cross_check, secondary_review])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[provenance_review, skip1])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[conservation_prep, documentation])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[report_creation, database_update])

# Define the root partial order
root = StrictPartialOrder(nodes=[intake_check, condition_log, xor1, loop1, xor2, loop2, xor3, loop3])
root.order.add_edge(intake_check, condition_log)
root.order.add_edge(condition_log, xor1)
root.order.add_edge(xor1, loop1)
root.order.add_edge(loop1, xor2)
root.order.add_edge(xor2, loop2)
root.order.add_edge(loop2, xor3)
root.order.add_edge(xor3, loop3)

# Print the root partial order
print(root)