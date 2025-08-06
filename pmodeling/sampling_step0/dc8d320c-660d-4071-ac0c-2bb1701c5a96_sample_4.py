import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define silent transitions
skip = SilentTransition()

# Define the loop for each activity
loop_provenance_check = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check])
loop_material_testing = OperatorPOWL(operator=Operator.LOOP, children=[material_testing])
loop_historical_review = OperatorPOWL(operator=Operator.LOOP, children=[historical_review])
loop_expert_interview = OperatorPOWL(operator=Operator.LOOP, children=[expert_interview])
loop_condition_audit = OperatorPOWL(operator=Operator.LOOP, children=[condition_audit])
loop_forgeries_detection = OperatorPOWL(operator=Operator.LOOP, children=[forgeries_detection])
loop_legal_compliance = OperatorPOWL(operator=Operator.LOOP, children=[legal_compliance])
loop_restoration_plan = OperatorPOWL(operator=Operator.LOOP, children=[restoration_plan])
loop_valuation_report = OperatorPOWL(operator=Operator.LOOP, children=[valuation_report])
loop_market_analysis = OperatorPOWL(operator=Operator.LOOP, children=[market_analysis])
loop_sale_preparation = OperatorPOWL(operator=Operator.LOOP, children=[sale_preparation])
loop_client_notification = OperatorPOWL(operator=Operator.LOOP, children=[client_notification])

# Define the XOR for the final steps
xor_final_approval_sale_preparation = OperatorPOWL(operator=Operator.XOR, children=[final_approval, sale_preparation])

# Define the root node
root = StrictPartialOrder(nodes=[artifact_intake, loop_provenance_check, loop_material_testing, loop_historical_review, loop_expert_interview, loop_condition_audit, loop_forgeries_detection, loop_legal_compliance, loop_restoration_plan, loop_valuation_report, loop_market_analysis, xor_final_approval_sale_preparation, loop_client_notification])
root.order.add_edge(artifact_intake, loop_provenance_check)
root.order.add_edge(artifact_intake, loop_material_testing)
root.order.add_edge(artifact_intake, loop_historical_review)
root.order.add_edge(artifact_intake, loop_expert_interview)
root.order.add_edge(artifact_intake, loop_condition_audit)
root.order.add_edge(artifact_intake, loop_forgeries_detection)
root.order.add_edge(artifact_intake, loop_legal_compliance)
root.order.add_edge(artifact_intake, loop_restoration_plan)
root.order.add_edge(artifact_intake, loop_valuation_report)
root.order.add_edge(artifact_intake, loop_market_analysis)
root.order.add_edge(loop_provenance_check, xor_final_approval_sale_preparation)
root.order.add_edge(loop_material_testing, xor_final_approval_sale_preparation)
root.order.add_edge(loop_historical_review, xor_final_approval_sale_preparation)
root.order.add_edge(loop_expert_interview, xor_final_approval_sale_preparation)
root.order.add_edge(loop_condition_audit, xor_final_approval_sale_preparation)
root.order.add_edge(loop_forgeries_detection, xor_final_approval_sale_preparation)
root.order.add_edge(loop_legal_compliance, xor_final_approval_sale_preparation)
root.order.add_edge(loop_restoration_plan, xor_final_approval_sale_preparation)
root.order.add_edge(loop_valuation_report, xor_final_approval_sale_preparation)
root.order.add_edge(loop_market_analysis, xor_final_approval_sale_preparation)
root.order.add_edge(xor_final_approval_sale_preparation, loop_client_notification)