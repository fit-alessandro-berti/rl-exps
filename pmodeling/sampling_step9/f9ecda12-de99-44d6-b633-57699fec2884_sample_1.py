import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
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

# Define loop for permit process
permit_loop = OperatorPOWL(operator=Operator.LOOP, children=[permit_apply, safety_check])

# Define exclusive choice for design review and structure simulate
design_structure_choice = OperatorPOWL(operator=Operator.XOR, children=[design_review, structure_simulate])

# Define exclusive choice for material procure and vendor select
material_vendor_choice = OperatorPOWL(operator=Operator.XOR, children=[material_procure, vendor_select])

# Define exclusive choice for logistics plan and fabricate parts
logistics_fabricate_choice = OperatorPOWL(operator=Operator.XOR, children=[logistics_plan, fabricate_parts])

# Define exclusive choice for assemble onsite and quality inspect
assemble_quality_choice = OperatorPOWL(operator=Operator.XOR, children=[assemble_onsite, quality_inspect])

# Define exclusive choice for weather monitor and public unveil
weather_public_choice = OperatorPOWL(operator=Operator.XOR, children=[weather_monitor, public_unveil])

# Define exclusive choice for maintenance plan and stakeholder meet
maintenance_stakeholder_choice = OperatorPOWL(operator=Operator.XOR, children=[maintenance_plan, stakeholder_meet])

# Define root POWL model
root = StrictPartialOrder(nodes=[permit_loop, design_structure_choice, material_vendor_choice, logistics_fabricate_choice, assemble_quality_choice, weather_public_choice, maintenance_stakeholder_choice])
root.order.add_edge(permit_loop, design_structure_choice)
root.order.add_edge(design_structure_choice, material_vendor_choice)
root.order.add_edge(material_vendor_choice, logistics_fabricate_choice)
root.order.add_edge(logistics_fabricate_choice, assemble_quality_choice)
root.order.add_edge(assemble_quality_choice, weather_public_choice)
root.order.add_edge(weather_public_choice, maintenance_stakeholder_choice)

print(root)