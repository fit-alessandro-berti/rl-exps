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

# Define silent transitions (empty labels)
skip = SilentTransition()

# Define partial order nodes
intake_check_node = OperatorPOWL(operator=Operator.ACTIVITY, children=[intake_check])
condition_log_node = OperatorPOWL(operator=Operator.ACTIVITY, children=[condition_log])
provenance_review_node = OperatorPOWL(operator=Operator.ACTIVITY, children=[provenance_review])
material_test_node = OperatorPOWL(operator=Operator.ACTIVITY, children=[material_test])
spectrometry_scan_node = OperatorPOWL(operator=Operator.ACTIVITY, children=[spectrometry_scan])
stylistic_analysis_node = OperatorPOWL(operator=Operator.ACTIVITY, children=[stylistic_analysis])
expert_consult_node = OperatorPOWL(operator=Operator.ACTIVITY, children=[expert_consult])
archive_search_node = OperatorPOWL(operator=Operator.ACTIVITY, children=[archive_search])
ledger_verification_node = OperatorPOWL(operator=Operator.ACTIVITY, children=[ledger_verification])
secondary_review_node = OperatorPOWL(operator=Operator.ACTIVITY, children=[secondary_review])
cross_check_node = OperatorPOWL(operator=Operator.ACTIVITY, children=[cross_check])
conservation_prep_node = OperatorPOWL(operator=Operator.ACTIVITY, children=[conservation_prep])
documentation_node = OperatorPOWL(operator=Operator.ACTIVITY, children=[documentation])
report_creation_node = OperatorPOWL(operator=Operator.ACTIVITY, children=[report_creation])
database_update_node = OperatorPOWL(operator=Operator.ACTIVITY, children=[database_update])

# Define partial order
root = StrictPartialOrder(nodes=[
    intake_check_node,
    condition_log_node,
    provenance_review_node,
    material_test_node,
    spectrometry_scan_node,
    stylistic_analysis_node,
    expert_consult_node,
    archive_search_node,
    ledger_verification_node,
    secondary_review_node,
    cross_check_node,
    conservation_prep_node,
    documentation_node,
    report_creation_node,
    database_update_node
])

# Define dependencies between nodes
root.order.add_edge(intake_check_node, condition_log_node)
root.order.add_edge(intake_check_node, provenance_review_node)
root.order.add_edge(condition_log_node, material_test_node)
root.order.add_edge(provenance_review_node, material_test_node)
root.order.add_edge(material_test_node, spectrometry_scan_node)
root.order.add_edge(material_test_node, stylistic_analysis_node)
root.order.add_edge(spectrometry_scan_node, expert_consult_node)
root.order.add_edge(stylistic_analysis_node, expert_consult_node)
root.order.add_edge(expert_consult_node, archive_search_node)
root.order.add_edge(archive_search_node, ledger_verification_node)
root.order.add_edge(ledger_verification_node, secondary_review_node)
root.order.add_edge(secondary_review_node, cross_check_node)
root.order.add_edge(cross_check_node, conservation_prep_node)
root.order.add_edge(conservation_prep_node, documentation_node)
root.order.add_edge(documentation_node, report_creation_node)
root.order.add_edge(report_creation_node, database_update_node)