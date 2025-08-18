from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the transitions for each activity
milk_sourcing = Transition(label='Milk Sourcing')
quality_testing = Transition(label='Quality Testing')
starter_culture = Transition(label='Starter Culture')
milk_pasteurize = Transition(label='Milk Pasteurize')
curd_cutting = Transition(label='Curd Cutting')
whey_draining = Transition(label='Whey Draining')
pressing_cheese = Transition(label='Pressing Cheese')
salting_stage = Transition(label='Salting Stage')
fermentation = Transition(label='Fermentation')
aging_control = Transition(label='Aging Control')
flavor_tasting = Transition(label='Flavor Tasting')
packaging_artisanal = Transition(label='Packaging Artisanal')
label_printing = Transition(label='Label Printing')
order_processing = Transition(label='Order Processing')
direct_delivery = Transition(label='Direct Delivery')
customer_feedback = Transition(label='Customer Feedback')

# Define the partial order structure
root = StrictPartialOrder(
    nodes=[
        milk_sourcing,
        quality_testing,
        starter_culture,
        milk_pasteurize,
        curd_cutting,
        whey_draining,
        pressing_cheese,
        salting_stage,
        fermentation,
        aging_control,
        flavor_tasting,
        packaging_artisanal,
        label_printing,
        order_processing,
        direct_delivery,
        customer_feedback
    ],
    order=[
        (milk_sourcing, quality_testing),
        (quality_testing, starter_culture),
        (starter_culture, milk_pasteurize),
        (milk_pasteurize, curd_cutting),
        (curd_cutting, whey_draining),
        (whey_draining, pressing_cheese),
        (pressing_cheese, salting_stage),
        (salting_stage, fermentation),
        (fermentation, aging_control),
        (aging_control, flavor_tasting),
        (flavor_tasting, packaging_artisanal),
        (packaging_artisanal, label_printing),
        (label_printing, order_processing),
        (order_processing, direct_delivery),
        (direct_delivery, customer_feedback)
    ]
)