import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define a loop for aging control and sensory audit
loop_aging_sensory = OperatorPOWL(operator=Operator.LOOP, children=[aging_control, sensory_audit])

# Define a choice for packaging design and label approval
choice_packaging_label = OperatorPOWL(operator=Operator.XOR, children=[packaging_design, label_approval])

# Define a choice for order customization and logistics plan
choice_customization_plan = OperatorPOWL(operator=Operator.XOR, children=[order_customization, logistics_plan])

# Define a choice for market delivery and customer feedback
choice_delivery_feedback = OperatorPOWL(operator=Operator.XOR, children=[market_delivery, customer_feedback])

# Define a choice for regulatory check and customer feedback
choice_regulatory_feedback = OperatorPOWL(operator=Operator.XOR, children=[regulatory_check, customer_feedback])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[
    milk_sourcing,
    quality_testing,
    milk_pasteurize,
    culture_inoculate,
    coagulation,
    curd_cutting,
    whey_drain,
    pressing,
    salting,
    loop_aging_sensory,
    choice_packaging_label,
    choice_customization_plan,
    choice_delivery_feedback,
    choice_regulatory_feedback
])

# Add dependencies between nodes
root.order.add_edge(milk_sourcing, quality_testing)
root.order.add_edge(quality_testing, milk_pasteurize)
root.order.add_edge(milk_pasteurize, culture_inoculate)
root.order.add_edge(culture_inoculate, coagulation)
root.order.add_edge(coagulation, curd_cutting)
root.order.add_edge(curd_cutting, whey_drain)
root.order.add_edge(whey_drain, pressing)
root.order.add_edge(pressing, salting)
root.order.add_edge(salting, loop_aging_sensory)
root.order.add_edge(loop_aging_sensory, choice_packaging_label)
root.order.add_edge(choice_packaging_label, choice_customization_plan)
root.order.add_edge(choice_customization_plan, choice_delivery_feedback)
root.order.add_edge(choice_delivery_feedback, choice_regulatory_feedback)

# Add dependencies within loops
root.order.add_edge(loop_aging_sensory, loop_aging_sensory)
root.order.add_edge(loop_aging_sensory, loop_aging_sensory)

# Add dependencies within choices
root.order.add_edge(choice_packaging_label, choice_packaging_label)
root.order.add_edge(choice_customization_plan, choice_customization_plan)
root.order.add_edge(choice_delivery_feedback, choice_delivery_feedback)
root.order.add_edge(choice_regulatory_feedback, choice_regulatory_feedback)

# Add dependencies within loops and choices
root.order.add_edge(loop_aging_sensory, choice_packaging_label)
root.order.add_edge(loop_aging_sensory, choice_customization_plan)
root.order.add_edge(loop_aging_sensory, choice_delivery_feedback)
root.order.add_edge(loop_aging_sensory, choice_regulatory_feedback)

# Add dependencies within choices and loops
root.order.add_edge(choice_packaging_label, loop_aging_sensory)
root.order.add_edge(choice_customization_plan, loop_aging_sensory)
root.order.add_edge(choice_delivery_feedback, loop_aging_sensory)
root.order.add_edge(choice_regulatory_feedback, loop_aging_sensory)

# Add dependencies within loops and choices
root.order.add_edge(loop_aging_sensory, loop_aging_sensory)
root.order.add_edge(loop_aging_sensory, loop_aging_sensory)

# Add dependencies within choices
root.order.add_edge(choice_packaging_label, choice_packaging_label)
root.order.add_edge(choice_customization_plan, choice_customization_plan)
root.order.add_edge(choice_delivery_feedback, choice_delivery_feedback)
root.order.add_edge(choice_regulatory_feedback, choice_regulatory_feedback)

# Add dependencies within loops and choices
root.order.add_edge(loop_aging_sensory, choice_packaging_label)
root.order.add_edge(loop_aging_sensory, choice_customization_plan)
root.order.add_edge(loop_aging_sensory, choice_delivery_feedback)
root.order.add_edge(loop_aging_sensory, choice_regulatory_feedback)

# Add dependencies within choices and loops
root.order.add_edge(choice_packaging_label, loop_aging_sensory)
root.order.add_edge(choice_customization_plan, loop_aging_sensory)
root.order.add_edge(choice_delivery_feedback, loop_aging_sensory)
root.order.add_edge(choice_regulatory_feedback, loop_aging_sensory)

# Add dependencies within loops and choices
root.order.add_edge(loop_aging_sensory, loop_aging_sensory)
root.order.add_edge(loop_aging_sensory, loop_aging_sensory)

