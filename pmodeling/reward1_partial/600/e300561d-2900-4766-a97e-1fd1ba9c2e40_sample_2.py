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

# Define silent transitions for transitions without labels
skip = SilentTransition()

# Define the partial order
root = StrictPartialOrder()

# Define the partial order graph
root.nodes.append(intake_check)
root.nodes.append(condition_log)
root.nodes.append(provenance_review)
root.nodes.append(material_test)
root.nodes.append(spectrometry_scan)
root.nodes.append(stylistic_analysis)
root.nodes.append(expert_consult)
root.nodes.append(archive_search)
root.nodes.append(ledger_verification)
root.nodes.append(secondary_review)
root.nodes.append(cross_check)
root.nodes.append(conservation_prep)
root.nodes.append(documentation)
root.nodes.append(report_creation)
root.nodes.append(database_update)

# Define the dependencies
root.order.add_edge(intake_check, condition_log)
root.order.add_edge(intake_check, provenance_review)
root.order.add_edge(condition_log, material_test)
root.order.add_edge(condition_log, stylistic_analysis)
root.order.add_edge(provenance_review, expert_consult)
root.order.add_edge(provenance_review, archive_search)
root.order.add_edge(provenance_review, ledger_verification)
root.order.add_edge(provenance_review, secondary_review)
root.order.add_edge(material_test, spectrometry_scan)
root.order.add_edge(material_test, stylistic_analysis)
root.order.add_edge(expert_consult, archive_search)
root.order.add_edge(expert_consult, ledger_verification)
root.order.add_edge(expert_consult, secondary_review)
root.order.add_edge(archive_search, ledger_verification)
root.order.add_edge(archive_search, cross_check)
root.order.add_edge(ledger_verification, cross_check)
root.order.add_edge(secondary_review, cross_check)
root.order.add_edge(cross_check, conservation_prep)
root.order.add_edge(conservation_prep, documentation)
root.order.add_edge(conservation_prep, report_creation)
root.order.add_edge(conservation_prep, database_update)

# Print the final result
print(root)