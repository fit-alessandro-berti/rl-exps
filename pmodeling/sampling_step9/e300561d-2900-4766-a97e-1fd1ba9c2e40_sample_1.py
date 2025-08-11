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

# Define operators
xor = OperatorPOWL(operator=Operator.XOR, children=[secondary_review, skip])
loop = OperatorPOWL(operator=Operator.LOOP, children=[provenance_review, archive_search, ledger_verification])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[conservation_prep, documentation])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[report_creation, database_update])

# Define POWL model
root = StrictPartialOrder(nodes=[intake_check, condition_log, material_test, spectrometry_scan, stylistic_analysis, xor, loop, expert_consult, xor2, xor3])

# Define edges
root.order.add_edge(intake_check, condition_log)
root.order.add_edge(condition_log, material_test)
root.order.add_edge(material_test, spectrometry_scan)
root.order.add_edge(spectrometry_scan, stylistic_analysis)
root.order.add_edge(stylistic_analysis, xor)
root.order.add_edge(provenance_review, archive_search)
root.order.add_edge(archive_search, ledger_verification)
root.order.add_edge(ledger_verification, xor)
root.order.add_edge(expert_consult, xor)
root.order.add_edge(conservation_prep, documentation)
root.order.add_edge(documentation, xor2)
root.order.add_edge(report_creation, database_update)
root.order.add_edge(database_update, xor3)

print(root)