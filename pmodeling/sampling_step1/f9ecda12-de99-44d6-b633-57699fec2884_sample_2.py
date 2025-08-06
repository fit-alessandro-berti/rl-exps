from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with exact names
ConceptApprove = Transition(label='Concept Approve')
BudgetAlign = Transition(label='Budget Align')
DesignReview = Transition(label='Design Review')
StructureSimulate = Transition(label='Structure Simulate')
MaterialProcure = Transition(label='Material Procure')
VendorSelect = Transition(label='Vendor Select')
PermitApply = Transition(label='Permit Apply')
SafetyCheck = Transition(label='Safety Check')
SitePrep = Transition(label='Site Prep')
LogisticsPlan = Transition(label='Logistics Plan')
FabricateParts = Transition(label='Fabricate Parts')
AssembleOnsite = Transition(label='Assemble Onsite')
QualityInspect = Transition(label='Quality Inspect')
WeatherMonitor = Transition(label='Weather Monitor')
PublicUnveil = Transition(label='Public Unveil')
MaintenancePlan = Transition(label='Maintenance Plan')
StakeholderMeet = Transition(label='Stakeholder Meet')

# Define the partial order model
root = StrictPartialOrder(nodes=[
    ConceptApprove, BudgetAlign, DesignReview, StructureSimulate, MaterialProcure, VendorSelect, PermitApply, SafetyCheck,
    SitePrep, LogisticsPlan, FabricateParts, AssembleOnsite, QualityInspect, WeatherMonitor, PublicUnveil, MaintenancePlan,
    StakeholderMeet
])

# Define the dependencies (edges) in the partial order
root.order.add_edge(ConceptApprove, BudgetAlign)
root.order.add_edge(BudgetAlign, DesignReview)
root.order.add_edge(DesignReview, StructureSimulate)
root.order.add_edge(StructureSimulate, MaterialProcure)
root.order.add_edge(MaterialProcure, VendorSelect)
root.order.add_edge(VendorSelect, PermitApply)
root.order.add_edge(PermitApply, SafetyCheck)
root.order.add_edge(SafetyCheck, SitePrep)
root.order.add_edge(SitePrep, LogisticsPlan)
root.order.add_edge(LogisticsPlan, FabricateParts)
root.order.add_edge(FabricateParts, AssembleOnsite)
root.order.add_edge(AssembleOnsite, QualityInspect)
root.order.add_edge(QualityInspect, WeatherMonitor)
root.order.add_edge(WeatherMonitor, PublicUnveil)
root.order.add_edge(PublicUnveil, MaintenancePlan)
root.order.add_edge(MaintenancePlan, StakeholderMeet)

print(root)