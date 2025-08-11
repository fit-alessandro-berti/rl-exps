import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL nodes
concept_approve = Transition(label='Concept Approve')
budget_align = Transition(label='Budget Align')
design_review = Transition(label='Design Review')
structure_simulate = Transition(label='Structure Simulate')
material_procure = Transition(label='Material Procure')
vendor_select = Transition(label='Vendor Select')
permit_apply = Transition(label='Permit Apply')
safety_check = Transition(label='Safety Check')
site_prep = Transition(label='Site Prep')
logistics_plan = Transition(label='Logistics Plan')
fabricate_parts = Transition(label='Fabricate Parts')
assemble_onsite = Transition(label='Assemble Onsite')
quality_inspect = Transition(label='Quality Inspect')
weather_monitor = Transition(label='Weather Monitor')
public_unveil = Transition(label='Public Unveil')
maintenance_plan = Transition(label='Maintenance Plan')
stakeholder_meet = Transition(label='Stakeholder Meet')
skip = SilentTransition()

# Define the POWL model
loop_design = OperatorPOWL(operator=Operator.LOOP, children=[design_review, structure_simulate])
loop_procure = OperatorPOWL(operator=Operator.LOOP, children=[material_procure, vendor_select])
loop_permit = OperatorPOWL(operator=Operator.LOOP, children=[permit_apply, safety_check])
loop_site_prep = OperatorPOWL(operator=Operator.LOOP, children=[site_prep, logistics_plan])
loop_fabricate = OperatorPOWL(operator=Operator.LOOP, children=[fabricate_parts, assemble_onsite])
loop_inspect = OperatorPOWL(operator=Operator.LOOP, children=[quality_inspect, weather_monitor])

xor_public_unveil = OperatorPOWL(operator=Operator.XOR, children=[public_unveil, skip])
xor_maintenance_plan = OperatorPOWL(operator=Operator.XOR, children=[maintenance_plan, skip])

root = StrictPartialOrder(nodes=[
    loop_design, loop_procure, loop_permit, loop_site_prep, loop_fabricate, loop_inspect,
    xor_public_unveil, xor_maintenance_plan, stakeholder_meet
])

# Add edges to the POWL model
root.order.add_edge(loop_design, loop_procure)
root.order.add_edge(loop_procure, loop_permit)
root.order.add_edge(loop_permit, loop_site_prep)
root.order.add_edge(loop_site_prep, loop_fabricate)
root.order.add_edge(loop_fabricate, loop_inspect)
root.order.add_edge(loop_inspect, xor_public_unveil)
root.order.add_edge(loop_inspect, xor_maintenance_plan)
root.order.add_edge(xor_public_unveil, stakeholder_meet)
root.order.add_edge(xor_maintenance_plan, stakeholder_meet)

print(root)