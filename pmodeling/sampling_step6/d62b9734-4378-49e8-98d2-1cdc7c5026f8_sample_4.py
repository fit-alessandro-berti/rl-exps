import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with their labels
provenance_check = Transition(label='Provenance Check')
image_capture = Transition(label='Image Capture')
material_scan = Transition(label='Material Scan')
expert_review = Transition(label='Expert Review')
historical_cross = Transition(label='Historical Cross')
legal_verify = Transition(label='Legal Verify')
registry_search = Transition(label='Registry Search')
customs_clear = Transition(label='Customs Clear')
condition_assess = Transition(label='Condition Assess')
data_log = Transition(label='Data Log')
chain_custody = Transition(label='Chain Custody')
report_draft = Transition(label='Report Draft')
certification = Transition(label='Certification')
secure_archive = Transition(label='Secure Archive')
auction_prep = Transition(label='Auction Prep')

# Define the partial order
root = StrictPartialOrder(nodes=[
    provenance_check,
    image_capture,
    material_scan,
    expert_review,
    historical_cross,
    legal_verify,
    registry_search,
    customs_clear,
    condition_assess,
    data_log,
    chain_custody,
    report_draft,
    certification,
    secure_archive,
    auction_prep
])
# Since the process does not specify any dependencies, we don't need to add any edges here.

# The 'root' variable now contains the POWL model for the described process.