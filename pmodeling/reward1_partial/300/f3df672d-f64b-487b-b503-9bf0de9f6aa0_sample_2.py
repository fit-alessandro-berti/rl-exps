import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model for the process
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

# Define the POWL operators
xor = OperatorPOWL(operator=Operator.XOR, children=[blockchain_verify, oral_history])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[legal_review, archival_update])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[certification, insurance_setup])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[exhibition_prep, iot_monitoring])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[re_validation, data_collection])

# Define the StrictPartialOrder model
root = StrictPartialOrder(nodes=[data_collection, provenance_check, material_scan, historical_review, expert_panel, xor, xor2, xor3, xor4, xor5])
root.order.add_edge(data_collection, provenance_check)
root.order.add_edge(provenance_check, material_scan)
root.order.add_edge(material_scan, historical_review)
root.order.add_edge(historical_review, expert_panel)
root.order.add_edge(expert_panel, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, data_collection)

# Print the final POWL model
print(root)