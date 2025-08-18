import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define activities
discover_item = Transition(label='Discover Item')
document_find = Transition(label='Document Find')
initial_survey = Transition(label='Initial Survey')
image_capture = Transition(label='Image Capture')
material_testing = Transition(label='Material Testing')
style_compare = Transition(label='Style Compare')
expert_consult = Transition(label='Expert Consult')
provenance_check = Transition(label='Provenance Check')
ownership_verify = Transition(label='Ownership Verify')
legal_review = Transition(label='Legal Review')
risk_assess = Transition(label='Risk Assess')
conservation_plan = Transition(label='Conservation Plan')
certification = Transition(label='Certification')
secure_transfer = Transition(label='Secure Transfer')
dispute_resolve = Transition(label='Dispute Resolve')
final_archive = Transition(label='Final Archive')

# Define silent transitions
skip = SilentTransition()

# Define sub-processes
# Image Capture and Material Testing can be combined
image_material = OperatorPOWL(operator=Operator.XOR, children=[image_capture, material_testing])

# Expert Consult and Provenance Check can be combined
expert_provenance = OperatorPOWL(operator=Operator.XOR, children=[expert_consult, provenance_check])

# Ownership Verify and Legal Review can be combined
ownership_legal = OperatorPOWL(operator=Operator.XOR, children=[ownership_verify, legal_review])

# Risk Assess and Conservation Plan can be combined
risk_conservation = OperatorPOWL(operator=Operator.XOR, children=[risk_assess, conservation_plan])

# Certification and Secure Transfer can be combined
certification_secure = OperatorPOWL(operator=Operator.XOR, children=[certification, secure_transfer])

# Dispute Resolve and Final Archive can be combined
dispute_archive = OperatorPOWL(operator=Operator.XOR, children=[dispute_resolve, final_archive])

# Define loops and choices
# Loop for Risk Assess and Conservation Plan
risk_conservation_loop = OperatorPOWL(operator=Operator.LOOP, children=[risk_assess, conservation_plan])

# Loop for Ownership Verify and Legal Review
ownership_legal_loop = OperatorPOWL(operator=Operator.LOOP, children=[ownership_verify, legal_review])

# Loop for Expert Consult and Provenance Check
expert_provenance_loop = OperatorPOWL(operator=Operator.LOOP, children=[expert_consult, provenance_check])

# Loop for Image Capture and Material Testing
image_material_loop = OperatorPOWL(operator=Operator.LOOP, children=[image_capture, material_testing])

# Loop for Discover Item and Document Find
discover_document_loop = OperatorPOWL(operator=Operator.LOOP, children=[discover_item, document_find])

# Loop for Initial Survey
initial_survey_loop = OperatorPOWL(operator=Operator.LOOP, children=[initial_survey])

# Define the root POWL model
root = StrictPartialOrder(nodes=[
    discover_document_loop,
    initial_survey_loop,
    image_material_loop,
    expert_provenance_loop,
    risk_conservation_loop,
    ownership_legal_loop,
    risk_conservation,
    ownership_legal,
    image_material,
    expert_provenance,
    risk_assess,
    conservation_plan,
    ownership_verify,
    legal_review,
    dispute_resolve,
    final_archive
])

# Add edges between nodes
root.order.add_edge(discover_document_loop, initial_survey_loop)
root.order.add_edge(initial_survey_loop, image_material_loop)
root.order.add_edge(image_material_loop, expert_provenance_loop)
root.order.add_edge(expert_provenance_loop, risk_conservation_loop)
root.order.add_edge(risk_conservation_loop, ownership_legal_loop)
root.order.add_edge(ownership_legal_loop, risk_conservation)
root.order.add_edge(risk_conservation, ownership_legal)
root.order.add_edge(image_material, expert_provenance)
root.order.add_edge(expert_provenance, risk_assess)
root.order.add_edge(risk_assess, conservation_plan)
root.order.add_edge(conservation_plan, ownership_verify)
root.order.add_edge(ownership_verify, legal_review)
root.order.add_edge(legal_review, dispute_resolve)
root.order.add_edge(dispute_resolve, final_archive)