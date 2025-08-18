from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the activities
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

# Define the process model
root = StrictPartialOrder(
    nodes=[
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
        sensory_audit,
        packaging_design,
        label_approval,
        order_customization,
        logistics_plan,
        market_delivery,
        customer_feedback,
        regulatory_check
    ],
    order=[
        (milk_sourcing, quality_testing),
        (quality_testing, milk_pasteurize),
        (milk_pasteurize, culture_inoculate),
        (culture_inoculate, coagulation),
        (coagulation, curd_cutting),
        (curd_cutting, whey_drain),
        (whey_drain, pressing),
        (pressing, salting),
        (salting, aging_control),
        (aging_control, sensory_audit),
        (sensory_audit, packaging_design),
        (packaging_design, label_approval),
        (label_approval, order_customization),
        (order_customization, logistics_plan),
        (logistics_plan, market_delivery),
        (market_delivery, customer_feedback),
        (customer_feedback, regulatory_check)
    ]
)