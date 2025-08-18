import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

# Define the POWL model
milk_processing = OperatorPOWL(operator=Operator.LOOP, children=[
    milk_sourcing,
    quality_testing,
    milk_pasteurize,
    culture_inoculate,
    coagulation,
    curd_cutting,
    whey_drain,
    pressing,
    salting,
    aging_control,
    sensory_audit
])

packaging_and_distribution = OperatorPOWL(operator=Operator.LOOP, children=[
    packaging_design,
    label_approval,
    order_customization,
    logistics_plan,
    market_delivery
])

regulatory_and_feedback = OperatorPOWL(operator=Operator.LOOP, children=[
    regulatory_check,
    customer_feedback
])

root = StrictPartialOrder(nodes=[milk_processing, packaging_and_distribution, regulatory_and_feedback])
root.order.add_edge(milk_processing, packaging_and_distribution)
root.order.add_edge(packaging_and_distribution, regulatory_and_feedback)