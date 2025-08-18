import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

loop1 = OperatorPOWL(operator=Operator.LOOP, children=[data_collection, provenance_check])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[material_scan, historical_review])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[expert_panel, blockchain_verify])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[oral_history, condition_report])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[legal_review, certification])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[archival_update, insurance_setup])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[exhibition_prep, iot_monitoring])

root = StrictPartialOrder(nodes=[loop1, xor1, xor2, xor3, xor4, xor5, xor6])
root.order.add_edge(loop1, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, loop1)

root