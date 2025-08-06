import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
milk_sourcing = Transition(label='Milk Sourcing')
quality_testing = Transition(label='Quality Testing')
batch_curdling = Transition(label='Batch Curdling')
whey_removal = Transition(label='Whey Removal')
mold_inoculation = Transition(label='Mold Inoculation')
humidity_control = Transition(label='Humidity Control')
temperature_aging = Transition(label='Temperature Aging')
rind_brushing = Transition(label='Rind Brushing')
flavor_sampling = Transition(label='Flavor Sampling')
label_printing = Transition(label='Label Printing')
packaging_prep = Transition(label='Packaging Prep')
cold_storage = Transition(label='Cold Storage')
order_consolidation = Transition(label='Order Consolidation')
logistics_scheduling = Transition(label='Logistics Scheduling')
customer_feedback = Transition(label='Customer Feedback')
certification_audit = Transition(label='Certification Audit')
recipe_adjustment = Transition(label='Recipe Adjustment')

# Define the model
root = StrictPartialOrder(
    nodes=[
        milk_sourcing,
        quality_testing,
        batch_curdling,
        whey_removal,
        mold_inoculation,
        humidity_control,
        temperature_aging,
        rind_brushing,
        flavor_sampling,
        label_printing,
        packaging_prep,
        cold_storage,
        order_consolidation,
        logistics_scheduling,
        customer_feedback,
        certification_audit,
        recipe_adjustment
    ],
    order=[
        (milk_sourcing, quality_testing),
        (quality_testing, batch_curdling),
        (batch_curdling, whey_removal),
        (whey_removal, mold_inoculation),
        (mold_inoculation, humidity_control),
        (humidity_control, temperature_aging),
        (temperature_aging, rind_brushing),
        (rind_brushing, flavor_sampling),
        (flavor_sampling, label_printing),
        (label_printing, packaging_prep),
        (packaging_prep, cold_storage),
        (cold_storage, order_consolidation),
        (order_consolidation, logistics_scheduling),
        (logistics_scheduling, customer_feedback),
        (customer_feedback, certification_audit),
        (certification_audit, recipe_adjustment)
    ]
)