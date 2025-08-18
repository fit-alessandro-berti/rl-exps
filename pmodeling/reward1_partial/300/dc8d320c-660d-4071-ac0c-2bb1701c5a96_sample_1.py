import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
intake = Transition(label='Artifact Intake')
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

# Define exclusive choice (XOR) for verification steps
verification_steps = OperatorPOWL(operator=Operator.XOR, children=[
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

# Define loop for verification steps
verification_loop = OperatorPOWL(operator=Operator.LOOP, children=[
    verification_steps
])

# Define final approval and sale preparation
final_approval_loop = OperatorPOWL(operator=Operator.LOOP, children=[
    final_approval,
    sale_preparation
])

# Define the root node of the POWL model
root = StrictPartialOrder(nodes=[verification_loop, final_approval_loop])
root.order.add_edge(verification_loop, final_approval_loop)

# Print the root node to verify the model
print(root)