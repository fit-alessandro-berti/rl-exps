import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
data_collection       = Transition(label='Data Collection')
provenance_check      = Transition(label='Provenance Check')
material_scan         = Transition(label='Material Scan')
historical_review     = Transition(label='Historical Review')
expert_panel          = Transition(label='Expert Panel')
blockchain_verify     = Transition(label='Blockchain Verify')
oral_history          = Transition(label='Oral History')
condition_report      = Transition(label='Condition Report')
legal_review          = Transition(label='Legal Review')
certification         = Transition(label='Certification')
archival_update       = Transition(label='Archival Update')
insurance_setup       = Transition(label='Insurance Setup')
exhibition_prep       = Transition(label='Exhibition Prep')
iot_monitoring        = Transition(label='IoT Monitoring')
re_validation         = Transition(label='Re-validation')

# Loop for continuous IoT monitoring and re-validation
monitoring_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[iot_monitoring, re_validation]
)

# Build the partial order
root = StrictPartialOrder(nodes=[
    data_collection,
    provenance_check,
    material_scan,
    historical_review,
    expert_panel,
    blockchain_verify,
    oral_history,
    condition_report,
    legal_review,
    certification,
    archival_update,
    insurance_setup,
    exhibition_prep,
    monitoring_loop
])

# Define the control-flow dependencies
root.order.add_edge(data_collection, provenance_check)
root.order.add_edge(provenance_check, material_scan)
root.order.add_edge(provenance_check, historical_review)
root.order.add_edge(material_scan, condition_report)
root.order.add_edge(historical_review, condition_report)
root.order.add_edge(condition_report, expert_panel)
root.order.add_edge(condition_report, blockchain_verify)
root.order.add_edge(condition_report, oral_history)
root.order.add_edge(blockchain_verify, certification)
root.order.add_edge(oral_history, certification)
root.order.add_edge(certification, legal_review)
root.order.add_edge(legal_review, archival_update)
root.order.add_edge(archival_update, insurance_setup)
root.order.add_edge(insurance_setup, exhibition_prep)
root.order.add_edge(insurance_setup, monitoring_loop)

print(root)