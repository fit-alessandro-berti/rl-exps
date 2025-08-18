from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the transitions (activities) for the POWL model
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

# Define the silent transition for the POWL model
skip = SilentTransition()

# Define the POWL model
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
    order=[
        (discover_item, document_find),
        (document_find, initial_survey),
        (initial_survey, image_capture),
        (image_capture, material_testing),
        (material_testing, style_compare),
        (style_compare, expert_consult),
        (expert_consult, provenance_check),
        (provenance_check, ownership_verify),
        (ownership_verify, legal_review),
        (legal_review, risk_assess),
        (risk_assess, conservation_plan),
        (conservation_plan, certification),
        (certification, secure_transfer),
        (secure_transfer, dispute_resolve),
        (dispute_resolve, final_archive)
    ]
)

print(root)