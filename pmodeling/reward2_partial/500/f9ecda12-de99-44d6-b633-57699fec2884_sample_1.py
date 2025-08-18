import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
Concept_Approve = Transition(label='Concept Approve')
Budget_Align = Transition(label='Budget Align')
Design_Review = Transition(label='Design Review')
Structure_Simulate = Transition(label='Structure Simulate')
Material_Procure = Transition(label='Material Procure')
Vendor_Select = Transition(label='Vendor Select')
Permit_Apply = Transition(label='Permit Apply')
Safety_Check = Transition(label='Safety Check')
Site_Prep = Transition(label='Site Prep')
Logistics_Plan = Transition(label='Logistics Plan')
Fabricate_Parts = Transition(label='Fabricate Parts')
Assemble_Onsite = Transition(label='Assemble Onsite')
Quality_Inspect = Transition(label='Quality Inspect')
Weather_Monitor = Transition(label='Weather Monitor')
Public_Unveil = Transition(label='Public Unveil')
Maintenance_Plan = Transition(label='Maintenance Plan')
Stakeholder_Meet = Transition(label='Stakeholder Meet')

# Define the partial order
root = StrictPartialOrder(nodes=[
    Concept_Approve,
    Budget_Align,
    Design_Review,
    Structure_Simulate,
    Material_Procure,
    Vendor_Select,
    Permit_Apply,
    Safety_Check,
    Site_Prep,
    Logistics_Plan,
    Fabricate_Parts,
    Assemble_Onsite,
    Quality_Inspect,
    Weather_Monitor,
    Public_Unveil,
    Maintenance_Plan,
    Stakeholder_Meet
])

# Define the order dependencies
root.order.add_edge(Concept_Approve, Budget_Align)
root.order.add_edge(Budget_Align, Design_Review)
root.order.add_edge(Design_Review, Structure_Simulate)
root.order.add_edge(Structure_Simulate, Material_Procure)
root.order.add_edge(Material_Procure, Vendor_Select)
root.order.add_edge(Vendor_Select, Permit_Apply)
root.order.add_edge(Permit_Apply, Safety_Check)
root.order.add_edge(Safety_Check, Site_Prep)
root.order.add_edge(Site_Prep, Logistics_Plan)
root.order.add_edge(Logistics_Plan, Fabricate_Parts)
root.order.add_edge(Fabricate_Parts, Assemble_Onsite)
root.order.add_edge(Assemble_Onsite, Quality_Inspect)
root.order.add_edge(Quality_Inspect, Weather_Monitor)
root.order.add_edge(Weather_Monitor, Public_Unveil)
root.order.add_edge(Public_Unveil, Maintenance_Plan)
root.order.add_edge(Maintenance_Plan, Stakeholder_Meet)

# Print the root model
print(root)