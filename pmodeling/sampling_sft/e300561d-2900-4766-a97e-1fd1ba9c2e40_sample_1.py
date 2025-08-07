import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
intake_check     = Transition(label='Intake Check')
condition_log    = Transition(label='Condition Log')
provenance_review= Transition(label='Provenance Review')
material_test    = Transition(label='Material Test')
spectrometry_scan= Transition(label='Spectrometry Scan')
stylistic_analysis=Transition(label='Stylistic Analysis')
expert_consult   = Transition(label='Expert Consult')
archive_search   = Transition(label='Archive Search')
ledger_verification=Transition(label='Ledger Verification')
secondary_review = Transition(label='Secondary Review')
cross_check      = Transition(label='Cross-Check')
conservation_prep= Transition(label='Conservation Prep')
documentation    = Transition(label='Documentation')
report_creation  = Transition(label='Report Creation')
database_update  = Transition(label='Database Update')

# Build the partial‐order workflow
root = StrictPartialOrder(nodes=[
    intake_check, condition_log, provenance_review, material_test, spectrometry_scan,
    stylistic_analysis, expert_consult, archive_search, ledger_verification,
    secondary_review, cross_check, conservation_prep, documentation, report_creation,
    database_update
])

# Initial intake and condition logging
root.order.add_edge(intake_check, condition_log)

# Material test and provenance review are concurrent
root.order.add_edge(material_test, provenance_review)
root.order.add_edge(spectrometry_scan, provenance_review)

# Style analysis and expert consult are concurrent
root.order.add_edge(stylistic_analysis, expert_consult)
root.order.add_edge(expert_consult, provenance_review)

# Provenance review triggers archival search and ledger verification
root.order.add_edge(provenance_review, archive_search)
root.order.add_edge(provenance_review, ledger_verification)

# Cross‐check is optional after archival search and ledger verification
root.order.add_edge(archive_search, cross_check)
root.order.add_edge(ledger_verification, cross_check)

# All results are required before the conservation prep
root.order.add_edge(archive_search, conservation_prep)
root.order.add_edge(ledger_verification, conservation_prep)
root.order.add_edge(cross_check, conservation_prep)

# Conservation prep then documentation, then report creation, then database update
root.order.add_edge(conservation_prep, documentation)
root.order.add_edge(documentation, report_creation)
root.order.add_edge(report_creation, database_update)