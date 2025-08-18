import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with their labels
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

# Define the partial order structure
root = StrictPartialOrder(nodes=[
    Asset_Intake,
    Provenance_Check,
    Material_Sampling,
    Radiocarbon_Test,
    Style_Compare,
    Historical_Search,
    Expert_Consult,
    Condition_Review,
    Scientific_Analysis,
    Data_Compilation,
    Peer_Review,
    Report_Draft,
    Certification,
    Digital_Archive,
    Client_Delivery
])

# Define the dependencies (partial order edges)
root.order.add_edge(Asset_Intake, Provenance_Check)
root.order.add_edge(Provenance_Check, Material_Sampling)
root.order.add_edge(Material_Sampling, Radiocarbon_Test)
root.order.add_edge(Radiocarbon_Test, Style_Compare)
root.order.add_edge(Style_Compare, Historical_Search)
root.order.add_edge(Historical_Search, Expert_Consult)
root.order.add_edge(Expert_Consult, Condition_Review)
root.order.add_edge(Condition_Review, Scientific_Analysis)
root.order.add_edge(Scientific_Analysis, Data_Compilation)
root.order.add_edge(Data_Compilation, Peer_Review)
root.order.add_edge(Peer_Review, Report_Draft)
root.order.add_edge(Report_Draft, Certification)
root.order.add_edge(Certification, Digital_Archive)
root.order.add_edge(Digital_Archive, Client_Delivery)

print(root)