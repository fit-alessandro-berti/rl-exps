import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define the partial order
root = StrictPartialOrder(nodes=[
    artifact_intake,
    provenance_check,
    material_testing,
    historical_review,
    expert_interview,
    condition_audit,
    digital_catalog,
    forgery_detection,
    legal_compliance,
    restoration_plan,
    valuation_report,
    market_analysis,
    final_approval,
    sale_preparation,
    client_notification
])

# Define dependencies (partial order edges)
root.order.add_edge(artifact_intake, provenance_check)
root.order.add_edge(artifact_intake, material_testing)
root.order.add_edge(artifact_intake, historical_review)
root.order.add_edge(artifact_intake, expert_interview)
root.order.add_edge(artifact_intake, condition_audit)
root.order.add_edge(artifact_intake, digital_catalog)
root.order.add_edge(artifact_intake, forgery_detection)
root.order.add_edge(artifact_intake, legal_compliance)
root.order.add_edge(artifact_intake, restoration_plan)
root.order.add_edge(artifact_intake, valuation_report)
root.order.add_edge(artifact_intake, market_analysis)
root.order.add_edge(artifact_intake, final_approval)
root.order.add_edge(artifact_intake, sale_preparation)
root.order.add_edge(artifact_intake, client_notification)

# The final POWL model is defined in the 'root' variable