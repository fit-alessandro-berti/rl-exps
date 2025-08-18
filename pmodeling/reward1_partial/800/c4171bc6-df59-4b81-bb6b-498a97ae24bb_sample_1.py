from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define transitions
milk_sourcing = Transition(label='Milk Sourcing')
quality_testing = Transition(label='Quality Testing')
milk_pasturize = Transition(label='Milk Pasteurize')
curd_formation = Transition(label='Curd Formation')
whey_separation = Transition(label='Whey Separation')
press_cheese = Transition(label='Press Cheese')
salt_application = Transition(label='Salt Application')
controlled_aging = Transition(label='Controlled Aging')
sensory_check = Transition(label='Sensory Check')
batch_packaging = Transition(label='Batch Packaging')
label_printing = Transition(label='Label Printing')
cold_storage = Transition(label='Cold Storage')
logistics_plan = Transition(label='Logistics Plan')
retail_delivery = Transition(label='Retail Delivery')
feedback_review = Transition(label='Feedback Review')
demand_forecast = Transition(label='Demand Forecast')
provenance_track = Transition(label='Provenance Track')

# Define the POWL model
root = StrictPartialOrder(
    nodes=[
        milk_sourcing,
        quality_testing,
        milk_pasturize,
        curd_formation,
        whey_separation,
        press_cheese,
        salt_application,
        controlled_aging,
        sensory_check,
        batch_packaging,
        label_printing,
        cold_storage,
        logistics_plan,
        retail_delivery,
        feedback_review,
        demand_forecast,
        provenance_track
    ],
    order=[
        (milk_sourcing, quality_testing),
        (quality_testing, milk_pasturize),
        (milk_pasturize, curd_formation),
        (curd_formation, whey_separation),
        (whey_separation, press_cheese),
        (press_cheese, salt_application),
        (salt_application, controlled_aging),
        (controlled_aging, sensory_check),
        (sensory_check, batch_packaging),
        (batch_packaging, label_printing),
        (label_printing, cold_storage),
        (cold_storage, logistics_plan),
        (logistics_plan, retail_delivery),
        (retail_delivery, feedback_review),
        (feedback_review, demand_forecast),
        (demand_forecast, provenance_track)
    ]
)