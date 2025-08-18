import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
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

# Define the loop for material sourcing and prototype build
loop_material_source_prototype = OperatorPOWL(operator=Operator.LOOP, children=[material_sourcing, prototype_build])

# Define the XOR for quality check and client approval
xor_quality_check_client_approval = OperatorPOWL(operator=Operator.XOR, children=[quality_check, client_approval])

# Define the partial order
root = StrictPartialOrder(nodes=[
    client_brief,
    concept_sketch,
    design_review,
    loop_material_source_prototype,
    xor_quality_check_client_approval,
    packaging_prep,
    shipping_arrange,
    feedback_collect,
    portfolio_update,
    contract_sign,
    ip_management,
    future_schedule,
    maintenance_plan
])

# Define the dependencies
root.order.add_edge(client_brief, concept_sketch)
root.order.add_edge(concept_sketch, design_review)
root.order.add_edge(design_review, loop_material_source_prototype)
root.order.add_edge(loop_material_source_prototype, xor_quality_check_client_approval)
root.order.add_edge(xor_quality_check_client_approval, packaging_prep)
root.order.add_edge(packaging_prep, shipping_arrange)
root.order.add_edge(shipping_arrange, feedback_collect)
root.order.add_edge(feedback_collect, portfolio_update)
root.order.add_edge(portfolio_update, contract_sign)
root.order.add_edge(contract_sign, ip_management)
root.order.add_edge(ip_management, future_schedule)
root.order.add_edge(future_schedule, maintenance_plan)

# Print the root
print(root)