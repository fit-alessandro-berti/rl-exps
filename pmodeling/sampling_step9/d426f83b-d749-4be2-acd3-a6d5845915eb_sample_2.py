import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
Asset_Intake = Transition(label='Asset Intake')
Provenance_Check = Transition(label='Provenance Check')
Material_Sampling = Transition(label='Material Sampling')
Radiocarbon_Test = Transition(label='Radiocarbon Test')
Style_Compare = Transition(label='Style Compare')
Historical_Search = Transition(label='Historical Search')
Expert_Consult = Transition(label='Expert Consult')
Condition_Review = Transition(label='Condition Review')
Scientific_Analysis = Transition(label='Scientific Analysis')
Data_Compilation = Transition(label='Data Compilation')
Peer_Review = Transition(label='Peer Review')
Report_Draft = Transition(label='Report Draft')
Certification = Transition(label='Certification')
Digital_Archive = Transition(label='Digital Archive')
Client_Delivery = Transition(label='Client Delivery')
skip = SilentTransition()
loop = OperatorPOWL(operator=Operator.LOOP, children=[Asset_Intake, Provenance_Check, Material_Sampling, Radiocarbon_Test, Style_Compare, Historical_Search, Expert_Consult, Condition_Review, Scientific_Analysis, Data_Compilation])
xor = OperatorPOWL(operator=Operator.XOR, children=[Certification, skip])
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)