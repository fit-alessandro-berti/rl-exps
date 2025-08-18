from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

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

# Define partial order for each step
intake_check_log = StrictPartialOrder(nodes=[intake_check, condition_log])
provenance_log = StrictPartialOrder(nodes=[provenance_review, material_test, spectrometry_scan, stylistic_analysis])
expert_consult_log = StrictPartialOrder(nodes=[expert_consult, archive_search, ledger_verification, secondary_review, cross_check])
conservation_prep_log = StrictPartialOrder(nodes=[conservation_prep, documentation])
report_database_log = StrictPartialOrder(nodes=[report_creation, database_update])

# Define partial order for the entire process
root = StrictPartialOrder(nodes=[intake_check_log, provenance_log, expert_consult_log, conservation_prep_log, report_database_log])
root.order.add_edge(intake_check_log, provenance_log)
root.order.add_edge(provenance_log, expert_consult_log)
root.order.add_edge(expert_consult_log, conservation_prep_log)
root.order.add_edge(conservation_prep_log, report_database_log)