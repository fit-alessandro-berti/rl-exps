import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the silent transitions (empty labels)
skip = SilentTransition()

# Define the partial order structure
loop = OperatorPOWL(operator=Operator.LOOP, children=[material_test, spectrometry_scan, stylistic_analysis, expert_consult, archive_search, ledger_verification])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[cross_check, secondary_review])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[conservation_prep, documentation])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[report_creation, database_update])

# Define the root partial order
root = StrictPartialOrder(nodes=[intake_check, condition_log, provenance_review, loop, xor1, xor2, xor3])

# Define the dependencies between nodes
root.order.add_edge(intake_check, condition_log)
root.order.add_edge(condition_log, provenance_review)
root.order.add_edge(provenance_review, loop)
root.order.add_edge(loop, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, report_creation)
root.order.add_edge(xor3, database_update)

# Print the root partial order
print(root)