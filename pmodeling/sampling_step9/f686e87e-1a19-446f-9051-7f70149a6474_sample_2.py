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

skip = SilentTransition()

# Define the loops
milk_sourcing_loop = OperatorPOWL(operator=Operator.LOOP, children=[milk_sourcing, quality_testing])
quality_testing_loop = OperatorPOWL(operator=Operator.LOOP, children=[quality_testing, milk_sourcing])

# Define the exclusive choices
curdling_choice = OperatorPOWL(operator=Operator.XOR, children=[batch_curdling, skip])
aging_choice = OperatorPOWL(operator=Operator.XOR, children=[humidity_control, temperature_aging])
rind_brushing_choice = OperatorPOWL(operator=Operator.XOR, children=[rind_brushing, skip])
flavor_sampling_choice = OperatorPOWL(operator=Operator.XOR, children=[flavor_sampling, skip])
label_printing_choice = OperatorPOWL(operator=Operator.XOR, children=[label_printing, skip])
packaging_prep_choice = OperatorPOWL(operator=Operator.XOR, children=[packaging_prep, skip])
cold_storage_choice = OperatorPOWL(operator=Operator.XOR, children=[cold_storage, skip])
order_consolidation_choice = OperatorPOWL(operator=Operator.XOR, children=[order_consolidation, skip])
logistics_scheduling_choice = OperatorPOWL(operator=Operator.XOR, children=[logistics_scheduling, skip])
customer_feedback_choice = OperatorPOWL(operator=Operator.XOR, children=[customer_feedback, skip])
certification_audit_choice = OperatorPOWL(operator=Operator.XOR, children=[certification_audit, skip])
recipe_adjustment_choice = OperatorPOWL(operator=Operator.XOR, children=[recipe_adjustment, skip])

# Define the POWL model root
root = StrictPartialOrder(nodes=[milk_sourcing_loop, quality_testing_loop, curdling_choice, aging_choice, rind_brushing_choice, flavor_sampling_choice, label_printing_choice, packaging_prep_choice, cold_storage_choice, order_consolidation_choice, logistics_scheduling_choice, customer_feedback_choice, certification_audit_choice, recipe_adjustment_choice])
root.order.add_edge(milk_sourcing_loop, quality_testing_loop)
root.order.add_edge(quality_testing_loop, milk_sourcing_loop)
root.order.add_edge(milk_sourcing_loop, curdling_choice)
root.order.add_edge(quality_testing_loop, aging_choice)
root.order.add_edge(curdling_choice, rind_brushing_choice)
root.order.add_edge(aging_choice, flavor_sampling_choice)
root.order.add_edge(rind_brushing_choice, label_printing_choice)
root.order.add_edge(flavor_sampling_choice, packaging_prep_choice)
root.order.add_edge(label_printing_choice, cold_storage_choice)
root.order.add_edge(packaging_prep_choice, order_consolidation_choice)
root.order.add_edge(cold_storage_choice, logistics_scheduling_choice)
root.order.add_edge(order_consolidation_choice, customer_feedback_choice)
root.order.add_edge(logistics_scheduling_choice, certification_audit_choice)
root.order.add_edge(customer_feedback_choice, recipe_adjustment_choice)
root.order.add_edge(certification_audit_choice, recipe_adjustment_choice)