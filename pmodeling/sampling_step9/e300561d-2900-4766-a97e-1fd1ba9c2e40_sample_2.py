import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
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

# Define loops and choices
loop_condition_log = OperatorPOWL(operator=Operator.LOOP, children=[intake_check, condition_log])
loop_material_test = OperatorPOWL(operator=Operator.LOOP, children=[material_test, spectrometry_scan, stylistic_analysis])
loop_expert_consult = OperatorPOWL(operator=Operator.LOOP, children=[expert_consult, archive_search, ledger_verification, secondary_review, cross_check])
loop_conservation_prep = OperatorPOWL(operator=Operator.LOOP, children=[conservation_prep, documentation, report_creation, database_update])

# Define the root POWL model
root = StrictPartialOrder(nodes=[loop_condition_log, loop_material_test, loop_expert_consult, loop_conservation_prep])
root.order.add_edge(loop_condition_log, loop_material_test)
root.order.add_edge(loop_material_test, loop_expert_consult)
root.order.add_edge(loop_expert_consult, loop_conservation_prep)

# Print the root POWL model
print(root)