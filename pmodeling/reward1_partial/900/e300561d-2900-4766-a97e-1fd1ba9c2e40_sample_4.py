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
root = StrictPartialOrder()

# Add transitions to the root
root.nodes.add(intake_check)
root.nodes.add(condition_log)
root.nodes.add(provenance_review)
root.nodes.add(material_test)
root.nodes.add(spectrometry_scan)
root.nodes.add(stylistic_analysis)
root.nodes.add(expert_consult)
root.nodes.add(archive_search)
root.nodes.add(ledger_verification)
root.nodes.add(secondary_review)
root.nodes.add(cross_check)
root.nodes.add(conservation_prep)
root.nodes.add(documentation)
root.nodes.add(report_creation)
root.nodes.add(database_update)

# Define the partial order
root.order.add_edge(intake_check, condition_log)
root.order.add_edge(condition_log, provenance_review)
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

print(root)