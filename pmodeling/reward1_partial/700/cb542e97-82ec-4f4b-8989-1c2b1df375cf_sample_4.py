import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
artifact_intake = Transition(label='Artifact Intake')
condition_check = Transition(label='Condition Check')
material_test = Transition(label='Material Test')
archival_search = Transition(label='Archival Search')
style_compare = Transition(label='Style Compare')
expert_review = Transition(label='Expert Review')
restoration_check = Transition(label='Restoration Check')
provenance_trace = Transition(label='Provenance Trace')
legal_verify = Transition(label='Legal Verify')
value_appraise = Transition(label='Value Appraise')
catalog_entry = Transition(label='Catalog Entry')
marketing_plan = Transition(label='Marketing Plan')
auction_setup = Transition(label='Auction Setup')
certify_final = Transition(label='Certify Final')
sales_report = Transition(label='Sales Report')

# Define the workflow
artifact_intake -> condition_check
condition_check -> material_test
material_test -> archival_search
archival_search -> style_compare
style_compare -> expert_review
expert_review -> restoration_check
restoration_check -> provenance_trace
provenance_trace -> legal_verify
legal_verify -> value_appraise
value_appraise -> catalog_entry
catalog_entry -> marketing_plan
marketing_plan -> auction_setup
auction_setup -> certify_final
certify_final -> sales_report

# Create the POWL model
root = StrictPartialOrder(nodes=[artifact_intake, condition_check, material_test, archival_search, style_compare, expert_review, restoration_check, provenance_trace, legal_verify, value_appraise, catalog_entry, marketing_plan, auction_setup, certify_final, sales_report])