# Add dependencies within choices
root.order.add_edge(choice_packaging_label, choice_packaging_label)
root.order.add_edge(choice_customization_plan, choice_customization_plan)
root.order.add_edge(choice_delivery_feedback, choice_delivery_feedback)
root.order.add_edge(choice_regulatory_feedback, choice_regulatory_feedback)

# Add dependencies within loops and choices
root.order.add_edge(loop_aging_sensory, choice_packaging_label)
root.order.add_edge(loop_aging_sensory, choice_customization_plan)
root.order.add_edge(loop_aging_sensory, choice_delivery_feedback)
root.order.add_edge(loop_aging_sensory, choice_regulatory_feedback)

# Add dependencies within choices and loops
root.order.add_edge(choice_packaging_label, loop_aging_sensory)
root.order.add_edge(choice_customization_plan, loop_aging_sensory)
root.order.add_edge(choice_delivery_feedback, loop_aging_sensory)
root.order.add_edge(choice_regulatory_feedback, loop_aging_sensory)

# Add dependencies within loops and choices
root.order.add_edge(loop_aging_sensory, loop_aging_sensory)
root.order.add_edge(loop_aging_sensory, loop_aging_sensory)

# Add dependencies within choices
root.order.add_edge(choice_packaging_label, choice_packaging_label)
root.order.add_edge(choice_customization_plan, choice_customization_plan)
root.order.add_edge(choice_delivery_feedback, choice_delivery_feedback)
root.order.add_edge(choice_regulatory_feedback, choice_regulatory_feedback)

# Add dependencies within loops and choices
root.order.add_edge(loop_aging_sensory, choice_packaging_label)
root.order.add_edge(loop_aging_sensory, choice_customization_plan)
root.order.add_edge(loop_aging_sensory, choice_delivery_feedback)
root.order.add_edge(loop_aging_sensory, choice_regulatory_feedback)

# Add dependencies within choices and loops
root.order.add_edge(choice_packaging_label, loop_aging_sensory)
root.order.add_edge(choice_customization_plan, loop_aging_sensory)
root.order.add_edge(choice_delivery_feedback, loop_aging_sensory)
root.order.add_edge(choice_regulatory_feedback, loop_aging_sensory)

# Add dependencies within loops and choices
root.order.add_edge(loop_aging_sensory, loop_aging_sensory)
root.order.add_edge(loop_aging_sensory, loop_aging_sensory)

# Add dependencies within choices
root.order.add_edge(choice_packaging_label, choice_packaging_label)
root.order.add_edge(choice_customization_plan, choice_customization_plan)
root.order.add_edge(choice_delivery_feedback, choice_delivery_feedback)
root.order.add_edge(choice_regulatory_feedback, choice_regulatory_feedback)

# Add dependencies within loops and choices
root.order.add_edge(loop_aging_sensory, choice_packaging_label)
root.order.add_edge(loop_aging_sensory, choice_customization_plan)
root.order.add_edge(loop_aging_sensory, choice_delivery_feedback)
root.order.add_edge(loop_aging_sensory, choice_regulatory_feedback)

# Add dependencies within choices and loops
root.order.add_edge(choice_packaging_label, loop_aging_sensory)
root.order.add_edge(choice_customization_plan, loop_aging_sensory)
root.order.add_edge(choice_delivery_feedback, loop_aging_sensory)
root.order.add_edge(choice_regulatory_feedback, loop_aging_sensory)

# Add dependencies within loops and choices
root.order.add_edge(loop_aging_sensory, loop_aging_sensory)
root.order.add_edge(loop_aging_sensory, loop_aging_sensory)

# Add dependencies within choices
root.order.add_edge(choice_packaging_label, choice_packaging_label)
root.order.add_edge(choice_customization_plan, choice_customization_plan)
root.order.add_edge(choice_delivery_feedback, choice_delivery_feedback)
root.order.add_edge(choice_regulatory_feedback, choice_regulatory_feedback)

# Add dependencies within loops and choices
root.order.add_edge(loop_aging_sensory, choice_packaging_label)
root.order.add_edge(loop_aging_sensory, choice_customization_plan)
root.order.add_edge(loop_aging_sensory, choice_delivery_feedback)
root.order.add_edge(loop_aging_sensory, choice_regulatory_feedback)

# Add dependencies within choices and loops
root.order.add_edge(choice_packaging_label, loop_aging_sensory)
root.order.add_edge(choice_customization_plan, loop_aging_sensory)
root.order.add_edge(choice_delivery_feedback, loop_aging_sensory)
root.order.add_edge(choice_regulatory_feedback, loop_aging_sensory)

# Add dependencies within loops and choices
root.order.add_edge(loop_aging_sensory, loop_aging_sensory)
root.order.add_edge(loop_aging_sensory, loop_aging_sensory)

