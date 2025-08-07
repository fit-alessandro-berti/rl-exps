import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
Submit_Artifact = Transition(label='Submit Artifact')
Initial_Review = Transition(label='Initial Review')
Provenance_Check = Transition(label='Provenance Check')
Material_Scan = Transition(label='Material Scan')
Context_Analysis = Transition(label='Context Analysis')
Expert_Panel = Transition(label='Expert Panel')
Digital_Fingerprint = Transition(label='Digital Fingerprint')
AI_Pattern = Transition(label='AI Pattern')
Legal_Audit = Transition(label='Legal Audit')
Ethics_Review = Transition(label='Ethics Review')
Fraud_Detection = Transition(label='Fraud Detection')
Blockchain_Log = Transition(label='Blockchain Log')
Certification = Transition(label='Certification')
Owner_Notify = Transition(label='Owner Notify')
Archive_Data = Transition(label='Archive Data')
Secure_Storage = Transition(label='Secure Storage')

# Define silent transitions
skip = SilentTransition()

# Define loops and choices
provenance_loop = OperatorPOWL(operator=Operator.LOOP, children=[Provenance_Check, skip])
material_scan_loop = OperatorPOWL(operator=Operator.LOOP, children=[Material_Scan, skip])
context_analysis_loop = OperatorPOWL(operator=Operator.LOOP, children=[Context_Analysis, skip])
expert_panel_loop = OperatorPOWL(operator=Operator.LOOP, children=[Expert_Panel, skip])
ai_pattern_loop = OperatorPOWL(operator=Operator.LOOP, children=[AI_Pattern, skip])
legal_audit_loop = OperatorPOWL(operator=Operator.LOOP, children=[Legal_Audit, skip])
ethics_review_loop = OperatorPOWL(operator=Operator.LOOP, children=[Ethics_Review, skip])
fraud_detection_loop = OperatorPOWL(operator=Operator.LOOP, children=[Fraud_Detection, skip])
blockchain_log_loop = OperatorPOWL(operator=Operator.LOOP, children=[Blockchain_Log, skip])
certification_loop = OperatorPOWL(operator=Operator.LOOP, children=[Certification, skip])
owner_notify_loop = OperatorPOWL(operator=Operator.LOOP, children=[Owner_Notify, skip])
archive_data_loop = OperatorPOWL(operator=Operator.LOOP, children=[Archive_Data, skip])
secure_storage_loop = OperatorPOWL(operator=Operator.LOOP, children=[Secure_Storage, skip])

# Define exclusive choices
provenance_choice = OperatorPOWL(operator=Operator.XOR, children=[provenance_loop, skip])
material_scan_choice = OperatorPOWL(operator=Operator.XOR, children=[material_scan_loop, skip])
context_analysis_choice = OperatorPOWL(operator=Operator.XOR, children=[context_analysis_loop, skip])
expert_panel_choice = OperatorPOWL(operator=Operator.XOR, children=[expert_panel_loop, skip])
ai_pattern_choice = OperatorPOWL(operator=Operator.XOR, children=[ai_pattern_loop, skip])
legal_audit_choice = OperatorPOWL(operator=Operator.XOR, children=[legal_audit_loop, skip])
ethics_review_choice = OperatorPOWL(operator=Operator.XOR, children=[ethics_review_loop, skip])
fraud_detection_choice = OperatorPOWL(operator=Operator.XOR, children=[fraud_detection_loop, skip])
blockchain_log_choice = OperatorPOWL(operator=Operator.XOR, children=[blockchain_log_loop, skip])
certification_choice = OperatorPOWL(operator=Operator.XOR, children=[certification_loop, skip])
owner_notify_choice = OperatorPOWL(operator=Operator.XOR, children=[owner_notify_loop, skip])
archive_data_choice = OperatorPOWL(operator=Operator.XOR, children=[archive_data_loop, skip])
secure_storage_choice = OperatorPOWL(operator=Operator.XOR, children=[secure_storage_loop, skip])

# Define the root model
root = StrictPartialOrder(nodes=[
    Submit_Artifact,
    Initial_Review,
    provenance_choice,
    material_scan_choice,
    context_analysis_choice,
    expert_panel_choice,
    ai_pattern_choice,
    legal_audit_choice,
    ethics_review_choice,
    fraud_detection_choice,
    blockchain_log_choice,
    certification_choice,
    owner_notify_choice,
    archive_data_choice,
    secure_storage_choice
])
root.order.add_edge(Submit_Artifact, Initial_Review)
root.order.add_edge(Initial_Review, provenance_choice)
root.order.add_edge(Initial_Review, material_scan_choice)
root.order.add_edge(Initial_Review, context_analysis_choice)
root.order.add_edge(Initial_Review, expert_panel_choice)
root.order.add_edge(Initial_Review, ai_pattern_choice)
root.order.add_edge(Initial_Review, legal_audit_choice)
root.order.add_edge(Initial_Review, ethics_review_choice)
root.order.add_edge(Initial_Review, fraud_detection_choice)
root.order.add_edge(Initial_Review, blockchain_log_choice)
root.order.add_edge(Initial_Review, certification_choice)
root.order.add_edge(Initial_Review, owner_notify_choice)
root.order.add_edge(Initial_Review, archive_data_choice)
root.order.add_edge(Initial_Review, secure_storage_choice)