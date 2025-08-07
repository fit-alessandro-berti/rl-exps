import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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
skip = SilentTransition()

# Define process steps
sourcing_loop = OperatorPOWL(operator=Operator.LOOP, children=[milk_sourcing, quality_testing])
curdling_loop = OperatorPOWL(operator=Operator.LOOP, children=[batch_curdling, whey_removal, mold_inoculation])
aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[humidity_control, temperature_aging])
rind_loop = OperatorPOWL(operator=Operator.LOOP, children=[rind_brushing, flavor_sampling])
labeling_loop = OperatorPOWL(operator=Operator.LOOP, children=[label_printing, packaging_prep])
cold_storage_loop = OperatorPOWL(operator=Operator.LOOP, children=[cold_storage, order_consolidation])
logistics_loop = OperatorPOWL(operator=Operator.LOOP, children=[logistics_scheduling, customer_feedback])
certification_loop = OperatorPOWL(operator=Operator.LOOP, children=[certification_audit, recipe_adjustment])

# Define the root POWL model
root = StrictPartialOrder(nodes=[
    sourcing_loop, quality_testing, curdling_loop, whey_removal, mold_inoculation, humidity_control, 
    temperature_aging, rind_loop, rind_brushing, flavor_sampling, label_printing, packaging_prep, 
    cold_storage, order_consolidation, logistics_scheduling, customer_feedback, certification_audit, 
    recipe_adjustment])

# Add dependencies between nodes
root.order.add_edge(sourcing_loop, quality_testing)
root.order.add_edge(curdling_loop, whey_removal)
root.order.add_edge(curdling_loop, mold_inoculation)
root.order.add_edge(aging_loop, humidity_control)
root.order.add_edge(aging_loop, temperature_aging)
root.order.add_edge(rind_loop, rind_brushing)
root.order.add_edge(rind_loop, flavor_sampling)
root.order.add_edge(labeling_loop, label_printing)
root.order.add_edge(labeling_loop, packaging_prep)
root.order.add_edge(cold_storage_loop, cold_storage)
root.order.add_edge(cold_storage_loop, order_consolidation)
root.order.add_edge(logistics_loop, logistics_scheduling)
root.order.add_edge(logistics_loop, customer_feedback)
root.order.add_edge(certification_loop, certification_audit)
root.order.add_edge(certification_loop, recipe_adjustment)

# Print the POWL model
print(root)