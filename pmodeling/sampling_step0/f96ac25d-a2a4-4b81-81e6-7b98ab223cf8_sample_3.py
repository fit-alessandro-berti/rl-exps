import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator
from collections import defaultdict

# Define transitions
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

# Define silent transitions
skip = SilentTransition()

# Define partial orders
loop_1 = OperatorPOWL(operator=Operator.LOOP, children=[quality_check, skip])
loop_2 = OperatorPOWL(operator=Operator.LOOP, children=[vendor_coordination, skip])
loop_3 = OperatorPOWL(operator=Operator.LOOP, children=[prototype_build, skip])
loop_4 = OperatorPOWL(operator=Operator.LOOP, children=[material_sourcing, skip])
loop_5 = OperatorPOWL(operator=Operator.LOOP, children=[design_review, skip])

xor_1 = OperatorPOWL(operator=Operator.XOR, children=[contract_sign, ip_management])
xor_2 = OperatorPOWL(operator=Operator.XOR, children=[future_schedule, maintenance_plan])

# Define root partial order
root = StrictPartialOrder(nodes=[client_brief, concept_sketch, loop_1, loop_2, loop_3, loop_4, loop_5, xor_1, xor_2])

# Define dependencies
root.order.add_edge(client_brief, concept_sketch)
root.order.add_edge(concept_sketch, loop_1)
root.order.add_edge(loop_1, design_review)
root.order.add_edge(design_review, loop_2)
root.order.add_edge(loop_2, vendor_coordination)
root.order.add_edge(vendor_coordination, loop_3)
root.order.add_edge(loop_3, prototype_build)
root.order.add_edge(prototype_build, loop_4)
root.order.add_edge(loop_4, material_sourcing)
root.order.add_edge(material_sourcing, loop_5)
root.order.add_edge(loop_5, quality_check)
root.order.add_edge(quality_check, client_approval)
root.order.add_edge(client_approval, xor_1)
root.order.add_edge(xor_1, packaging_prep)
root.order.add_edge(packaging_prep, shipping_arrange)
root.order.add_edge(shipping_arrange, feedback_collect)
root.order.add_edge(feedback_collect, xor_2)
root.order.add_edge(xor_2, contract_sign)
root.order.add_edge(contract_sign, ip_management)
root.order.add_edge(ip_management, future_schedule)
root.order.add_edge(future_schedule, maintenance_plan)
root.order.add_edge(maintenance_plan, client_brief)

# Print the root
print(root)