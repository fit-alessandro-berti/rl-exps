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

# Define the POWL model
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[spectrometry_scan, stylistic_analysis, expert_consult, archive_search, ledger_verification])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[provenance_review, secondary_review, cross_check])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[conservation_prep, documentation, report_creation])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[database_update, skip])

root = StrictPartialOrder(nodes=[intake_check, condition_log, loop1, xor1, loop2, xor2])
root.order.add_edge(intake_check, condition_log)
root.order.add_edge(condition_log, loop1)
root.order.add_edge(loop1, xor1)
root.order.add_edge(xor1, loop2)
root.order.add_edge(loop2, xor2)
root.order.add_edge(xor2, database_update)

print(root)