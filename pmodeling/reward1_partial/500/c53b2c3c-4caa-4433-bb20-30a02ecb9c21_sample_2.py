import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the silent transition for the loop
skip = SilentTransition()

# Define the partial order
root = StrictPartialOrder(
    nodes=[
        discover_item,
        document_find,
        initial_survey,
        image_capture,
        material_testing,
        style_compare,
        expert_consult,
        provenance_check,
        ownership_verify,
        legal_review,
        risk_assess,
        conservation_plan,
        certification,
        secure_transfer,
        dispute_resolve,
        final_archive
    ],
    order={
        discover_item: [document_find],
        document_find: [initial_survey],
        initial_survey: [image_capture, material_testing],
        image_capture: [style_compare],
        material_testing: [style_compare],
        style_compare: [expert_consult, provenance_check, ownership_verify],
        expert_consult: [risk_assess],
        provenance_check: [risk_assess],
        ownership_verify: [risk_assess],
        risk_assess: [conservation_plan],
        conservation_plan: [certification],
        certification: [secure_transfer, dispute_resolve],
        secure_transfer: [final_archive],
        dispute_resolve: [final_archive]
    }
)

# Add the dependencies
root.order.add_edge(discover_item, document_find)
root.order.add_edge(document_find, initial_survey)
root.order.add_edge(initial_survey, image_capture)
root.order.add_edge(initial_survey, material_testing)
root.order.add_edge(image_capture, style_compare)
root.order.add_edge(material_testing, style_compare)
root.order.add_edge(style_compare, expert_consult)
root.order.add_edge(style_compare, provenance_check)
root.order.add_edge(style_compare, ownership_verify)
root.order.add_edge(expert_consult, risk_assess)
root.order.add_edge(provenance_check, risk_assess)
root.order.add_edge(ownership_verify, risk_assess)
root.order.add_edge(risk_assess, conservation_plan)
root.order.add_edge(conservation_plan, certification)
root.order.add_edge(certification, secure_transfer)
root.order.add_edge(certification, dispute_resolve)
root.order.add_edge(secure_transfer, final_archive)
root.order.add_edge(dispute_resolve, final_archive)

# Print the root
print(root)