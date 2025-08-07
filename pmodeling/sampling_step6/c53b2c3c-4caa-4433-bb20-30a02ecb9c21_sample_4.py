from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities (use the given names exactly)
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

# Define the partial order
root = StrictPartialOrder(nodes=[
    discover_item, document_find, initial_survey, image_capture, material_testing, style_compare, expert_consult,
    provenance_check, ownership_verify, legal_review, risk_assess, conservation_plan, certification, secure_transfer,
    dispute_resolve, final_archive
])

# Add dependencies as needed (for a full POWL model, you would need to define the 'order' attribute)
# For example, if 'discover_item' depends on 'document_find', you would add:
# root.order.add_edge(document_find, discover_item)

# The 'root' variable now contains the POWL model for the described process.