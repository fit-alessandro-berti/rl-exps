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

# Define the POWL model
loop_artifact_intake = OperatorPOWL(operator=Operator.LOOP, children=[artifact_intake])
xor_provenance_check = OperatorPOWL(operator=Operator.XOR, children=[provenance_check, SilentTransition()])
xor_material_testing = OperatorPOWL(operator=Operator.XOR, children=[material_testing, SilentTransition()])
xor_historical_review = OperatorPOWL(operator=Operator.XOR, children=[historical_review, SilentTransition()])
xor_expert_interview = OperatorPOWL(operator=Operator.XOR, children=[expert_interview, SilentTransition()])
xor_condition_audit = OperatorPOWL(operator=Operator.XOR, children=[condition_audit, SilentTransition()])
xor_digital_catalog = OperatorPOWL(operator=Operator.XOR, children=[digital_catalog, SilentTransition()])
xor_forgery_detection = OperatorPOWL(operator=Operator.XOR, children=[forgery_detection, SilentTransition()])
xor_legal_compliance = OperatorPOWL(operator=Operator.XOR, children=[legal_compliance, SilentTransition()])
xor_restoration_plan = OperatorPOWL(operator=Operator.XOR, children=[restoration_plan, SilentTransition()])
xor_valuation_report = OperatorPOWL(operator=Operator.XOR, children=[valuation_report, SilentTransition()])
xor_market_analysis = OperatorPOWL(operator=Operator.XOR, children=[market_analysis, SilentTransition()])
xor_final_approval = OperatorPOWL(operator=Operator.XOR, children=[final_approval, SilentTransition()])
xor_sale_preparation = OperatorPOWL(operator=Operator.XOR, children=[sale_preparation, SilentTransition()])
xor_client_notification = OperatorPOWL(operator=Operator.XOR, children=[client_notification, SilentTransition()])

root = StrictPartialOrder(nodes=[
    loop_artifact_intake,
    xor_provenance_check,
    xor_material_testing,
    xor_historical_review,
    xor_expert_interview,
    xor_condition_audit,
    xor_digital_catalog,
    xor_forgery_detection,
    xor_legal_compliance,
    xor_restoration_plan,
    xor_valuation_report,
    xor_market_analysis,
    xor_final_approval,
    xor_sale_preparation,
    xor_client_notification
])
root.order.add_edge(loop_artifact_intake, xor_provenance_check)
root.order.add_edge(loop_artifact_intake, xor_material_testing)
root.order.add_edge(loop_artifact_intake, xor_historical_review)
root.order.add_edge(loop_artifact_intake, xor_expert_interview)
root.order.add_edge(loop_artifact_intake, xor_condition_audit)
root.order.add_edge(loop_artifact_intake, xor_digital_catalog)
root.order.add_edge(loop_artifact_intake, xor_forgery_detection)
root.order.add_edge(loop_artifact_intake, xor_legal_compliance)
root.order.add_edge(loop_artifact_intake, xor_restoration_plan)
root.order.add_edge(loop_artifact_intake, xor_valuation_report)
root.order.add_edge(loop_artifact_intake, xor_market_analysis)
root.order.add_edge(loop_artifact_intake, xor_final_approval)
root.order.add_edge(loop_artifact_intake, xor_sale_preparation)
root.order.add_edge(loop_artifact_intake, xor_client_notification)