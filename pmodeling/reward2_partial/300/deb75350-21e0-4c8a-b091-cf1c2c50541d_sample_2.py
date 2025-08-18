import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with their labels
Intake_Review = Transition(label='Intake Review')
Visual_Inspect = Transition(label='Visual Inspect')
Material_Test = Transition(label='Material Test')
Provenance_Check = Transition(label='Provenance Check')
Archival_Search = Transition(label='Archival Search')
Expert_Consult = Transition(label='Expert Consult')
Digital_Scan = Transition(label='Digital Scan')
Condition_Report = Transition(label='Condition Report')
Forgery_Assess = Transition(label='Forgery Assess')
Legal_Review = Transition(label='Legal Review')
Risk_Analysis = Transition(label='Risk Analysis')
Acquisition_Vote = Transition(label='Acquisition Vote')
Catalog_Entry = Transition(label='Catalog Entry')
Storage_Prep = Transition(label='Storage Prep')
Final_Approval = Transition(label='Final Approval')

# Define the partial order with dependencies
root = StrictPartialOrder(nodes=[
    Intake_Review, Visual_Inspect, Material_Test, Provenance_Check,
    Archival_Search, Expert_Consult, Digital_Scan, Condition_Report,
    Forging_Assess, Legal_Review, Risk_Analysis, Acquisition_Vote,
    Catalog_Entry, Storage_Prep, Final_Approval
])

# Add the dependencies
root.order.add_edge(Intake_Review, Visual_Inspect)
root.order.add_edge(Visual_Inspect, Material_Test)
root.order.add_edge(Material_Test, Provenance_Check)
root.order.add_edge(Provenance_Check, Archival_Search)
root.order.add_edge(Archival_Search, Expert_Consult)
root.order.add_edge(Expert_Consult, Digital_Scan)
root.order.add_edge(Digital_Scan, Condition_Report)
root.order.add_edge(Condition_Report, Forging_Assess)
root.order.add_edge(Forging_Assess, Legal_Review)
root.order.add_edge(Legal_Review, Risk_Analysis)
root.order.add_edge(Risk_Analysis, Acquisition_Vote)
root.order.add_edge(Acquisition_Vote, Catalog_Entry)
root.order.add_edge(Catalog_Entry, Storage_Prep)
root.order.add_edge(Storage_Prep, Final_Approval)