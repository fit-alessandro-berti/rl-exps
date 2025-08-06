import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
root = StrictPartialOrder()

# Define the activities
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

# Define the transitions
xor1 = OperatorPOWL(operator=Operator.XOR, children=[permit_apply, safety_check])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[site_prep, logistics_plan])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[fabricate_parts, assemble_onsite])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[quality_inspect, weather_monitor])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[public_unveil, maintenance_plan])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[stakeholder_meet])

# Define the loop
loop = OperatorPOWL(operator=Operator.LOOP, children=[design_review, structure_simulate])

# Define the partial order
root.nodes = [loop, xor1, xor2, xor3, xor4, xor5, xor6]

# Define the dependencies
root.order.add_edge(loop, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor1)

# Print the result
print(root)