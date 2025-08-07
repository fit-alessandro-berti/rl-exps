import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
data_collection      = Transition(label='Data Collection')
provenance_check     = Transition(label='Provenance Check')
material_scan        = Transition(label='Material Scan')
historical_review    = Transition(label='Historical Review')
expert_panel         = Transition(label='Expert Panel')
blockchain_verify    = Transition(label='Blockchain Verify')
oral_history         = Transition(label='Oral History')
condition_report     = Transition(label='Condition Report')
legal_review         = Transition(label='Legal Review')
certification        = Transition(label='Certification')
archival_update      = Transition(label='Archival Update')
insurance_setup      = Transition(label='Insurance Setup')
exhibition_prep      = Transition(label='Exhibition Prep')
iot_monitoring       = Transition(label='IoT Monitoring')
re_validation        = Transition(label='Re-validation')

# Build the monitoring loop: IoT Monitoring -> Re-validation -> IoT Monitoring ...
monitoring_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[iot_monitoring, re_validation]
)

# Assemble the overall partial order
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

# Add the control-flow dependencies
root.order.add_edge(data_collection, provenance_check)
root.order.add_edge(data_collection, material_scan)
root.order.add_edge(provenance_check, archival_update)
root.order.add_edge(material_scan, archival_update)
root.order.add_edge(provenance_check, expert_panel)
root.order.add_edge(material_scan, expert_panel)
root.order.add_edge(expert_panel, certification)
root.order.add_edge(certification, archival_update)
root.order.add_edge(certification, legal_review)
root.order.add_edge(legal_review, archival_update)
root.order.add_edge(oral_history, archival_update)
root.order.add_edge(condition_report, archival_update)
root.order.add_edge(blockchain_verify, archival_update)
root.order.add_edge(archival_update, insurance_setup)
root.order.add_edge(archival_update, exhibition_prep)
root.order.add_edge(archival_update, monitoring_loop)
root.order.add_edge(legal_review, insurance_setup)
root.order.add_edge(legal_review, exhibition_prep)
root.order.add_edge(legal_review, monitoring_loop)
root.order.add_edge(archival_update, legal_review)
root.order.add_edge(archival_update, insurance_setup)
root.order.add_edge(archival_update, exhibition_prep)
root.order.add_edge(archival_update, monitoring_loop)