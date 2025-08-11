import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
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
skip = SilentTransition()

# Define loop nodes
loop_1 = OperatorPOWL(operator=Operator.LOOP, children=[material_test, spectroscopy_scan])
loop_2 = OperatorPOWL(operator=Operator.LOOP, children=[stylistic_analysis, expert_consult])

# Define exclusive choice nodes
xor_1 = OperatorPOWL(operator=Operator.XOR, children=[provenance_review, skip])
xor_2 = OperatorPOWL(operator=Operator.XOR, children=[archive_search, ledger_verification])

# Define root
root = StrictPartialOrder(nodes=[intake_check, condition_log, xor_1, xor_2, loop_1, loop_2, conservation_prep, documentation, report_creation, database_update])
root.order.add_edge(intake_check, condition_log)
root.order.add_edge(condition_log, xor_1)
root.order.add_edge(xor_1, loop_1)
root.order.add_edge(loop_1, xor_2)
root.order.add_edge(xor_2, loop_2)
root.order.add_edge(loop_2, conservation_prep)
root.order.add_edge(conservation_prep, documentation)
root.order.add_edge(documentation, report_creation)
root.order.add_edge(report_creation, database_update)