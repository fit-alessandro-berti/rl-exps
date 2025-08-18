from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions (activities) based on the process description
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

# Create a partial order for the process
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

# Define the partial order dependencies
root.order.add_edge(provenance_check, image_capture)
root.order.add_edge(image_capture, material_scan)
root.order.add_edge(material_scan, expert_review)
root.order.add_edge(expert_review, historical_cross)
root.order.add_edge(historical_cross, legal_verify)
root.order.add_edge(legal_verify, registry_search)
root.order.add_edge(registry_search, customs_clear)
root.order.add_edge(customs_clear, condition_assess)
root.order.add_edge(condition_assess, data_log)
root.order.add_edge(data_log, chain_custody)
root.order.add_edge(chain_custody, report_draft)
root.order.add_edge(report_draft, certification)
root.order.add_edge(certification, secure_archive)
root.order.add_edge(secure_archive, auction_prep)

# Print the root POWL model
print(root)