# Add dependencies within choices
root.order.add_edge(choice_packaging_label, choice_packaging_label)
root.order.add_edge(choice_customization_plan, choice_customization_plan)
root.order.add_edge(choice_delivery_feedback, choice_delivery_feedback)
root.order.add_edge(choice_regulatory_feedback, choice_regulatory_feedback)

# Add dependencies within loops and choices
root.order.add_edge(loop_aging_sensory, choice_packaging_label)
root.order.add_edge(loop_aging_sensory, choice_customization_plan)
root.order.add_edge(loop_aging_sensory, choice_delivery_feedback)
root.order.add_edge(loop_aging_sensory, choice_regulatory_feedback)

# Add dependencies within choices and loops
root.order.add_edge(choice_packaging_label, loop_aging_sensory)
root.order.add_edge(choice_customization_plan, loop_aging_sensory)
root.order.add_edge(choice_delivery_feedback, loop_aging_sensory)
root.order.add_edge(choice_regulatory_feedback, loop_aging_sensory)

# Add dependencies within loops and choices
root.order.add_edge(loop_aging_sensory, loop_aging_sensory)
root.order.add_edge(loop_aging_sensory, loop_aging_sensory)

# Add dependencies within choices
root.order.add_edge(choice_packaging_label, choice_packaging_label)
root.order.add_edge(choice_customization_plan, choice_customization_plan)
root.order.add_edge(choice_delivery_feedback, choice_delivery_feedback)
root.order.add_edge(choice_regulatory_feedback, choice_regulatory_feedback)

# Add dependencies within loops and choices
root.order.add_edge(loop_aging_sensory, choice_packaging_label)
root.order.add_edge(loop_aging_sensory, choice_customization_plan)
root.order.add_edge(loop_aging_sensory, choice_delivery_feedback)
root.order.add_edge(loop_aging_sensory, choice_regulatory_feedback)

# Add dependencies within choices and loops
root.order.add_edge(choice_packaging_label, loop_aging_sensory)
root.order.add_edge(choice_customization_plan, loop_aging_sensory)
root.order.add_edge(choice_delivery_feedback, loop_aging_sensory)
root.order.add_edge(choice_regulatory_feedback, loop_aging_sensory)

# Add dependencies within loops and choices
root.order.add_edge(loop_aging_sensory, loop_aging_sensory)
root.order.add_edge(loop_aging_sensory, loop_aging_sensory)

# Add dependencies within choices
root.order.add_edge(choice_packaging_label, choice_packaging_label)
root.order.add_edge(choice_customization_plan, choice_customization_plan)
root.order.add_edge(choice_delivery_feedback, choice_delivery_feedback)
root.order.add_edge(choice_regulatory_feedback, choice_regulatory_feedback)

# Add dependencies within loops and choices
root.order.add_edge(loop_aging_sensory, choice_packaging_label)
root.order.add_edge(loop_aging_sensory, choice_customization_plan)
root.order.add_edge(loop_aging_sensory, choice_delivery_feedback)
root.order.add_edge(loop_aging_sensory, choice_regulatory_feedback)

# Add dependencies within choices and loops
root.order.add_edge(choice_packaging_label, loop_aging_sensory)
root.order.add_edge(choice_customization_plan, loop_aging_sensory)
root.order.add_edge(choice_delivery_feedback, loop_aging_sensory)
root.order.add_edge(choice_regulatory_feedback, loop_aging_sensory)

# Add dependencies within loops and choices
root.order.add_edge(loop_aging_sensory, loop_aging_sensory)
root.order.add_edge(loop_aging_sensory, loop_aging_sensory)

# Add dependencies within choices
root.order.add_edge(choice_packaging_label, choice_packaging_label)
root.order.add_edge(choice_customization_plan, choice_customization_plan)
root.order.add_edge(choice_delivery_feedback, choice_delivery_feedback)
root.order.add_edge(choice_regulatory_feedback, choice_regulatory_feedback)

# Add dependencies within loops and choices
root.order.add_edge(loop_aging_sensory, choice_packaging_label)
root.order.add_edge(loop_aging_sensory, choice_customization_plan)
root.order.add_edge(loop_aging_sensory, choice_delivery_feedback)
root.order.add_edge(loop_aging_sensory, choice_regulatory_feedback)

# Add dependencies within choices and loops
root.order.add_edge(choice_packaging_label, loop_aging_sensory)
root.order.add_edge(choice_customization_plan, loop_aging_sensory)
root.order.add_edge(choice_delivery_feedback, loop_aging_sensory)
root.order.add_edge(choice_regulatory_feedback, loop_aging_sensory)

