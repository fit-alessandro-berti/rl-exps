import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions for no actions
skip = SilentTransition()

# Define loops and choices
provenance_loop = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check, image_capture])
material_scan_loop = OperatorPOWL(operator=Operator.LOOP, children=[material_scan, expert_review])
historical_cross_loop = OperatorPOWL(operator=Operator.LOOP, children=[historical_cross, legal_verify])
registry_search_loop = OperatorPOWL(operator=Operator.LOOP, children=[registry_search, customs_clear])
condition_assess_loop = OperatorPOWL(operator=Operator.LOOP, children=[condition_assess, data_log])
chain_custody_loop = OperatorPOWL(operator=Operator.LOOP, children=[chain_custody, report_draft])
auction_prep_loop = OperatorPOWL(operator=Operator.LOOP, children=[auction_prep, secure_archive])

# Define root
root = StrictPartialOrder(nodes=[
    provenance_loop, material_scan_loop, historical_cross_loop, registry_search_loop,
    condition_assess_loop, chain_custody_loop, auction_prep_loop
])

# Define edges for the partial order
root.order.add_edge(provenance_loop, material_scan_loop)
root.order.add_edge(material_scan_loop, historical_cross_loop)
root.order.add_edge(historical_cross_loop, registry_search_loop)
root.order.add_edge(registry_search_loop, condition_assess_loop)
root.order.add_edge(condition_assess_loop, chain_custody_loop)
root.order.add_edge(chain_custody_loop, auction_prep_loop)

print(root)