from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions for no-op
skip = SilentTransition()

# Define partial order nodes
intake_node = OperatorPOWL(operator=Operator.LOOP, children=[intake_check, condition_log, provenance_review])
test_node = OperatorPOWL(operator=Operator.XOR, children=[material_test, spectrometry_scan])
stylistic_node = OperatorPOWL(operator=Operator.XOR, children=[stylistic_analysis, expert_consult])
archive_node = OperatorPOWL(operator=Operator.XOR, children=[archive_search, ledger_verification])
review_node = OperatorPOWL(operator=Operator.LOOP, children=[secondary_review, cross_check])
conservation_node = OperatorPOWL(operator=Operator.LOOP, children=[conservation_prep, documentation, report_creation])
database_node = OperatorPOWL(operator=Operator.LOOP, children=[database_update])

# Define the root partial order
root = StrictPartialOrder(nodes=[intake_node, test_node, stylistic_node, archive_node, review_node, conservation_node, database_node])
root.order.add_edge(intake_node, test_node)
root.order.add_edge(test_node, stylistic_node)
root.order.add_edge(stylistic_node, archive_node)
root.order.add_edge(archive_node, review_node)
root.order.add_edge(review_node, conservation_node)
root.order.add_edge(conservation_node, database_node)

# Print the root POWL model
print(root)