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

# Define loops and choices
loop_1 = OperatorPOWL(operator=Operator.LOOP, children=[intake_check, condition_log])
loop_2 = OperatorPOWL(operator=Operator.LOOP, children=[provenance_review, material_test])
choice_1 = OperatorPOWL(operator=Operator.XOR, children=[spectrometry_scan, stylistic_analysis])
choice_2 = OperatorPOWL(operator=Operator.XOR, children=[expert_consult, archive_search])
choice_3 = OperatorPOWL(operator=Operator.XOR, children=[ledger_verification, cross_check])
choice_4 = OperatorPOWL(operator=Operator.XOR, children=[secondary_review, cross_check])
loop_3 = OperatorPOWL(operator=Operator.LOOP, children=[conservation_prep, documentation])
choice_5 = OperatorPOWL(operator=Operator.XOR, children=[report_creation, database_update])

# Define the root POWL model
root = StrictPartialOrder(nodes=[loop_1, choice_1, loop_2, choice_2, choice_3, choice_4, loop_3, choice_5])
root.order.add_edge(loop_1, choice_1)
root.order.add_edge(choice_1, loop_2)
root.order.add_edge(loop_2, choice_2)
root.order.add_edge(choice_2, choice_3)
root.order.add_edge(choice_3, choice_4)
root.order.add_edge(choice_4, loop_3)
root.order.add_edge(loop_3, choice_5)
root.order.add_edge(choice_5, root)

print(root)