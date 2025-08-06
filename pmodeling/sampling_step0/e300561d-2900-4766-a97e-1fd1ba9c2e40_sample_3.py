import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
root = StrictPartialOrder()

# Intake Check activity
intake_check = Transition(label='Intake Check')
root.nodes.add(intake_check)

# Condition Log activity
condition_log = Transition(label='Condition Log')
root.nodes.add(condition_log)

# Provenance Review activity
provenance_review = Transition(label='Provenance Review')
root.nodes.add(provenance_review)

# Material Test activity
material_test = Transition(label='Material Test')
root.nodes.add(material_test)

# Spectrometry Scan activity
spectrometry_scan = Transition(label='Spectrometry Scan')
root.nodes.add(spectrometry_scan)

# Stylistic Analysis activity
stylistic_analysis = Transition(label='Stylistic Analysis')
root.nodes.add(stylistic_analysis)

# Expert Consult activity
expert_consult = Transition(label='Expert Consult')
root.nodes.add(expert_consult)

# Archive Search activity
archive_search = Transition(label='Archive Search')
root.nodes.add(archive_search)

# Ledger Verification activity
ledger_verification = Transition(label='Ledger Verification')
root.nodes.add(ledger_verification)

# Secondary Review activity
secondary_review = Transition(label='Secondary Review')
root.nodes.add(secondary_review)

# Cross-Check activity
cross_check = Transition(label='Cross-Check')
root.nodes.add(cross_check)

# Conservation Prep activity
conservation_prep = Transition(label='Conservation Prep')
root.nodes.add(conservation_prep)

# Documentation activity
documentation = Transition(label='Documentation')
root.nodes.add(documentation)

# Report Creation activity
report_creation = Transition(label='Report Creation')
root.nodes.add(report_creation)

# Database Update activity
database_update = Transition(label='Database Update')
root.nodes.add(database_update)

# Add dependencies between activities
root.order.add_edge(intake_check, condition_log)
root.order.add_edge(intake_check, provenance_review)
root.order.add_edge(condition_log, material_test)
root.order.add_edge(provenance_review, expert_consult)
root.order.add_edge(provenance_review, archive_search)
root.order.add_edge(provenance_review, ledger_verification)
root.order.add_edge(expert_consult, secondary_review)
root.order.add_edge(archive_search, secondary_review)
root.order.add_edge(ledger_verification, secondary_review)
root.order.add_edge(secondary_review, cross_check)
root.order.add_edge(cross_check, material_test)
root.order.add_edge(material_test, conservation_prep)
root.order.add_edge(conservation_prep, documentation)
root.order.add_edge(documentation, report_creation)
root.order.add_edge(report_creation, database_update)

# Set the final activity (root) to the last activity in the model
root.final = database_update

print(root)