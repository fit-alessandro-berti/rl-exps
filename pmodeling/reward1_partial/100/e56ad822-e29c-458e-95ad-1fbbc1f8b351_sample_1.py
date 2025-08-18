import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions (activities)
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

# Define sub-processes
provenance_loop = OperatorPOWL(operator=Operator.LOOP, children=[Provenance_Check, skip])
context_loop = OperatorPOWL(operator=Operator.LOOP, children=[Context_Analysis, skip])
pattern_loop = OperatorPOWL(operator=Operator.LOOP, children=[AI_Pattern, skip])

# Define exclusive choice nodes
expert_choice = OperatorPOWL(operator=Operator.XOR, children=[Expert_Panel, Fraud_Detection])
legal_choice = OperatorPOWL(operator=Operator.XOR, children=[Legal_Audit, Ethics_Review])

# Define main workflow
root = StrictPartialOrder(nodes=[Submit_Artifact, Initial_Review, provenance_loop, context_loop, pattern_loop, expert_choice, legal_choice, Blockchain_Log, Certification, Owner_Notify, Archive_Data, Secure_Storage])
root.order.add_edge(Submit_Artifact, Initial_Review)
root.order.add_edge(Initial_Review, provenance_loop)
root.order.add_edge(provenance_loop, context_loop)
root.order.add_edge(context_loop, pattern_loop)
root.order.add_edge(pattern_loop, expert_choice)
root.order.add_edge(expert_choice, legal_choice)
root.order.add_edge(legal_choice, Blockchain_Log)
root.order.add_edge(Blockchain_Log, Certification)
root.order.add_edge(Certification, Owner_Notify)
root.order.add_edge(Owner_Notify, Archive_Data)
root.order.add_edge(Archive_Data, Secure_Storage)