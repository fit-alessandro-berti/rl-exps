from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with their labels
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

# Define the control-flow operators
exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[client_approval, packaging_prep, shipping_arrange, feedback_collect, portfolio_update, contract_sign, ip_management, future_schedule, maintenance_plan])
loop = OperatorPOWL(operator=Operator.LOOP, children=[concept_sketch, design_review, material_sourcing, prototype_build, vendor_coordination, quality_check])

# Define the root node as a StrictPartialOrder
root = StrictPartialOrder(nodes=[loop, exclusive_choice])
root.order.add_edge(loop, exclusive_choice)

# Print the root node
print(root)