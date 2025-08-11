import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
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
revalidation = Transition(label='Re-validation')

# Define silent transitions
skip = SilentTransition()

# Define the loop nodes
material_scan_loop = OperatorPOWL(operator=Operator.LOOP, children=[material_scan, skip])
expert_panel_loop = OperatorPOWL(operator=Operator.LOOP, children=[expert_panel, skip])

# Define the XOR nodes
orality_xor = OperatorPOWL(operator=Operator.XOR, children=[oral_history, skip])
legal_xor = OperatorPOWL(operator=Operator.XOR, children=[legal_review, skip])

# Define the POWL model
root = StrictPartialOrder(nodes=[data_collection, provenance_check, material_scan_loop, expert_panel_loop, orality_xor, legal_xor, condition_report, archival_update, insurance_setup, exhibition_prep, iot_monitoring, revalidation])
root.order.add_edge(data_collection, provenance_check)
root.order.add_edge(provenance_check, material_scan_loop)
root.order.add_edge(material_scan_loop, expert_panel_loop)
root.order.add_edge(expert_panel_loop, orality_xor)
root.order.add_edge(orality_xor, legal_xor)
root.order.add_edge(legal_xor, condition_report)
root.order.add_edge(condition_report, archival_update)
root.order.add_edge(archival_update, insurance_setup)
root.order.add_edge(insurance_setup, exhibition_prep)
root.order.add_edge(exhibition_prep, iot_monitoring)
root.order.add_edge(iot_monitoring, revalidation)
root.order.add_edge(revalidation, data_collection)