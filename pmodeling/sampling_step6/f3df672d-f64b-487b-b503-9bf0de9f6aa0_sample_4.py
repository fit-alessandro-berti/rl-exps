import pm4py
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

# Define the root partial order
root = StrictPartialOrder(nodes=[data_collection, provenance_check, material_scan, historical_review, expert_panel, blockchain_verify, oral_history, condition_report, legal_review, certification, archival_update, insurance_setup, exhibition_prep, iot_monitoring, re_validation])

# Define the dependencies between activities (for a partial order model)
root.order.add_edge(data_collection, provenance_check)
root.order.add_edge(data_collection, material_scan)
root.order.add_edge(data_collection, historical_review)
root.order.add_edge(data_collection, expert_panel)
root.order.add_edge(data_collection, blockchain_verify)
root.order.add_edge(data_collection, oral_history)
root.order.add_edge(data_collection, condition_report)
root.order.add_edge(data_collection, legal_review)
root.order.add_edge(data_collection, certification)
root.order.add_edge(data_collection, archival_update)
root.order.add_edge(data_collection, insurance_setup)
root.order.add_edge(data_collection, exhibition_prep)
root.order.add_edge(data_collection, iot_monitoring)
root.order.add_edge(data_collection, re_validation)

# Save the root partial order model in the variable 'root'
print(root)