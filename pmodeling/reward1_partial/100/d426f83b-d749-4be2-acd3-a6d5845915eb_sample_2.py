import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
intake = Transition(label='Asset Intake')
check = Transition(label='Provenance Check')
sampling = Transition(label='Material Sampling')
radiocarbon = Transition(label='Radiocarbon Test')
style_compare = Transition(label='Style Compare')
historical = Transition(label='Historical Search')
consult = Transition(label='Expert Consult')
review = Transition(label='Condition Review')
analysis = Transition(label='Scientific Analysis')
compile = Transition(label='Data Compilation')
peer_review = Transition(label='Peer Review')
draft = Transition(label='Report Draft')
certify = Transition(label='Certification')
archive = Transition(label='Digital Archive')
delivery = Transition(label='Client Delivery')

# Define silent transitions
skip = SilentTransition()

# Define the process using Partial Order
root = StrictPartialOrder(
    nodes=[
        intake,
        check,
        sampling,
        radiocarbon,
        style_compare,
        historical,
        consult,
        review,
        analysis,
        compile,
        peer_review,
        draft,
        certify,
        archive,
        delivery
    ],
    order=[
        (intake, check),
        (intake, sampling),
        (check, historical),
        (check, consult),
        (sampling, analysis),
        (sampling, style_compare),
        (consult, review),
        (review, compile),
        (compile, peer_review),
        (peer_review, draft),
        (draft, certify),
        (certify, archive),
        (archive, delivery)
    ]
)

# Print the root to confirm
print(root)