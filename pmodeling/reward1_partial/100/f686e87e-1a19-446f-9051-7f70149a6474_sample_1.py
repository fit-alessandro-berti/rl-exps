import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

# Define the partial order
root = StrictPartialOrder(
    nodes=[milk_sourcing, quality_testing, batch_curdling, whey_removal, mold_inoculation,
           humidity_control, temperature_aging, rind_brushing, flavor_sampling, label_printing,
           packaging_prep, cold_storage, order_consolidation, logistics_scheduling,
           customer_feedback, certification_audit, recipe_adjustment],
    order={
        milk_sourcing: {quality_testing},
        quality_testing: {batch_curdling},
        batch_curdling: {whey_removal, mold_inoculation},
        whey_removal: {humidity_control, temperature_aging},
        mold_inoculation: {humidity_control, temperature_aging},
        humidity_control: {temperature_aging},
        temperature_aging: {rind_brushing, flavor_sampling},
        rind_brushing: {label_printing},
        label_printing: {packaging_prep},
        packaging_prep: {cold_storage},
        cold_storage: {order_consolidation},
        order_consolidation: {logistics_scheduling},
        logistics_scheduling: {customer_feedback},
        customer_feedback: {certification_audit},
        certification_audit: {recipe_adjustment},
        recipe_adjustment: {milk_sourcing}
    }
)

# Add the dependency between milk_sourcing and quality_testing
root.order.add_edge(milk_sourcing, quality_testing)

# Add the dependency between batch_curdling and whey_removal and mold_inoculation
root.order.add_edge(batch_curdling, whey_removal)
root.order.add_edge(batch_curdling, mold_inoculation)

# Add the dependency between whey_removal and humidity_control and temperature_aging
root.order.add_edge(whey_removal, humidity_control)
root.order.add_edge(whey_removal, temperature_aging)

# Add the dependency between mold_inoculation and humidity_control and temperature_aging
root.order.add_edge(mold_inoculation, humidity_control)
root.order.add_edge(mold_inoculation, temperature_aging)

# Add the dependency between temperature_aging and rind_brushing and flavor_sampling
root.order.add_edge(temperature_aging, rind_brushing)
root.order.add_edge(temperature_aging, flavor_sampling)

# Add the dependency between rind_brushing and label_printing
root.order.add_edge(rind_brushing, label_printing)

# Add the dependency between label_printing and packaging_prep
root.order.add_edge(label_printing, packaging_prep)

# Add the dependency between packaging_prep and cold_storage
root.order.add_edge(packaging_prep, cold_storage)

# Add the dependency between cold_storage and order_consolidation
root.order.add_edge(cold_storage, order_consolidation)

# Add the dependency between order_consolidation and logistics_scheduling
root.order.add_edge(order_consolidation, logistics_scheduling)

# Add the dependency between logistics_scheduling and customer_feedback
root.order.add_edge(logistics_scheduling, customer_feedback)

# Add the dependency between customer_feedback and certification_audit
root.order.add_edge(customer_feedback, certification_audit)

# Add the dependency between certification_audit and recipe_adjustment
root.order.add_edge(certification_audit, recipe_adjustment)

# Add the dependency between recipe_adjustment and milk_sourcing
root.order.add_edge(recipe_adjustment, milk_sourcing)