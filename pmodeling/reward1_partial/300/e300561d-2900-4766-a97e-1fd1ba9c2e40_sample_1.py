import pm4py
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

# Define silent transitions
skip = SilentTransition()

# Define the POWL model
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[material_test, spectrometry_scan, stylistic_analysis, expert_consult])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[archive_search, ledger_verification, secondary_review, cross_check])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[provenance_review, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[conservation_prep, documentation])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[report_creation, database_update])

root = StrictPartialOrder(nodes=[intake_check, condition_log, loop1, loop2, xor1, xor2, xor3])
root.order.add_edge(intake_check, condition_log)
root.order.add_edge(condition_log, loop1)
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)

print(root)