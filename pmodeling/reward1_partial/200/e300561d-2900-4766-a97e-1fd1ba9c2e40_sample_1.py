import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with their labels
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

# Define the silent transition (tau)
skip = SilentTransition()

# Define the partial order structure
loop_1 = OperatorPOWL(operator=Operator.LOOP, children=[intake_check, condition_log, provenance_review, material_test, spectrometry_scan, stylistic_analysis, expert_consult])
loop_2 = OperatorPOWL(operator=Operator.LOOP, children=[archive_search, ledger_verification, secondary_review, cross_check])
xor_1 = OperatorPOWL(operator=Operator.XOR, children=[conservation_prep, documentation])
xor_2 = OperatorPOWL(operator=Operator.XOR, children=[report_creation, database_update])

# Define the root partial order
root = StrictPartialOrder(nodes=[loop_1, loop_2, xor_1, xor_2])
root.order.add_edge(loop_1, loop_2)
root.order.add_edge(loop_2, xor_1)
root.order.add_edge(loop_2, xor_2)

# Print the root partial order
print(root)