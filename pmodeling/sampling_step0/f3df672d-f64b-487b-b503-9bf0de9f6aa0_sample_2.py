import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the POWL model
root = StrictPartialOrder()

# Define the nodes
data_collection = Transition('Data Collection')
provenance_check = Transition('Provenance Check')
material_scan = Transition('Material Scan')
historical_review = Transition('Historical Review')
expert_panel = Transition('Expert Panel')
blockchain_verify = Transition('Blockchain Verify')
oral_history = Transition('Oral History')
condition_report = Transition('Condition Report')
legal_review = Transition('Legal Review')
certification = Transition('Certification')
archival_update = Transition('Archival Update')
insurance_setup = Transition('Insurance Setup')
exhibition_prep = Transition('Exhibition Prep')
iot_monitoring = Transition('IoT Monitoring')
revalidation = Transition('Re-validation')

# Define the transitions
data_collection_to_provenance_check = OperatorPOWL(operator=OperatorPOWL.EXCLUSIVE, children=[data_collection, provenance_check])
provenance_check_to_material_scan = OperatorPOWL(operator=OperatorPOWL.EXCLUSIVE, children=[provenance_check, material_scan])
material_scan_to_historical_review = OperatorPOWL(operator=OperatorPOWL.EXCLUSIVE, children=[material_scan, historical_review])
historical_review_to_expert_panel = OperatorPOWL(operator=OperatorPOWL.EXCLUSIVE, children=[historical_review, expert_panel])
expert_panel_to_blockchain_verify = OperatorPOWL(operator=OperatorPOWL.EXCLUSIVE, children=[expert_panel, blockchain_verify])
blockchain_verify_to_oral_history = OperatorPOWL(operator=OperatorPOWL.EXCLUSIVE, children=[blockchain_verify, oral_history])
oral_history_to_condition_report = OperatorPOWL(operator=OperatorPOWL.EXCLUSIVE, children=[oral_history, condition_report])
condition_report_to_legal_review = OperatorPOWL(operator=OperatorPOWL.EXCLUSIVE, children=[condition_report, legal_review])
legal_review_to_certification = OperatorPOWL(operator=OperatorPOWL.EXCLUSIVE, children=[legal_review, certification])
certification_to_archival_update = OperatorPOWL(operator=OperatorPOWL.EXCLUSIVE, children=[certification, archival_update])
archival_update_to_insurance_setup = OperatorPOWL(operator=OperatorPOWL.EXCLUSIVE, children=[archival_update, insurance_setup])
insurance_setup_to_exhibition_prep = OperatorPOWL(operator=OperatorPOWL.EXCLUSIVE, children=[insurance_setup, exhibition_prep])
exhibition_prep_to_iot_monitoring = OperatorPOWL(operator=OperatorPOWL.EXCLUSIVE, children=[exhibition_prep, iot_monitoring])
iot_monitoring_to_revalidation = OperatorPOWL(operator=OperatorPOWL.EXCLUSIVE, children=[iot_monitoring, revalidation])

# Define the order of the nodes
root.nodes = [data_collection, provenance_check, material_scan, historical_review, expert_panel, blockchain_verify, oral_history, condition_report, legal_review, certification, archival_update, insurance_setup, exhibition_prep, iot_monitoring, revalidation]
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
root.order.add_edge(iot_monitoring, revalidation)