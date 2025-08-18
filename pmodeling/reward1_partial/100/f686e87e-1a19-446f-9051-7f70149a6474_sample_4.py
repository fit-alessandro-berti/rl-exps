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

# Define the process
# Milk Sourcing -> Quality Testing -> Batch Curdling -> Whey Removal -> Mold Inoculation
# Quality Testing -> Batch Curdling -> Whey Removal -> Mold Inoculation -> Humidity Control -> Temperature Aging -> Rind Brushing -> Flavor Sampling
# Batch Curdling -> Whey Removal -> Mold Inoculation -> Humidity Control -> Temperature Aging -> Rind Brushing -> Flavor Sampling -> Label Printing
# Whey Removal -> Mold Inoculation -> Humidity Control -> Temperature Aging -> Rind Brushing -> Flavor Sampling -> Label Printing -> Packaging Prep
# Mold Inoculation -> Humidity Control -> Temperature Aging -> Rind Brushing -> Flavor Sampling -> Label Printing -> Packaging Prep -> Cold Storage
# Humidity Control -> Temperature Aging -> Rind Brushing -> Flavor Sampling -> Label Printing -> Packaging Prep -> Cold Storage -> Order Consolidation
# Temperature Aging -> Rind Brushing -> Flavor Sampling -> Label Printing -> Packaging Prep -> Cold Storage -> Order Consolidation -> Logistics Scheduling
# Rind Brushing -> Flavor Sampling -> Label Printing -> Packaging Prep -> Cold Storage -> Order Consolidation -> Logistics Scheduling -> Customer Feedback
# Flavor Sampling -> Label Printing -> Packaging Prep -> Cold Storage -> Order Consolidation -> Logistics Scheduling -> Customer Feedback -> Certification Audit
# Label Printing -> Packaging Prep -> Cold Storage -> Order Consolidation -> Logistics Scheduling -> Customer Feedback -> Certification Audit -> Recipe Adjustment

# Define the loop nodes
milk_sourcing_loop = OperatorPOWL(operator=Operator.LOOP, children=[milk_sourcing, quality_testing, batch_curdling, whey_removal, mold_inoculation])
quality_testing_loop = OperatorPOWL(operator=Operator.LOOP, children=[quality_testing, batch_curdling, whey_removal, mold_inoculation, humidity_control, temperature_aging, rind_brushing, flavor_sampling])
batch_curdling_loop = OperatorPOWL(operator=Operator.LOOP, children=[batch_curdling, whey_removal, mold_inoculation, humidity_control, temperature_aging, rind_brushing, flavor_sampling, label_printing])
whey_removal_loop = OperatorPOWL(operator=Operator.LOOP, children=[whey_removal, mold_inoculation, humidity_control, temperature_aging, rind_brushing, flavor_sampling, label_printing, packaging_prep])
mold_inoculation_loop = OperatorPOWL(operator=Operator.LOOP, children=[mold_inoculation, humidity_control, temperature_aging, rind_brushing, flavor_sampling, label_printing, packaging_prep, cold_storage])
humidity_control_loop = OperatorPOWL(operator=Operator.LOOP, children=[humidity_control, temperature_aging, rind_brushing, flavor_sampling, label_printing, packaging_prep, cold_storage, order_consolidation])
temperature_aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[temperature_aging, rind_brushing, flavor_sampling, label_printing, packaging_prep, cold_storage, order_consolidation, logistics_scheduling])
rind_brushing_loop = OperatorPOWL(operator=Operator.LOOP, children=[rind_brushing, flavor_sampling, label_printing, packaging_prep, cold_storage, order_consolidation, logistics_scheduling, customer_feedback])
flavor_sampling_loop = OperatorPOWL(operator=Operator.LOOP, children=[flavor_sampling, label_printing, packaging_prep, cold_storage, order_consolidation, logistics_scheduling, customer_feedback, certification_audit])
label_printing_loop = OperatorPOWL(operator=Operator.LOOP, children=[label_printing, packaging_prep, cold_storage, order_consolidation, logistics_scheduling, customer_feedback, certification_audit, recipe_adjustment])

# Define the partial order
root = StrictPartialOrder(nodes=[milk_sourcing_loop, quality_testing_loop, batch_curdling_loop, whey_removal_loop, mold_inoculation_loop, humidity_control_loop, temperature_aging_loop, rind_brushing_loop, flavor_sampling_loop, label_printing_loop])
root.order.add_edge(milk_sourcing_loop, quality_testing_loop)
root.order.add_edge(quality_testing_loop, batch_curdling_loop)
root.order.add_edge(batch_curdling_loop, whey_removal_loop)
root.order.add_edge(whey_removal_loop, mold_inoculation_loop)
root.order.add_edge(mold_inoculation_loop, humidity_control_loop)
root.order.add_edge(humidity_control_loop, temperature_aging_loop)
root.order.add_edge(temperature_aging_loop, rind_brushing_loop)
root.order.add_edge(rind_brushing_loop, flavor_sampling_loop)
root.order.add_edge(flavor_sampling_loop, label_printing_loop)