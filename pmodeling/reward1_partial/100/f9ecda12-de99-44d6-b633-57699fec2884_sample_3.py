from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define the POWL model
loop_design = OperatorPOWL(operator=Operator.LOOP, children=[Design_Review, Structure_Simulate])
loop_procure = OperatorPOWL(operator=Operator.LOOP, children=[Material_Procure, Vendor_Select])
loop_permit = OperatorPOWL(operator=Operator.LOOP, children=[Permit_Apply, Safety_Check])
loop_logistics = OperatorPOWL(operator=Operator.LOOP, children=[Site_Prep, Logistics_Plan])
loop_fabricate = OperatorPOWL(operator=Operator.LOOP, children=[Fabricate_Parts, Assemble_Onsite])
loop_inspect = OperatorPOWL(operator=Operator.LOOP, children=[Quality_Inspect, Weather_Monitor])
loop_unveil = OperatorPOWL(operator=Operator.LOOP, children=[Public_Unveil, Maintenance_Plan])
loop_stakeholder = OperatorPOWL(operator=Operator.LOOP, children=[Stakeholder_Meet])

root = StrictPartialOrder(nodes=[
    Concept_Approve,
    Budget_Align,
    loop_design,
    loop_procure,
    loop_permit,
    loop_logistics,
    loop_fabricate,
    loop_inspect,
    loop_unveil,
    loop_stakeholder
])

root.order.add_edge(Concept_Approve, Budget_Align)
root.order.add_edge(Budget_Align, loop_design)
root.order.add_edge(loop_design, loop_procure)
root.order.add_edge(loop_procure, loop_permit)
root.order.add_edge(loop_permit, loop_logistics)
root.order.add_edge(loop_logistics, loop_fabricate)
root.order.add_edge(loop_fabricate, loop_inspect)
root.order.add_edge(loop_inspect, loop_unveil)
root.order.add_edge(loop_unveil, loop_stakeholder)
root.order.add_edge(loop_stakeholder, Public_Unveil)