import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define the atomic activities
intake_check       = Transition(label='Intake Check')
condition_log      = Transition(label='Condition Log')
provenance_review  = Transition(label='Provenance Review')
material_test      = Transition(label='Material Test')
spectrometry_scan  = Transition(label='Spectrometry Scan')
stylistic_analysis = Transition(label='Stylistic Analysis')
expert_consult     = Transition(label='Expert Consult')
archive_search     = Transition(label='Archive Search')
ledger_verification= Transition(label='Ledger Verification')
secondary_review   = Transition(label='Secondary Review')
cross_check        = Transition(label='Cross-Check')
conservation_prep  = Transition(label='Conservation Prep')
documentation      = Transition(label='Documentation')
report_creation    = Transition(label='Report Creation')
database_update    = Transition(label='Database Update')

# Build the partial order
root = StrictPartialOrder(nodes=[
    intake_check,
    condition_log,
    provenance_review,
    material_test,
    spectrometry_scan,
    stylistic_analysis,
    expert_consult,
    archive_search,
    ledger_verification,
    secondary_review,
    cross_check,
    conservation_prep,
    documentation,
    report_creation,
    database_update
])

# Define the control-flow dependencies
root.order.add_edge(intake_check, condition_log)
root.order.add_edge(condition_log, provenance_review)

# Material testing and analysis are concurrent after provenance review
root.order.add_edge(provenance_review, material_test)
root.order.add_edge(provenance_review, stylistic_analysis)

# Material test and spectral scan are concurrent
root.order.add_edge(material_test, spectrometry_scan)

# Stylistic analysis and expert consultation are concurrent
root.order.add_edge(stylistic_analysis, expert_consult)

# Both tests trigger the secondary review
root.order.add_edge(spectrometry_scan, secondary_review)
root.order.add_edge(stylistic_analysis, secondary_review)

# Secondary review triggers cross-check
root.order.add_edge(secondary_review, cross_check)

# Cross-check triggers the rest
for target in [
    archive_search,
    ledger_verification,
    conservation_prep,
    documentation,
    report_creation,
    database_update
]:
    root.order.add_edge(cross_check, target)