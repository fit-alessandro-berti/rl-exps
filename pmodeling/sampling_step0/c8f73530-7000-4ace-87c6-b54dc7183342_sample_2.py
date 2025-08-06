import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model for the process
milk_sourcing = Transition(label='Milk Sourcing')
quality_testing = Transition(label='Quality Testing')
milk_pasteurize = Transition(label='Milk Pasteurize')
culture_inoculate = Transition(label='Culture Inoculate')
coagulation = Transition(label='Coagulation')
curd_cutting = Transition(label='Curd Cutting')
whey_drain = Transition(label='Whey Drain')
pressing = Transition(label='Pressing')
salting = Transition(label='Salting')
aging_control = Transition(label='Aging Control')
sensory_audit = Transition(label='Sensory Audit')
packaging_design = Transition(label='Packaging Design')
label_approval = Transition(label='Label Approval')
order_customization = Transition(label='Order Customization')
logistics_plan = Transition(label='Logistics Plan')
market_delivery = Transition(label='Market Delivery')
customer_feedback = Transition(label='Customer Feedback')
regulatory_check = Transition(label='Regulatory Check')
skip = SilentTransition()

# Define the workflow structure
milk_flow = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, skip])
quality_flow = OperatorPOWL(operator=Operator.XOR, children=[quality_testing, skip])
milk_pasteurize_flow = OperatorPOWL(operator=Operator.XOR, children=[milk_pasteurize, skip])
culture_inoculate_flow = OperatorPOWL(operator=Operator.XOR, children=[culture_inoculate, skip])
coagulation_flow = OperatorPOWL(operator=Operator.XOR, children=[coagulation, skip])
curd_cutting_flow = OperatorPOWL(operator=Operator.XOR, children=[curd_cutting, skip])
whey_drain_flow = OperatorPOWL(operator=Operator.XOR, children=[whey_drain, skip])
pressing_flow = OperatorPOWL(operator=Operator.XOR, children=[pressing, skip])
salting_flow = OperatorPOWL(operator=Operator.XOR, children=[salting, skip])
aging_control_flow = OperatorPOWL(operator=Operator.XOR, children=[aging_control, skip])
sensory_audit_flow = OperatorPOWL(operator=Operator.XOR, children=[sensory_audit, skip])
packaging_design_flow = OperatorPOWL(operator=Operator.XOR, children=[packaging_design, skip])
label_approval_flow = OperatorPOWL(operator=Operator.XOR, children=[label_approval, skip])
order_customization_flow = OperatorPOWL(operator=Operator.XOR, children=[order_customization, skip])
logistics_plan_flow = OperatorPOWL(operator=Operator.XOR, children=[logistics_plan, skip])
market_delivery_flow = OperatorPOWL(operator=Operator.XOR, children=[market_delivery, skip])
customer_feedback_flow = OperatorPOWL(operator=Operator.XOR, children=[customer_feedback, skip])
regulatory_check_flow = OperatorPOWL(operator=Operator.XOR, children=[regulatory_check, skip])

# Define the loop for the aging control process
aging_control_loop = OperatorPOWL(operator=Operator.LOOP, children=[aging_control_flow, sensory_audit_flow])

# Define the root node with the workflow structure
root = StrictPartialOrder(nodes=[
    milk_flow,
    quality_flow,
    milk_pasteurize_flow,
    culture_inoculate_flow,
    coagulation_flow,
    curd_cutting_flow,
    whey_drain_flow,
    pressing_flow,
    salting_flow,
    aging_control_loop,
    packaging_design_flow,
    label_approval_flow,
    order_customization_flow,
    logistics_plan_flow,
    market_delivery_flow,
    customer_feedback_flow,
    regulatory_check_flow
])

# Add the dependencies between the nodes
root.order.add_edge(milk_flow, quality_flow)
root.order.add_edge(milk_flow, milk_pasteurize_flow)
root.order.add_edge(milk_flow, culture_inoculate_flow)
root.order.add_edge(milk_flow, coagulation_flow)
root.order.add_edge(milk_flow, curd_cutting_flow)
root.order.add_edge(milk_flow, whey_drain_flow)
root.order.add_edge(milk_flow, pressing_flow)
root.order.add_edge(milk_flow, salting_flow)
root.order.add_edge(milk_flow, aging_control_loop)
root.order.add_edge(milk_flow, packaging_design_flow)
root.order.add_edge(milk_flow, label_approval_flow)
root.order.add_edge(milk_flow, order_customization_flow)
root.order.add_edge(milk_flow, logistics_plan_flow)
root.order.add_edge(milk_flow, market_delivery_flow)
root.order.add_edge(milk_flow, customer_feedback_flow)
root.order.add_edge(milk_flow, regulatory_check_flow)

