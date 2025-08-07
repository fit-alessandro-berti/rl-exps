import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define the root node as a strict partial order
root = StrictPartialOrder(nodes=[
    concept_approve,
    budget_align,
    design_review,
    structure_simulate,
    material_procure,
    vendor_select,
    permit_apply,
    safety_check,
    site_prep,
    logistics_plan,
    fabricate_parts,
    assemble_onsite,
    quality_inspect,
    weather_monitor,
    public_unveil,
    maintenance_plan,
    stakeholder_meet
])

# Define dependencies if any (not specified in the problem description)
# Example: If there's a dependency between 'Design Review' and 'Material Procure', add it like this:
# root.order.add_edge(design_review, material_procure)

# Save the root node for further use or analysis
print(root)