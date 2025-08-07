import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the root of the POWL model as a strict partial order
root = StrictPartialOrder(nodes=[
    concept_approve, budget_align, design_review, structure_simulate,
    material_procure, vendor_select, permit_apply, safety_check,
    site_prep, logistics_plan, fabricate_parts, assemble_onsite,
    quality_inspect, weather_monitor, public_unveil, maintenance_plan,
    stakeholder_meet
])

# Add dependencies to the root
root.order.add_edge(concept_approve, budget_align)
root.order.add_edge(concept_approve, design_review)
root.order.add_edge(concept_approve, structure_simulate)
root.order.add_edge(concept_approve, material_procure)
root.order.add_edge(concept_approve, vendor_select)
root.order.add_edge(budget_align, permit_apply)
root.order.add_edge(budget_align, safety_check)
root.order.add_edge(budget_align, site_prep)
root.order.add_edge(budget_align, logistics_plan)
root.order.add_edge(design_review, fabricate_parts)
root.order.add_edge(design_review, assemble_onsite)
root.order.add_edge(structure_simulate, fabricate_parts)
root.order.add_edge(material_procure, fabricate_parts)
root.order.add_edge(vendor_select, fabricate_parts)
root.order.add_edge(permit_apply, safety_check)
root.order.add_edge(permit_apply, site_prep)
root.order.add_edge(permit_apply, logistics_plan)
root.order.add_edge(safety_check, quality_inspect)
root.order.add_edge(safety_check, weather_monitor)
root.order.add_edge(site_prep, fabricate_parts)
root.order.add_edge(site_prep, assemble_onsite)
root.order.add_edge(logistics_plan, fabricate_parts)
root.order.add_edge(logistics_plan, assemble_onsite)
root.order.add_edge(fabricate_parts, quality_inspect)
root.order.add_edge(fabricate_parts, weather_monitor)
root.order.add_edge(assemble_onsite, quality_inspect)
root.order.add_edge(assemble_onsite, weather_monitor)
root.order.add_edge(quality_inspect, public_unveil)
root.order.add_edge(quality_inspect, maintenance_plan)
root.order.add_edge(weather_monitor, public_unveil)
root.order.add_edge(weather_monitor, maintenance_plan)
root.order.add_edge(public_unveil, stakeholder_meet)
root.order.add_edge(maintenance_plan, stakeholder_meet)

# Print the root
print(root)