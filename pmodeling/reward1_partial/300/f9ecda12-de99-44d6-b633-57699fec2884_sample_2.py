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

# Define the POWL operators
xor_design_material = OperatorPOWL(operator=Operator.XOR, children=[material_procure, vendor_select])
xor_permit_safety = OperatorPOWL(operator=Operator.XOR, children=[permit_apply, safety_check])
xor_site_logistics = OperatorPOWL(operator=Operator.XOR, children=[site_prep, logistics_plan])
xor_fabricate_inspect = OperatorPOWL(operator=Operator.XOR, children=[fabricate_parts, assemble_onsite])
xor_quality_weather = OperatorPOWL(operator=Operator.XOR, children=[quality_inspect, weather_monitor])
xor_unveil_plan = OperatorPOWL(operator=Operator.XOR, children=[public_unveil, maintenance_plan])
xor_meet = OperatorPOWL(operator=Operator.XOR, children=[stakeholder_meet, ])

# Define the root node with the correct order of operations
root = StrictPartialOrder(nodes=[concept_approve, budget_align, design_review, structure_simulate, xor_design_material,
                                  xor_permit_safety, xor_site_logistics, xor_fabricate_inspect, xor_quality_weather,
                                  xor_unveil_plan, xor_meet])
root.order.add_edge(concept_approve, budget_align)
root.order.add_edge(budget_align, design_review)
root.order.add_edge(design_review, structure_simulate)
root.order.add_edge(structure_simulate, xor_design_material)
root.order.add_edge(xor_design_material, xor_permit_safety)
root.order.add_edge(xor_permit_safety, xor_site_logistics)
root.order.add_edge(xor_site_logistics, xor_fabricate_inspect)
root.order.add_edge(xor_fabricate_inspect, xor_quality_weather)
root.order.add_edge(xor_quality_weather, xor_unveil_plan)
root.order.add_edge(xor_unveil_plan, xor_meet)
root.order.add_edge(xor_meet, )

# Print the root POWL model
print(root)