import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
client_brief = Transition(label='Client Brief')
concept_sketch = Transition(label='Concept Sketch')
design_review = Transition(label='Design Review')
material_sourcing = Transition(label='Material Sourcing')
prototype_build = Transition(label='Prototype Build')
vendor_coordination = Transition(label='Vendor Coordination')
quality_check = Transition(label='Quality Check')
client_approval = Transition(label='Client Approval')
packaging_prep = Transition(label='Packaging Prep')
shipping_arrange = Transition(label='Shipping Arrange')
feedback_collect = Transition(label='Feedback Collect')
portfolio_update = Transition(label='Portfolio Update')
contract_sign = Transition(label='Contract Sign')
ip_management = Transition(label='IP Management')
future_schedule = Transition(label='Future Schedule')
maintenance_plan = Transition(label='Maintenance Plan')

# Define the silent transition
skip = SilentTransition()

# Define the loops and choices
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[material_sourcing, vendor_coordination])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[quality_check, client_approval])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[packaging_prep, shipping_arrange])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[feedback_collect, portfolio_update])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[contract_sign, ip_management])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[future_schedule, maintenance_plan])

# Define the root model
root = StrictPartialOrder(nodes=[loop1, loop2, xor1, xor2, xor3, xor4])
root.order.add_edge(loop1, xor1)
root.order.add_edge(loop2, xor2)
root.order.add_edge(xor1, xor3)
root.order.add_edge(xor2, xor4)

# Print the root model
print(root)