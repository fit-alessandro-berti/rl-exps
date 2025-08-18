import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

# Define the POWL operators
xor_provenance = OperatorPOWL(operator=Operator.XOR, children=[provenance_check, SilentTransition()])
xor_image = OperatorPOWL(operator=Operator.XOR, children=[image_capture, SilentTransition()])
xor_material = OperatorPOWL(operator=Operator.XOR, children=[material_scan, SilentTransition()])
xor_expert = OperatorPOWL(operator=Operator.XOR, children=[expert_review, SilentTransition()])
xor_historical = OperatorPOWL(operator=Operator.XOR, children=[historical_cross, SilentTransition()])
xor_legal = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, SilentTransition()])
xor_registry = OperatorPOWL(operator=Operator.XOR, children=[registry_search, SilentTransition()])
xor_customs = OperatorPOWL(operator=Operator.XOR, children=[customs_clear, SilentTransition()])
xor_condition = OperatorPOWL(operator=Operator.XOR, children=[condition_assess, SilentTransition()])
xor_data_log = OperatorPOWL(operator=Operator.XOR, children=[data_log, SilentTransition()])
xor_chain_custody = OperatorPOWL(operator=Operator.XOR, children=[chain_custody, SilentTransition()])
xor_report = OperatorPOWL(operator=Operator.XOR, children=[report_draft, SilentTransition()])
xor_certification = OperatorPOWL(operator=Operator.XOR, children=[certification, SilentTransition()])
xor_archive = OperatorPOWL(operator=Operator.XOR, children=[secure_archive, SilentTransition()])
xor_auction = OperatorPOWL(operator=Operator.XOR, children=[auction_prep, SilentTransition()])

# Define the partial order
root = StrictPartialOrder(nodes=[
    xor_provenance,
    xor_image,
    xor_material,
    xor_expert,
    xor_historical,
    xor_legal,
    xor_registry,
    xor_customs,
    xor_condition,
    xor_data_log,
    xor_chain_custody,
    xor_report,
    xor_certification,
    xor_archive,
    xor_auction
])

# Define the order relationships
root.order.add_edge(xor_provenance, xor_image)
root.order.add_edge(xor_image, xor_material)
root.order.add_edge(xor_material, xor_expert)
root.order.add_edge(xor_expert, xor_historical)
root.order.add_edge(xor_historical, xor_legal)
root.order.add_edge(xor_legal, xor_registry)
root.order.add_edge(xor_registry, xor_customs)
root.order.add_edge(xor_customs, xor_condition)
root.order.add_edge(xor_condition, xor_data_log)
root.order.add_edge(xor_data_log, xor_chain_custody)
root.order.add_edge(xor_chain_custody, xor_report)
root.order.add_edge(xor_report, xor_certification)
root.order.add_edge(xor_certification, xor_archive)
root.order.add_edge(xor_archive, xor_auction)

print(root)