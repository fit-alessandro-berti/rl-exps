import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) as POWL nodes
Intake_Document = Transition(label='Intake Document')
Visual_Inspect = Transition(label='Visual Inspect')
Imaging_Scan = Transition(label='Imaging Scan')
Material_Test = Transition(label='Material Test')
Database_Cross = Transition(label='Database Cross')
Provenance_Check = Transition(label='Provenance Check')
Expert_Consult = Transition(label='Expert Consult')
Carbon_Dating = Transition(label='Carbon Dating')
Forensic_Analyze = Transition(label='Forensic Analyze')
Anomaly_Review = Transition(label='Anomaly Review')
Risk_Assess = Transition(label='Risk Assess')
Report_Draft = Transition(label='Report Draft')
Insurance_Quote = Transition(label='Insurance Quote')
Storage_Plan = Transition(label='Storage Plan')
Final_Approval = Transition(label='Final Approval')

# Define the partial order
root = StrictPartialOrder(nodes=[
    Intake_Document, 
    Visual_Inspect, 
    Imaging_Scan, 
    Material_Test, 
    Database_Cross, 
    Provenance_Check, 
    Expert_Consult, 
    Carbon_Dating, 
    Forensic_Analyze, 
    Anomaly_Review, 
    Risk_Assess, 
    Report_Draft, 
    Insurance_Quote, 
    Storage_Plan, 
    Final_Approval
])

# Define the order (dependencies) between nodes
root.order.add_edge(Intake_Document, Visual_Inspect)
root.order.add_edge(Intake_Document, Imaging_Scan)
root.order.add_edge(Intake_Document, Material_Test)
root.order.add_edge(Intake_Document, Database_Cross)
root.order.add_edge(Visual_Inspect, Provenance_Check)
root.order.add_edge(Imaging_Scan, Provenance_Check)
root.order.add_edge(Material_Test, Provenance_Check)
root.order.add_edge(Database_Cross, Provenance_Check)
root.order.add_edge(Provenance_Check, Expert_Consult)
root.order.add_edge(Expert_Consult, Carbon_Dating)
root.order.add_edge(Carbon_Dating, Forensic_Analyze)
root.order.add_edge(Forensic_Analyze, Anomaly_Review)
root.order.add_edge(Anomaly_Review, Risk_Assess)
root.order.add_edge(Risk_Assess, Report_Draft)
root.order.add_edge(Report_Draft, Insurance_Quote)
root.order.add_edge(Insurance_Quote, Storage_Plan)
root.order.add_edge(Storage_Plan, Final_Approval)