root.order.add_edge(quality_flow, milk_pasteurize_flow)
root.order.add_edge(quality_flow, culture_inoculate_flow)
root.order.add_edge(quality_flow, coagulation_flow)
root.order.add_edge(quality_flow, curd_cutting_flow)
root.order.add_edge(quality_flow, whey_drain_flow)
root.order.add_edge(quality_flow, pressing_flow)
root.order.add_edge(quality_flow, salting_flow)
root.order.add_edge(quality_flow, aging_control_loop)
root.order.add_edge(quality_flow, packaging_design_flow)
root.order.add_edge(quality_flow, label_approval_flow)
root.order.add_edge(quality_flow, order_customization_flow)
root.order.add_edge(quality_flow, logistics_plan_flow)
root.order.add_edge(quality_flow, market_delivery_flow)
root.order.add_edge(quality_flow, customer_feedback_flow)
root.order.add_edge(quality_flow, regulatory_check_flow)

root.order.add_edge(milk_pasteurize_flow, culture_inoculate_flow)
root.order.add_edge(milk_pasteurize_flow, coagulation_flow)
root.order.add_edge(milk_pasteurize_flow, curd_cutting_flow)
root.order.add_edge(milk_pasteurize_flow, whey_drain_flow)
root.order.add_edge(milk_pasteurize_flow, pressing_flow)
root.order.add_edge(milk_pasteurize_flow, salting_flow)
root.order.add_edge(milk_pasteurize_flow, aging_control_loop)
root.order.add_edge(milk_pasteurize_flow, packaging_design_flow)
root.order.add_edge(milk_pasteurize_flow, label_approval_flow)
root.order.add_edge(milk_pasteurize_flow, order_customization_flow)
root.order.add_edge(milk_pasteurize_flow, logistics_plan_flow)
root.order.add_edge(milk_pasteurize_flow, market_delivery_flow)
root.order.add_edge(milk_pasteurize_flow, customer_feedback_flow)
root.order.add_edge(milk_pasteurize_flow, regulatory_check_flow)

root.order.add_edge(culture_inoculate_flow, coagulation_flow)
root.order.add_edge(culture_inoculate_flow, curd_cutting_flow)
root.order.add_edge(culture_inoculate_flow, whey_drain_flow)
root.order.add_edge(culture_inoculate_flow, pressing_flow)
root.order.add_edge(culture_inoculate_flow, salting_flow)
root.order.add_edge(culture_inoculate_flow, aging_control_loop)
root.order.add_edge(culture_inoculate_flow, packaging_design_flow)
root.order.add_edge(culture_inoculate_flow, label_approval_flow)
root.order.add_edge(culture_inoculate_flow, order_customization_flow)
root.order.add_edge(culture_inoculate_flow, logistics_plan_flow)
root.order.add_edge(culture_inoculate_flow, market_delivery_flow)
root.order.add_edge(culture_inoculate_flow, customer_feedback_flow)
root.order.add_edge(culture_inoculate_flow, regulatory_check_flow)

root.order.add_edge(coagulation_flow, curd_cutting_flow)
root.order.add_edge(coagulation_flow, whey_drain_flow)
root.order.add_edge(coagulation_flow, pressing_flow)
root.order.add_edge(coagulation_flow, salting_flow)
root.order.add_edge(coagulation_flow, aging_control_loop)
root.order.add_edge(coagulation_flow, packaging_design_flow)
root.order.add_edge(coagulation_flow, label_approval_flow)
root.order.add_edge(coagulation_flow, order_customization_flow)
root.order.add_edge(coagulation_flow, logistics_plan_flow)
root.order.add_edge(coagulation_flow, market_delivery_flow)
root.order.add_edge(coagulation_flow, customer_feedback_flow)
root.order.add_edge(coagulation_flow, regulatory_check_flow)

