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

# Define the silent transitions
skip = SilentTransition()

# Define the POWL model structure
loop_1 = OperatorPOWL(operator=Operator.LOOP, children=[material_test, spectrometry_scan])
xor_1 = OperatorPOWL(operator=Operator.XOR, children=[stylistic_analysis, skip])
loop_2 = OperatorPOWL(operator=Operator.LOOP, children=[archive_search, ledger_verification])
xor_2 = OperatorPOWL(operator=Operator.XOR, children=[expert_consult, skip])
xor_3 = OperatorPOWL(operator=Operator.XOR, children=[secondary_review, skip])
xor_4 = OperatorPOWL(operator=Operator.XOR, children=[cross_check, skip])
loop_3 = OperatorPOWL(operator=Operator.LOOP, children=[conservation_prep, documentation])
xor_5 = OperatorPOWL(operator=Operator.XOR, children=[report_creation, skip])
xor_6 = OperatorPOWL(operator=Operator.XOR, children=[database_update, skip])

# Create the root POWL model
root = StrictPartialOrder(nodes=[intake_check, condition_log, provenance_review, loop_1, xor_1, loop_2, xor_2, xor_3, xor_4, loop_3, xor_5, xor_6])
root.order.add_edge(intake_check, condition_log)
root.order.add_edge(condition_log, provenance_review)
root.order.add_edge(provenance_review, loop_1)
root.order.add_edge(loop_1, xor_1)
root.order.add_edge(xor_1, loop_2)
root.order.add_edge(loop_2, xor_2)
root.order.add_edge(xor_2, xor_3)
root.order.add_edge(xor_3, xor_4)
root.order.add_edge(xor_4, loop_3)
root.order.add_edge(loop_3, xor_5)
root.order.add_edge(xor_5, xor_6)
root.order.add_edge(xor_6, database_update)

print(root)