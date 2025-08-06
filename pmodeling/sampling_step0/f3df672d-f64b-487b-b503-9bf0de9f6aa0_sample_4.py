from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
data_collection = Transition(label='Data Collection')
provenance_check = Transition(label='Provenance Check')
material_scan = Transition(label='Material Scan')
historical_review = Transition(label='Historical Review')
expert_panel = Transition(label='Expert Panel')
blockchain_verify = Transition(label='Blockchain Verify')
oral_history = Transition(label='Oral History')
condition_report = Transition(label='Condition Report')
legal_review = Transition(label='Legal Review')
certification = Transition(label='Certification')
archival_update = Transition(label='Archival Update')
insurance_setup = Transition(label='Insurance Setup')
exhibition_prep = Transition(label='Exhibition Prep')
iot_monitoring = Transition(label='IoT Monitoring')
re_validation = Transition(label='Re-validation')

# Define silent transitions
skip = SilentTransition()

# Define partial order
root = StrictPartialOrder()

# Add transitions to the partial order
root.nodes.append(data_collection)
root.nodes.append(provenance_check)
root.nodes.append(material_scan)
root.nodes.append(historical_review)
root.nodes.append(expert_panel)
root.nodes.append(blockchain_verify)
root.nodes.append(oral_history)
root.nodes.append(condition_report)
root.nodes.append(legal_review)
root.nodes.append(certification)
root.nodes.append(archival_update)
root.nodes.append(insurance_setup)
root.nodes.append(exhibition_prep)
root.nodes.append(iot_monitoring)
root.nodes.append(re_validation)

# Define dependencies
root.order.add_edge(data_collection, provenance_check)
root.order.add_edge(provenance_check, material_scan)
root.order.add_edge(material_scan, historical_review)
root.order.add_edge(historical_review, expert_panel)
root.order.add_edge(expert_panel, blockchain_verify)
root.order.add_edge(blockchain_verify, oral_history)
root.order.add_edge(oral_history, condition_report)
root.order.add_edge(condition_report, legal_review)
root.order.add_edge(legal_review, certification)
root.order.add_edge(certification, archival_update)
root.order.add_edge(archival_update, insurance_setup)
root.order.add_edge(insurance_setup, exhibition_prep)
root.order.add_edge(exhibition_prep, iot_monitoring)
root.order.add_edge(iot_monitoring, re_validation)

# Print the final result
print(root)