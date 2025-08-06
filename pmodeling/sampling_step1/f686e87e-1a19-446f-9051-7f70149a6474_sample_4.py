import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions
skip = SilentTransition()

# Define partial order for milk sourcing and quality testing
milk_quality = StrictPartialOrder(nodes=[milk_sourcing, quality_testing])
milk_quality.order.add_edge(milk_sourcing, quality_testing)

# Define partial order for batch curdling, whey removal, mold inoculation, and humidity control
batch_control = StrictPartialOrder(nodes=[batch_curdling, whey_removal, mold_inoculation, humidity_control])
batch_control.order.add_edge(batch_curdling, whey_removal)
batch_control.order.add_edge(whey_removal, mold_inoculation)
batch_control.order.add_edge(mold_inoculation, humidity_control)

# Define partial order for temperature aging, rind brushing, and flavor sampling
aging_sampling = StrictPartialOrder(nodes=[temperature_aging, rind_brushing, flavor_sampling])
aging_sampling.order.add_edge(temperature_aging, rind_brushing)
aging_sampling.order.add_edge(rind_brushing, flavor_sampling)

# Define partial order for label printing and packaging preparation
label_prep = StrictPartialOrder(nodes=[label_printing, packaging_prep])
label_prep.order.add_edge(label_printing, packaging_prep)

# Define partial order for cold storage and order consolidation
cold_storage_consolidation = StrictPartialOrder(nodes=[cold_storage, order_consolidation])
cold_storage_consolidation.order.add_edge(cold_storage, order_consolidation)

# Define partial order for logistics scheduling and customer feedback
logistics_feedback = StrictPartialOrder(nodes=[logistics_scheduling, customer_feedback])
logistics_feedback.order.add_edge(logistics_scheduling, customer_feedback)

# Define partial order for certification audit and recipe adjustment
audit_adjustment = StrictPartialOrder(nodes=[certification_audit, recipe_adjustment])
audit_adjustment.order.add_edge(certification_audit, recipe_adjustment)

# Define partial order for the entire process
root = StrictPartialOrder(nodes=[milk_quality, batch_control, aging_sampling, label_prep, cold_storage_consolidation, logistics_feedback, audit_adjustment])
root.order.add_edge(milk_quality, batch_control)
root.order.add_edge(batch_control, aging_sampling)
root.order.add_edge(aging_sampling, label_prep)
root.order.add_edge(label_prep, cold_storage_consolidation)
root.order.add_edge(cold_storage_consolidation, logistics_feedback)
root.order.add_edge(logistics_feedback, audit_adjustment)