root.order.add_edge(curd_cutting_flow, whey_drain_flow)
root.order.add_edge(curd_cutting_flow, pressing_flow)
root.order.add_edge(curd_cutting_flow, salting_flow)
root.order.add_edge(curd_cutting_flow, aging_control_loop)
root.order.add_edge(curd_cutting_flow, packaging_design_flow)
root.order.add_edge(curd_cutting_flow, label_approval_flow)
root.order.add_edge(curd_cutting_flow, order_customization_flow)
root.order.add_edge(curd_cutting_flow, logistics_plan_flow)
root.order.add_edge(curd_cutting_flow, market_delivery_flow)
root.order.add_edge(curd_cutting_flow, customer_feedback_flow)
root.order.add_edge(curd_cutting_flow, regulatory_check_flow)

root.order.add_edge(whey_drain_flow, pressing_flow)
root.order.add_edge(whey_drain_flow, salting_flow)
root.order.add_edge(whey_drain_flow, aging_control_loop)
root.order.add_edge(whey_drain_flow, packaging_design_flow)
root.order.add_edge(whey_drain_flow, label_approval_flow)
root.order.add_edge(whey_drain_flow, order_customization_flow)
root.order.add_edge(whey_drain_flow, logistics_plan_flow)
root.order.add_edge(whey_drain_flow, market_delivery_flow)
root.order.add_edge(whey_drain_flow, customer_feedback_flow)
root.order.add_edge(whey_drain_flow, regulatory_check_flow)

root.order.add_edge(pressing_flow, salting_flow)
root.order.add_edge(pressing_flow, aging_control_loop)
root.order.add_edge(pressing_flow, packaging_design_flow)
root.order.add_edge(pressing_flow, label_approval_flow)
root.order.add_edge(pressing_flow, order_customization_flow)
root.order.add_edge(pressing_flow, logistics_plan_flow)
root.order.add_edge(pressing_flow, market_delivery_flow)
root.order.add_edge(pressing_flow, customer_feedback_flow)
root.order.add_edge(pressing_flow, regulatory_check_flow)

root.order.add_edge(salting_flow, aging_control_loop)
root.order.add_edge(salting_flow, packaging_design_flow)
root.order.add_edge(salting_flow, label_approval_flow)
root.order.add_edge(salting_flow, order_customization_flow)
root.order.add_edge(salting_flow, logistics_plan_flow)
root.order.add_edge(salting_flow, market_delivery_flow)
root.order.add_edge(salting_flow, customer_feedback_flow)
root.order.add_edge(salting_flow, regulatory_check_flow)

root.order.add_edge(aging_control_loop, packaging_design_flow)
root.order.add_edge(aging_control_loop, label_approval_flow)
root.order.add_edge(aging_control_loop, order_customization_flow)
root.order.add_edge(aging_control_loop, logistics_plan_flow)
root.order.add_edge(aging_control_loop, market_delivery_flow)
root.order.add_edge(aging_control_loop, customer_feedback_flow)
root.order.add_edge(aging_control_loop, regulatory_check_flow)

root.order.add_edge(packaging_design_flow, label_approval_flow)
root.order.add_edge(packaging_design_flow, order_customization_flow)
root.order.add_edge(packaging_design_flow, logistics_plan_flow)
root.order.add_edge(packaging_design_flow, market_delivery_flow)
root.order.add_edge(packaging_design_flow, customer_feedback_flow)
root.order.add_edge(packaging_design_flow, regulatory_check_flow)

root.order.add_edge(label_approval_flow, order_customization_flow)
root.order.add_edge(label_approval_flow, logistics_plan_flow)
root.order.add_edge(label_approval_flow, market_delivery_flow)
root.order.add_edge(label_approval_flow, customer_feedback_flow)
root.order.add_edge(label_approval_flow, regulatory_check_flow)

root.order.add_edge(order_customization_flow, logistics_plan_flow)
root.order.add_edge(order_customization_flow, market_delivery_flow)
root.order.add_edge(order_customization_flow, customer_feedback_flow)
root.order.add_edge(order_customization_flow, regulatory_check_flow)

root.order.add_edge(logistics_plan_flow, market_delivery_flow)
root.order.add_edge(logistics_plan_flow, customer_feedback_flow)
root.order.add_edge(logistics_plan_flow, regulatory_check_flow)

root.order.add_edge(market_delivery_flow, customer_feedback_flow)
root.order.add_edge(market_delivery_flow, regulatory_check_flow)

root.order.add_edge(customer_feedback_flow, regulatory_check_flow)

print(root)