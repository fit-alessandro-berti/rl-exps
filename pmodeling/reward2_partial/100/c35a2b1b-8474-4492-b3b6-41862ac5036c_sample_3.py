import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the POWL model
root = StrictPartialOrder(nodes=[
    Initial_Inspect,
    Material_Test,
    Imaging_Scan,
    Historical_Check,
    Expert_Consult,
    Provenance_Trace,
    Forging_Detect,
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

# Define the dependencies
root.order.add_edge(Initial_Inspect, Material_Test)
root.order.add_edge(Material_Test, Imaging_Scan)
root.order.add_edge(Imaging_Scan, Historical_Check)
root.order.add_edge(Historical_Check, Expert_Consult)
root.order.add_edge(Expert_Consult, Provenance_Trace)
root.order.add_edge(Provenance_Trace, Forging_Detect)
root.order.add_edge(Forging_Detect, Restoration_Map)
root.order.add_edge(Restoration_Map, Market_Analyze)
root.order.add_edge(Market_Analyze, Auction_Review)
root.order.add_edge(Auction_Review, Value_Assess)
root.order.add_edge(Value_Assess, Report_Draft)
root.order.add_edge(Report_Draft, Board_Review)
root.order.add_edge(Board_Review, Certification)
root.order.add_edge(Certification, Release_Artifact)
root.order.add_edge(Release_Artifact, Chain_Custody)

print(root)