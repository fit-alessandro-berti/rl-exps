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

# Define silent transitions
skip = SilentTransition()

# Define the loop for fabricating and assembling parts
loop = OperatorPOWL(operator=Operator.LOOP, children=[fabricate_parts, assemble_onsite])

# Define the XOR for weather monitoring and quality inspection
xor = OperatorPOWL(operator=Operator.XOR, children=[quality_inspect, weather_monitor])

# Define the partial order with all activities
root = StrictPartialOrder(
    nodes=[concept_approve, budget_align, design_review, structure_simulate, material_procure, vendor_select,
           permit_apply, safety_check, site_prep, logistics_plan, loop, xor, quality_inspect, weather_monitor,
           public_unveil, maintenance_plan, stakeholder_meet],
    order=[
        (concept_approve, budget_align),
        (budget_align, design_review),
        (design_review, structure_simulate),
        (structure_simulate, material_procure),
        (material_procure, vendor_select),
        (vendor_select, permit_apply),
        (permit_apply, safety_check),
        (safety_check, site_prep),
        (site_prep, logistics_plan),
        (logistics_plan, loop),
        (loop, xor),
        (xor, quality_inspect),
        (xor, weather_monitor),
        (quality_inspect, public_unveil),
        (weather_monitor, maintenance_plan),
        (maintenance_plan, stakeholder_meet)
    ]
)

# Add edges for loop and XOR
root.order.add_edge(loop, xor)
root.order.add_edge(xor, quality_inspect)
root.order.add_edge(xor, weather_monitor)

# Print the root
print(root)