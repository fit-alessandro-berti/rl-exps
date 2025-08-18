from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the transitions
# Intake Check --> Condition Log
intake_check_to_condition_log = OperatorPOWL(operator=Operator.SEQUENCE, children=[intake_check, condition_log])

# Condition Log --> Provenance Review
condition_log_to_provenance_review = OperatorPOWL(operator=Operator.SEQUENCE, children=[condition_log, provenance_review])

# Provenance Review --> Material Test
provenance_review_to_material_test = OperatorPOWL(operator=Operator.SEQUENCE, children=[provenance_review, material_test])

# Material Test --> Spectrometry Scan
material_test_to_spectrometry_scan = OperatorPOWL(operator=Operator.SEQUENCE, children=[material_test, spectrometry_scan])

# Spectrometry Scan --> Stylistic Analysis
spectrometry_scan_to_stylistic_analysis = OperatorPOWL(operator=Operator.SEQUENCE, children=[spectrometry_scan, stylistic_analysis])

# Stylistic Analysis --> Expert Consult
stylistic_analysis_to_expert_consult = OperatorPOWL(operator=Operator.SEQUENCE, children=[stylistic_analysis, expert_consult])

# Expert Consult --> Archive Search
expert_consult_to_archive_search = OperatorPOWL(operator=Operator.SEQUENCE, children=[expert_consult, archive_search])

# Archive Search --> Ledger Verification
archive_search_to_ledger_verification = OperatorPOWL(operator=Operator.SEQUENCE, children=[archive_search, ledger_verification])

# Ledger Verification --> Secondary Review
ledger_verification_to_secondary_review = OperatorPOWL(operator=Operator.SEQUENCE, children=[ledger_verification, secondary_review])

# Secondary Review --> Cross-Check
secondary_review_to_cross_check = OperatorPOWL(operator=Operator.SEQUENCE, children=[secondary_review, cross_check])

# Cross-Check --> Conservation Prep
cross_check_to_conservation_prep = OperatorPOWL(operator=Operator.SEQUENCE, children=[cross_check, conservation_prep])

# Conservation Prep --> Documentation
conservation_prep_to_documentation = OperatorPOWL(operator=Operator.SEQUENCE, children=[conservation_prep, documentation])

# Documentation --> Report Creation
documentation_to_report_creation = OperatorPOWL(operator=Operator.SEQUENCE, children=[documentation, report_creation])

# Report Creation --> Database Update
report_creation_to_database_update = OperatorPOWL(operator=Operator.SEQUENCE, children=[report_creation, database_update])

# Define the final POWL model
root = StrictPartialOrder(nodes=[intake_check_to_condition_log, condition_log_to_provenance_review, provenance_review_to_material_test, material_test_to_spectrometry_scan, spectrometry_scan_to_stylistic_analysis, stylistic_analysis_to_expert_consult, expert_consult_to_archive_search, archive_search_to_ledger_verification, ledger_verification_to_secondary_review, secondary_review_to_cross_check, cross_check_to_conservation_prep, conservation_prep_to_documentation, documentation_to_report_creation, report_creation_to_database_update])

# Add the dependencies
root.order.add_edge(intake_check_to_condition_log, condition_log_to_provenance_review)
root.order.add_edge(condition_log_to_provenance_review, provenance_review_to_material_test)
root.order.add_edge(provenance_review_to_material_test, material_test_to_spectrometry_scan)
root.order.add_edge(material_test_to_spectrometry_scan, spectrometry_scan_to_stylistic_analysis)
root.order.add_edge(spectrometry_scan_to_stylistic_analysis, stylistic_analysis_to_expert_consult)
root.order.add_edge(stylistic_analysis_to_expert_consult, expert_consult_to_archive_search)
root.order.add_edge(expert_consult_to_archive_search, archive_search_to_ledger_verification)
root.order.add_edge(archive_search_to_ledger_verification, ledger_verification_to_secondary_review)
root.order.add_edge(ledger_verification_to_secondary_review, secondary_review_to_cross_check)
root.order.add_edge(secondary_review_to_cross_check, cross_check_to_conservation_prep)
root.order.add_edge(cross_check_to_conservation_prep, conservation_prep_to_documentation)
root.order.add_edge(conservation_prep_to_documentation, documentation_to_report_creation)
root.order.add_edge(documentation_to_report_creation, report_creation_to_database_update)