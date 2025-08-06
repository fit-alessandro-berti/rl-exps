import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
Provenance_Check = Transition(label='Provenance Check')
Image_Capture = Transition(label='Image Capture')
Material_Scan = Transition(label='Material Scan')
Expert_Review = Transition(label='Expert Review')
Historical_Cross = Transition(label='Historical Cross')
Legal_Verify = Transition(label='Legal Verify')
Registry_Search = Transition(label='Registry Search')
Customs_Clear = Transition(label='Customs Clear')
Condition_Assess = Transition(label='Condition Assess')
Data_Log = Transition(label='Data Log')
Chain_Custody = Transition(label='Chain Custody')
Report_Draft = Transition(label='Report Draft')
Certification = Transition(label='Certification')
Secure_Archive = Transition(label='Secure Archive')
Auction_Prep = Transition(label='Auction Prep')

# Define the partial order
root = StrictPartialOrder(nodes=[
    Provenance_Check, Image_Capture, Material_Scan, Expert_Review, Historical_Cross,
    Legal_Verify, Registry_Search, Customs_Clear, Condition_Assess, Data_Log,
    Chain_Custody, Report_Draft, Certification, Secure_Archive, Auction_Prep
])

# Define the dependencies
root.order.add_edge(Provenance_Check, Image_Capture)
root.order.add_edge(Image_Capture, Material_Scan)
root.order.add_edge(Material_Scan, Expert_Review)
root.order.add_edge(Expert_Review, Historical_Cross)
root.order.add_edge(Historical_Cross, Legal_Verify)
root.order.add_edge(Legal_Verify, Registry_Search)
root.order.add_edge(Registry_Search, Customs_Clear)
root.order.add_edge(Customs_Clear, Condition_Assess)
root.order.add_edge(Condition_Assess, Data_Log)
root.order.add_edge(Data_Log, Chain_Custody)
root.order.add_edge(Chain_Custody, Report_Draft)
root.order.add_edge(Report_Draft, Certification)
root.order.add_edge(Certification, Secure_Archive)
root.order.add_edge(Secure_Archive, Auction_Prep)

# Print the final result
print(root)