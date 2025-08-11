import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

artifact_intake = Transition(label='Artifact Intake')
initial_survey = Transition(label='Initial Survey')
material_test = Transition(label='Material Test')
historical_check = Transition(label='Historical Check')
registry_search = Transition(label='Registry Search')
owner_interview = Transition(label='Owner Interview')
condition_report = Transition(label='Condition Report')
forgery_scan = Transition(label='Forgery Scan')
digital_tagging = Transition(label='Digital Tagging')
ledger_entry = Transition(label='Ledger Entry')
expert_review = Transition(label='Expert Review')
legal_verify = Transition(label='Legal Verify')
provenance_draft = Transition(label='Provenance Draft')
client_approval = Transition(label='Client Approval')
final_certificate = Transition(label='Final Certificate')
archive_storage = Transition(label='Archive Storage')

skip = SilentTransition()

# Material Test and Initial Survey
material_test_survey = OperatorPOWL(operator=Operator.XOR, children=[material_test, initial_survey])

# Registry Search and Owner Interview
registry_search_owner_interview = OperatorPOWL(operator=Operator.XOR, children=[registry_search, owner_interview])

# Forgery Scan and Condition Report
forgery_scan_condition_report = OperatorPOWL(operator=Operator.XOR, children=[forgery_scan, condition_report])

# Digital Tagging and Ledger Entry
digital_tagging_ledger_entry = OperatorPOWL(operator=Operator.XOR, children=[digital_tagging, ledger_entry])

# Expert Review and Legal Verify
expert_review_legal_verify = OperatorPOWL(operator=Operator.XOR, children=[expert_review, legal_verify])

# Provenance Draft and Client Approval
provenance_draft_client_approval = OperatorPOWL(operator=Operator.XOR, children=[provenance_draft, client_approval])

# Final Certificate and Archive Storage
final_certificate_archive_storage = OperatorPOWL(operator=Operator.XOR, children=[final_certificate, archive_storage])

# Loop for the first set of verification stages
loop_1 = OperatorPOWL(operator=Operator.LOOP, children=[material_test_survey, registry_search_owner_interview])

# Loop for the second set of verification stages
loop_2 = OperatorPOWL(operator=Operator.LOOP, children=[forgery_scan_condition_report, digital_tagging_ledger_entry])

# Loop for the third set of verification stages
loop_3 = OperatorPOWL(operator=Operator.LOOP, children=[expert_review_legal_verify, provenance_draft_client_approval])

# Loop for the fourth set of verification stages
loop_4 = OperatorPOWL(operator=Operator.LOOP, children=[final_certificate_archive_storage])

# Create the root POWL model
root = StrictPartialOrder(nodes=[loop_1, loop_2, loop_3, loop_4])
root.order.add_edge(loop_1, loop_2)
root.order.add_edge(loop_2, loop_3)
root.order.add_edge(loop_3, loop_4)