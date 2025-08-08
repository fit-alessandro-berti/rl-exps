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
forgery_detection = Transition(label='Forgery Detection')
legal_compliance = Transition(label='Legal Compliance')
restoration_plan = Transition(label='Restoration Plan')
valuation_report = Transition(label='Valuation Report')
market_analysis = Transition(label='Market Analysis')
final_approval = Transition(label='Final Approval')
sale_preparation = Transition(label='Sale Preparation')
client_notification = Transition(label='Client Notification')

# Define the loop for verification
verification_loop = OperatorPOWL(operator=Operator.LOOP, children=[
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
    market_analysis
])

# Define the XOR for final approval
final_approval_xor = OperatorPOWL(operator=Operator.XOR, children=[
    final_approval,
    sale_preparation,
    client_notification
])

# Define the root POWL model
root = StrictPartialOrder(nodes=[verification_loop, final_approval_xor])

# Add the dependencies
root.order.add_edge(verification_loop, final_approval_xor)

# Print the root model
print(root)