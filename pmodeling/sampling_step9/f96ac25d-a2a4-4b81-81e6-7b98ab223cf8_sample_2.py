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

# Define silent transitions
skip = SilentTransition()

# Define loops and exclusive choices
design_loop = OperatorPOWL(operator=Operator.LOOP, children=[design_review, quality_check])
vendor_loop = OperatorPOWL(operator=Operator.LOOP, children=[vendor_coordination, skip])
contract_loop = OperatorPOWL(operator=Operator.LOOP, children=[contract_sign, ip_management])
schedule_loop = OperatorPOWL(operator=Operator.LOOP, children=[future_schedule, maintenance_plan])

# Define exclusive choices
exclusive_choice1 = OperatorPOWL(operator=Operator.XOR, children=[design_loop, vendor_loop])
exclusive_choice2 = OperatorPOWL(operator=Operator.XOR, children=[contract_loop, schedule_loop])

# Define the root POWL model
root = StrictPartialOrder(nodes=[client_brief, concept_sketch, exclusive_choice1, exclusive_choice2])
root.order.add_edge(client_brief, concept_sketch)
root.order.add_edge(concept_sketch, exclusive_choice1)
root.order.add_edge(concept_sketch, exclusive_choice2)
root.order.add_edge(exclusive_choice1, design_loop)
root.order.add_edge(exclusive_choice1, vendor_loop)
root.order.add_edge(exclusive_choice2, contract_loop)
root.order.add_edge(exclusive_choice2, schedule_loop)

print(root)