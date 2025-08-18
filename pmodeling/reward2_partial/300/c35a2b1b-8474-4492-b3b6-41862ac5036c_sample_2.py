from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
Initial_Inspect = Transition(label='Initial Inspect')
Material_Test = Transition(label='Material Test')
Imaging_Scan = Transition(label='Imaging Scan')
Historical_Check = Transition(label='Historical Check')
Expert_Consult = Transition(label='Expert Consult')
Provenance_Trace = Transition(label='Provenance Trace')
Forgery_Detect = Transition(label='Forgery Detect')
Restoration_Map = Transition(label='Restoration Map')
Market_Analyze = Transition(label='Market Analyze')
Auction_Review = Transition(label='Auction Review')
Value_Assess = Transition(label='Value Assess')
Report_Draft = Transition(label='Report Draft')
Board_Review = Transition(label='Board Review')
Certification = Transition(label='Certification')
Release_Artifact = Transition(label='Release Artifact')
Chain_Custody = Transition(label='Chain Custody')

# Define the POWL model structure
root = StrictPartialOrder(nodes=[
    Initial_Inspect, 
    Material_Test, 
    Imaging_Scan, 
    Historical_Check, 
    Expert_Consult, 
    Provenance_Trace, 
    Forgery_Detect, 
    Restoration_Map, 
    Market_Analyze, 
    Auction_Review, 
    Value_Assess, 
    Report_Draft, 
    Board_Review, 
    Certification, 
    Release_Artifact, 
    Chain_Custody
])

# Define the partial order dependencies
root.order.add_edge(Initial_Inspect, Material_Test)
root.order.add_edge(Initial_Inspect, Imaging_Scan)
root.order.add_edge(Material_Test, Historical_Check)
root.order.add_edge(Material_Test, Expert_Consult)
root.order.add_edge(Imaging_Scan, Provenance_Trace)
root.order.add_edge(Imaging_Scan, Forgery_Detect)
root.order.add_edge(Provenance_Trace, Restoration_Map)
root.order.add_edge(Provenance_Trace, Market_Analyze)
root.order.add_edge(Market_Analyze, Auction_Review)
root.order.add_edge(Auction_Review, Value_Assess)
root.order.add_edge(Value_Assess, Report_Draft)
root.order.add_edge(Report_Draft, Board_Review)
root.order.add_edge(Board_Review, Certification)
root.order.add_edge(Certification, Release_Artifact)
root.order.add_edge(Release_Artifact, Chain_Custody)

# Print the root model
print(root)