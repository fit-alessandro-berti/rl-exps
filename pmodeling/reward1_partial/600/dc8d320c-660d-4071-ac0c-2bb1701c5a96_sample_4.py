import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
artifact_intake = Transition(label='Artifact Intake')
provenance_check = Transition(label='Provenance Check')
material_testing = Transition(label='Material Testing')
historical_review = Transition(label='Historical Review')
expert_interview = Transition(label='Expert Interview')
condition_audit = Transition(label='Condition Audit')
digital_catalog = Transition(label='Digital Catalog')
forgery_detection = Transition(label='Forgery Detection')
legal_compliance = Transition(label='Legal Compliance')
restoration_plan = Transition(label='Restoration Plan')
valuation_report = Transition(label='Valuation Report')
market_analysis = Transition(label='Market Analysis')
final_approval = Transition(label='Final Approval')
sale_preparation = Transition(label='Sale Preparation')
client_notification = Transition(label='Client Notification')

# Define the process steps
provenance_check_and_material_testing = OperatorPOWL(operator=Operator.XOR, children=[provenance_check, material_testing])
historical_review_and_expert_interview = OperatorPOWL(operator=Operator.XOR, children=[historical_review, expert_interview])
condition_audit_and_forgery_detection = OperatorPOWL(operator=Operator.XOR, children=[condition_audit, forgery_detection])
legal_compliance_and_restoration_plan = OperatorPOWL(operator=Operator.XOR, children=[legal_compliance, restoration_plan])
market_analysis_and_valuation_report = OperatorPOWL(operator=Operator.XOR, children=[market_analysis, valuation_report])

# Define the loop for the verification process
verification_loop = OperatorPOWL(operator=Operator.LOOP, children=[historical_review_and_expert_interview, condition_audit_and_forgery_detection, legal_compliance_and_restoration_plan, market_analysis_and_valuation_report])

# Define the final approval and sale preparation steps
final_approval_and_sale_preparation = OperatorPOWL(operator=Operator.XOR, children=[final_approval, sale_preparation])

# Define the overall process
root = StrictPartialOrder(nodes=[artifact_intake, provenance_check_and_material_testing, verification_loop, final_approval_and_sale_preparation, client_notification])
root.order.add_edge(artifact_intake, provenance_check_and_material_testing)
root.order.add_edge(provenance_check_and_material_testing, verification_loop)
root.order.add_edge(verification_loop, final_approval_and_sale_preparation)
root.order.add_edge(final_approval_and_sale_preparation, client_notification)