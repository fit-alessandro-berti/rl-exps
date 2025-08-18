import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
Initial_Review = Transition(label='Initial Review')
Provenance_Check = Transition(label='Provenance Check')
Material_Scan = Transition(label='Material Scan')
Chemical_Test = Transition(label='Chemical Test')
Imaging_Capture = Transition(label='Imaging Capture')
Expert_Consult = Transition(label='Expert Consult')
Historical_Match = Transition(label='Historical Match')
Forgery_Detect = Transition(label='Forgery Detect')
Documentation_Verify = Transition(label='Documentation Verify')
Cross_Border_Check = Transition(label='Cross-Border Check')
Condition_Assess = Transition(label='Condition Assess')
Value_Estimate = Transition(label='Value Estimate')
Report_Draft = Transition(label='Report Draft')
Report_Review = Transition(label='Report Review')
Client_Approval = Transition(label='Client Approval')
Certification_Issue = Transition(label='Certification Issue')
Archive_Record = Transition(label='Archive Record')

# Define the POWL model
root = StrictPartialOrder(nodes=[
    Initial_Review, Provenance_Check, Material_Scan, Chemical_Test, Imaging_Capture,
    Expert_Consult, Historical_Match, Forgery_Detect, Documentation_Verify, Cross_Border_Check,
    Condition_Assess, Value_Estimate, Report_Draft, Report_Review, Client_Approval, Certification_Issue,
    Archive_Record
])

# Define the dependencies
root.order.add_edge(Initial_Review, Provenance_Check)
root.order.add_edge(Initial_Review, Material_Scan)
root.order.add_edge(Provenance_Check, Chemical_Test)
root.order.add_edge(Provenance_Check, Imaging_Capture)
root.order.add_edge(Chemical_Test, Expert_Consult)
root.order.add_edge(Imaging_Capture, Historical_Match)
root.order.add_edge(Expert_Consult, Forgery_Detect)
root.order.add_edge(Historical_Match, Documentation_Verify)
root.order.add_edge(Documentation_Verify, Cross_Border_Check)
root.order.add_edge(Cross_Border_Check, Condition_Assess)
root.order.add_edge(Condition_Assess, Value_Estimate)
root.order.add_edge(Value_Estimate, Report_Draft)
root.order.add_edge(Report_Draft, Report_Review)
root.order.add_edge(Report_Review, Client_Approval)
root.order.add_edge(Client_Approval, Certification_Issue)
root.order.add_edge(Certification_Issue, Archive_Record)

print(root)