import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
activities = {
    'Data Collection': Transition(label='Data Collection'),
    'Provenance Check': Transition(label='Provenance Check'),
    'Material Scan': Transition(label='Material Scan'),
    'Historical Review': Transition(label='Historical Review'),
    'Expert Panel': Transition(label='Expert Panel'),
    'Blockchain Verify': Transition(label='Blockchain Verify'),
    'Oral History': Transition(label='Oral History'),
    'Condition Report': Transition(label='Condition Report'),
    'Legal Review': Transition(label='Legal Review'),
    'Certification': Transition(label='Certification'),
    'Archival Update': Transition(label='Archival Update'),
    'Insurance Setup': Transition(label='Insurance Setup'),
    'Exhibition Prep': Transition(label='Exhibition Prep'),
    'IoT Monitoring': Transition(label='IoT Monitoring'),
    'Re-validation': Transition(label='Re-validation')
}

# Define the transitions
data_collection = activities['Data Collection']
provenance_check = activities['Provenance Check']
material_scan = activities['Material Scan']
historical_review = activities['Historical Review']
expert_panel = activities['Expert Panel']
blockchain_verify = activities['Blockchain Verify']
oral_history = activities['Oral History']
condition_report = activities['Condition Report']
legal_review = activities['Legal Review']
certification = activities['Certification']
archival_update = activities['Archival Update']
insurance_setup = activities['Insurance Setup']
exhibition_prep = activities['Exhibition Prep']
iot_monitoring = activities['IoT Monitoring']
re_validation = activities['Re-validation']

# Define the partial order
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
    iot_monitoring,
    re_validation
])

# Define the order
root.order.add_edge(data_collection, provenance_check)
root.order.add_edge(data_collection, material_scan)
root.order.add_edge(provenance_check, historical_review)
root.order.add_edge(provenance_check, expert_panel)
root.order.add_edge(material_scan, historical_review)
root.order.add_edge(material_scan, expert_panel)
root.order.add_edge(historical_review, legal_review)
root.order.add_edge(historical_review, condition_report)
root.order.add_edge(expert_panel, legal_review)
root.order.add_edge(expert_panel, condition_report)
root.order.add_edge(condition_report, archival_update)
root.order.add_edge(condition_report, certification)
root.order.add_edge(legal_review, archival_update)
root.order.add_edge(legal_review, certification)
root.order.add_edge(archival_update, insurance_setup)
root.order.add_edge(archival_update, exhibition_prep)
root.order.add_edge(certification, insurance_setup)
root.order.add_edge(certification, exhibition_prep)
root.order.add_edge(insurance_setup, exhibition_prep)
root.order.add_edge(insurance_setup, iot_monitoring)
root.order.add_edge(exhibition_prep, iot_monitoring)
root.order.add_edge(iot_monitoring, re_validation)
root.order.add_edge(re_validation, archival_update)
root.order.add_edge(re_validation, insurance_setup)
root.order.add_edge(re_validation, exhibition_prep)
root.order.add_edge(re_validation, iot_monitoring)
root.order.add_edge(re_validation, certification)

# Print the result
print(root)