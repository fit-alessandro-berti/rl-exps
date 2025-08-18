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

# Define the process
xor1 = OperatorPOWL(operator=Operator.XOR, children=[material_sourcing, vendor_coordination])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[quality_check, packaging_prep])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[shipping_arrange, feedback_collect])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[contract_sign, ip_management])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[future_schedule, maintenance_plan])

root = StrictPartialOrder(nodes=[client_brief, concept_sketch, design_review, xor1, xor2, xor3, xor4, xor5])
root.order.add_edge(client_brief, concept_sketch)
root.order.add_edge(concept_sketch, design_review)
root.order.add_edge(design_review, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor1, xor3)
root.order.add_edge(xor2, xor4)
root.order.add_edge(xor3, xor5)
root.order.add_edge(xor4, xor5)