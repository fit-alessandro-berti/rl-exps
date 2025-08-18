from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the transitions (activities) with their exact names
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

# Define silent transitions (tau labels)
skip = SilentTransition()

# Define the workflow model
root = StrictPartialOrder()

# Define the workflow structure
# Client Brief -> Concept Sketch -> Design Review -> Material Sourcing -> Prototype Build -> Vendor Coordination
root.nodes.add(client_brief)
root.nodes.add(concept_sketch)
root.nodes.add(design_review)
root.nodes.add(material_sourcing)
root.nodes.add(prototype_build)
root.nodes.add(vendor_coordination)
root.order.add_edge(client_brief, concept_sketch)
root.order.add_edge(concept_sketch, design_review)
root.order.add_edge(design_review, material_sourcing)
root.order.add_edge(material_sourcing, prototype_build)
root.order.add_edge(prototype_build, vendor_coordination)

# Material Sourcing -> Quality Check -> Client Approval
root.nodes.add(quality_check)
root.order.add_edge(material_sourcing, quality_check)
root.order.add_edge(quality_check, client_approval)

# Client Approval -> Packaging Prep -> Shipping Arrange
root.nodes.add(packaging_prep)
root.nodes.add(shipping_arrange)
root.order.add_edge(client_approval, packaging_prep)
root.order.add_edge(packaging_prep, shipping_arrange)

# Packaging Prep -> Feedback Collect -> Portfolio Update
root.nodes.add(feedback_collect)
root.nodes.add(portfolio_update)
root.order.add_edge(packaging_prep, feedback_collect)
root.order.add_edge(feedback_collect, portfolio_update)

# Feedback Collect -> Contract Sign -> IP Management
root.nodes.add(contract_sign)
root.nodes.add(ip_management)
root.order.add_edge(feedback_collect, contract_sign)
root.order.add_edge(contract_sign, ip_management)

# Contract Sign -> Future Schedule -> Maintenance Plan
root.nodes.add(future_schedule)
root.nodes.add(maintenance_plan)
root.order.add_edge(contract_sign, future_schedule)
root.order.add_edge(future_schedule, maintenance_plan)

# Define the loop structure
loop = OperatorPOWL(operator=Operator.LOOP, children=[client_brief, concept_sketch, design_review, material_sourcing, prototype_build, vendor_coordination])
root.nodes.add(loop)
root.order.add_edge(loop, client_brief)

# Define the XOR structure
xor = OperatorPOWL(operator=Operator.XOR, children=[quality_check, client_approval])
root.nodes.add(xor)
root.order.add_edge(quality_check, xor)
root.order.add_edge(client_approval, xor)

# Define the XOR structure for packaging and shipping
xor_packaging = OperatorPOWL(operator=Operator.XOR, children=[packaging_prep, shipping_arrange])
root.nodes.add(xor_packaging)
root.order.add_edge(packaging_prep, xor_packaging)
root.order.add_edge(shipping_arrange, xor_packaging)

# Define the XOR structure for feedback and portfolio update
xor_feedback = OperatorPOWL(operator=Operator.XOR, children=[feedback_collect, portfolio_update])
root.nodes.add(xor_feedback)
root.order.add_edge(feedback_collect, xor_feedback)
root.order.add_edge(portfolio_update, xor_feedback)

# Define the XOR structure for contract sign and IP management
xor_contract = OperatorPOWL(operator=Operator.XOR, children=[contract_sign, ip_management])
root.nodes.add(xor_contract)
root.order.add_edge(contract_sign, xor_contract)
root.order.add_edge(ip_management, xor_contract)

# Define the XOR structure for future schedule and maintenance plan
xor_future = OperatorPOWL(operator=Operator.XOR, children=[future_schedule, maintenance_plan])
root.nodes.add(xor_future)
root.order.add_edge(future_schedule, xor_future)
root.order.add_edge(maintenance_plan, xor_future)

# Add the loop and XOR structures to the root
root.nodes.add(loop)
root.nodes.add(xor)
root.nodes.add(xor_packaging)
root.nodes.add(xor_feedback)
root.nodes.add(xor_contract)
root.nodes.add(xor_future)
root.order.add_edge(loop, xor)
root.order.add_edge(xor, xor_packaging)
root.order.add_edge(xor_packaging, xor_feedback)
root.order.add_edge(xor_feedback, xor_contract)
root.order.add_edge(xor_contract, xor_future)
root.order.add_edge(xor_future, loop)