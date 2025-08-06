import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

skip = SilentTransition()

loop1 = OperatorPOWL(operator=Operator.LOOP, children=[material_test, spectrometry_scan])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[stylistic_analysis, expert_consult])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[archive_search, ledger_verification])

xor1 = OperatorPOWL(operator=Operator.XOR, children=[secondary_review, cross_check])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[conservation_prep, documentation])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[report_creation, database_update])

root = StrictPartialOrder(nodes=[intake_check, condition_log, provenance_review, loop1, loop2, loop3, xor1, xor2, xor3])
root.order.add_edge(intake_check, provenance_review)
root.order.add_edge(provenance_review, material_test)
root.order.add_edge(material_test, spectrometry_scan)
root.order.add_edge(spectrometry_scan, stylistic_analysis)
root.order.add_edge(stylistic_analysis, expert_consult)
root.order.add_edge(expert_consult, archive_search)
root.order.add_edge(archive_search, ledger_verification)
root.order.add_edge(ledger_verification, secondary_review)
root.order.add_edge(secondary_review, cross_check)
root.order.add_edge(cross_check, conservation_prep)
root.order.add_edge(conservation_prep, documentation)
root.order.add_edge(documentation, report_creation)
root.order.add_edge(report_creation, database_update)