# Add dependencies within loops and choices
root.order.add_edge(loop_aging_sensory, loop_aging_sensory)
root.order.add_edge(loop_aging_sensory, loop_aging_sensory)

# Add dependencies within choices
root.order.add_edge(choice_packaging_label, choice_packaging_label)
root.order.add_edge(choice_customization_plan, choice_customization_plan)
root.order.add_edge(choice_delivery_feedback, choice_delivery_feedback)
root.order.add_edge(choice_regulatory_feedback, choice_regulatory_feedback)

# Add dependencies within loops and choices
root.order.add_edge(loop_aging_sensory, choice_packaging_label)
root.order.add_edge(loop_aging_sensory, choice_customization_plan)
root.order.add_edge(loop_aging_sensory, choice_delivery_feedback)
root.order.add_edge(loop_aging_sensory, choice_regulatory_feedback)

# Add dependencies within choices and loops
root.order.add_edge(choice_packaging_label, loop_aging_sensory)
root.order.add_edge(choice_customization_plan, loop_aging_sensory)
root.order.add_edge(choice_delivery_feedback, loop_aging_sensory)
root.order.add_edge(choice_regulatory_feedback, loop_aging_sensory)

# Add dependencies within loops and choices
root.order.add_edge(loop_aging_sensory, loop_aging_sensory)
root.order.add_edge(loop_aging_sensory, loop_aging_sensory)

# Add dependencies within choices
root.order.add_edge(choice_packaging_label, choice_packaging_label)
root.order.add_edge(choice_customization_plan, choice_customization_plan)
root.order.add_edge(choice_delivery_feedback, choice_delivery_feedback)
root.order.add_edge(choice_regulatory_feedback, choice_regulatory_feedback)

# Add dependencies within loops and choices
root.order.add_edge(loop_aging_sensory, choice_packaging_label)
root.order.add_edge(loop_aging_sensory, choice_customization_plan)
root.order.add_edge(loop_aging_sensory, choice_delivery_feedback)
root.order.add_edge(loop_aging_sensory, choice_regulatory_feedback)

# Add dependencies within choices and loops
root.order.add_edge(choice_packaging_label, loop_aging_sensory)
root.order.add_edge(choice_customization_plan, loop_aging_sensory)
root.order.add_edge(choice_delivery_feedback, loop_aging_sensory)
root.order.add_edge(choice_regulatory_feedback, loop_aging_sensory)

# Add dependencies within loops and choices
root.order.add_edge(loop_aging_sensory, loop_aging_sensory)
root.order.add_edge(loop_aging_sensory, loop_aging_sensory)

# Add dependencies within choices
root.order.add_edge(choice_packaging_label, choice_packaging_label)
root.order.add_edge(choice_customization_plan, choice_customization_plan)
root.order.add_edge(choice_delivery_feedback, choice_delivery_feedback)
root.order.add_edge(choice_regulatory_feedback, choice_regulatory_feedback)

# Add dependencies within loops and choices
root.order.add_edge(loop_aging_sensory, choice_packaging_label)
root.order.add_edge(loop_aging_sensory, choice_customization_plan)
root.order.add_edge(loop_aging_sensory, choice_delivery_feedback)
root.order.add_edge(loop_aging_sensory, choice_regulatory_feedback)

# Add dependencies within choices and loops
root.order.add_edge(choice_packaging_label, loop_aging_sensory)
root.order.add_edge(choice_customization_plan, loop_aging_sensory)
root.order.add_edge(choice_delivery_feedback, loop_aging_sensory)
root.order.add_edge(choice_regulatory_feedback, loop_aging_sensory)

# Add dependencies within loops and choices
root.order.add_edge(loop_aging_sensory, loop_aging_sensory)
root.order.add_edge(loop_aging_sensory, loop_aging_sensory)

# Add dependencies within choices
root.order.add_edge(choice_packaging_label, choice_packaging_label)
root.order.add_edge(choice_customization_plan, choice_customization_plan)
root.order.add_edge(choice_delivery_feedback, choice_delivery_feedback)
root.order.add_edge(choice_regulatory_feedback, choice_regulatory_feedback)

# Add dependencies within loops and choices
root.order.add_edge(loop_aging_sensory, choice_packaging_label)
root.order.add_edge(loop_aging_sensory, choice_customization_plan)
root.order.add_edge(loop_aging_sensory, choice_delivery_feedback)
root.order.add_edge(loop_aging_sensory, choice_regulatory_feedback)

# Add dependencies within choices and loops
root.order.add_edge(choice_packaging_label, loop_aging_sensory)
root.order.add_edge(choice_customization_plan, loop_aging