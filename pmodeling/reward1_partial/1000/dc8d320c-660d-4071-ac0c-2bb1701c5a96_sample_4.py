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
forgeries_detection = Transition(label='Forgery Detection')
legal_compliance = Transition(label='Legal Compliance')
restoration_plan = Transition(label='Restoration Plan')
valuation_report = Transition(label='Valuation Report')
market_analysis = Transition(label='Market Analysis')
final_approval = Transition(label='Final Approval')
sale_preparation = Transition(label='Sale Preparation')
client_notification = Transition(label='Client Notification')

# Define the process steps
provenance_check_node = OperatorPOWL(operator=Operator.PO, children=[provenance_check])
material_testing_node = OperatorPOWL(operator=Operator.PO, children=[material_testing])
historical_review_node = OperatorPOWL(operator=Operator.PO, children=[historical_review])
expert_interview_node = OperatorPOWL(operator=Operator.PO, children=[expert_interview])
condition_audit_node = OperatorPOWL(operator=Operator.PO, children=[condition_audit])
digital_catalog_node = OperatorPOWL(operator=Operator.PO, children=[digital_catalog])
forgeries_detection_node = OperatorPOWL(operator=Operator.PO, children=[forgeries_detection])
legal_compliance_node = OperatorPOWL(operator=Operator.PO, children=[legal_compliance])
restoration_plan_node = OperatorPOWL(operator=Operator.PO, children=[restoration_plan])
valuation_report_node = OperatorPOWL(operator=Operator.PO, children=[valuation_report])
market_analysis_node = OperatorPOWL(operator=Operator.PO, children=[market_analysis])
final_approval_node = OperatorPOWL(operator=Operator.PO, children=[final_approval])
sale_preparation_node = OperatorPOWL(operator=Operator.PO, children=[sale_preparation])
client_notification_node = OperatorPOWL(operator=Operator.PO, children=[client_notification])

# Define the partial order
root = StrictPartialOrder(nodes=[artifact_intake, provenance_check_node, material_testing_node, historical_review_node, expert_interview_node, condition_audit_node, digital_catalog_node, forgeries_detection_node, legal_compliance_node, restoration_plan_node, valuation_report_node, market_analysis_node, final_approval_node, sale_preparation_node, client_notification_node])

# Define the dependencies
root.order.add_edge(artifact_intake, provenance_check_node)
root.order.add_edge(artifact_intake, material_testing_node)
root.order.add_edge(artifact_intake, historical_review_node)
root.order.add_edge(artifact_intake, expert_interview_node)
root.order.add_edge(artifact_intake, condition_audit_node)
root.order.add_edge(artifact_intake, digital_catalog_node)
root.order.add_edge(artifact_intake, forgeries_detection_node)
root.order.add_edge(artifact_intake, legal_compliance_node)
root.order.add_edge(artifact_intake, restoration_plan_node)
root.order.add_edge(artifact_intake, valuation_report_node)
root.order.add_edge(artifact_intake, market_analysis_node)
root.order.add_edge(artifact_intake, final_approval_node)
root.order.add_edge(artifact_intake, sale_preparation_node)
root.order.add_edge(artifact_intake, client_notification_node)