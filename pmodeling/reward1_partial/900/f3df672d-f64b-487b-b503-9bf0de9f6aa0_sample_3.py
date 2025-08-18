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

# Define the process model
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[data_collection, provenance_check, material_scan])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[historical_review, expert_panel, blockchain_verify, oral_history, condition_report])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[legal_review, certification, archival_update, insurance_setup, exhibition_prep])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[iot_monitoring, revalidation])

# Create the root process
root = StrictPartialOrder(nodes=[loop1, loop2, loop3, loop4])
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, loop4)

print(root)