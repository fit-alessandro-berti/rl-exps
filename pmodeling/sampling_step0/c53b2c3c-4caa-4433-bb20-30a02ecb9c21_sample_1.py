import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model for the process
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

skip = SilentTransition()

# Define the partial order for the process
partial_order = StrictPartialOrder(
    nodes=[discover_item, document_find, initial_survey, image_capture, material_testing, style_compare, expert_consult,
           provenance_check, ownership_verify, legal_review, risk_assess, conservation_plan, certification, secure_transfer,
           dispute_resolve, final_archive],
    order={
        (discover_item, document_find): 0,
        (discover_item, initial_survey): 0,
        (document_find, image_capture): 0,
        (document_find, material_testing): 0,
        (initial_survey, image_capture): 0,
        (initial_survey, material_testing): 0,
        (image_capture, style_compare): 0,
        (image_capture, expert_consult): 0,
        (material_testing, style_compare): 0,
        (material_testing, expert_consult): 0,
        (style_compare, provenance_check): 0,
        (style_compare, ownership_verify): 0,
        (expert_consult, provenance_check): 0,
        (expert_consult, ownership_verify): 0,
        (provenance_check, legal_review): 0,
        (ownership_verify, legal_review): 0,
        (legal_review, risk_assess): 0,
        (risk_assess, conservation_plan): 0,
        (conservation_plan, certification): 0,
        (certification, secure_transfer): 0,
        (secure_transfer, dispute_resolve): 0,
        (dispute_resolve, final_archive): 0
    }
)

# Define the exclusive choice for the process
exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[dispute_resolve, final_archive])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[partial_order, exclusive_choice])
root.order.add_edge(partial_order, exclusive_choice)

print(root)