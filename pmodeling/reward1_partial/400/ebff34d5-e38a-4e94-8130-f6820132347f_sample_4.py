import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
milk_sourcing = Transition(label='Milk Sourcing')
quality_testing = Transition(label='Quality Testing')
starter_culture = Transition(label='Starter Culture')
milk_pasturize = Transition(label='Milk Pasteurize')
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

# Define the process flow
milk_sourcing_to_quality_testing = OperatorPOWL(operator=Operator.FORK, children=[milk_sourcing, quality_testing])
quality_testing_to_starter_culture = OperatorPOWL(operator=Operator.FORK, children=[quality_testing, starter_culture])
starter_culture_to_milk_pasturize = OperatorPOWL(operator=Operator.FORK, children=[starter_culture, milk_pasturize])
milk_pasturize_to_curd_cutting = OperatorPOWL(operator=Operator.FORK, children=[milk_pasturize, curd_cutting])
curd_cutting_to_whey_draining = OperatorPOWL(operator=Operator.FORK, children=[curd_cutting, whey_draining])
whey_draining_to_pressing_cheese = OperatorPOWL(operator=Operator.FORK, children=[whey_draining, pressing_cheese])
pressing_cheese_to_salting_stage = OperatorPOWL(operator=Operator.FORK, children=[pressing_cheese, salting_stage])
salting_stage_to_fermentation = OperatorPOWL(operator=Operator.FORK, children=[salting_stage, fermentation])
fermentation_to_aging_control = OperatorPOWL(operator=Operator.FORK, children=[fermentation, aging_control])
aging_control_to_flavor_tasting = OperatorPOWL(operator=Operator.FORK, children=[aging_control, flavor_tasting])
flavor_tasting_to_packaging_artisanal = OperatorPOWL(operator=Operator.FORK, children=[flavor_tasting, packaging_artisanal])
packaging_artisanal_to_label_printing = OperatorPOWL(operator=Operator.FORK, children=[packaging_artisanal, label_printing])
label_printing_to_order_processing = OperatorPOWL(operator=Operator.FORK, children=[label_printing, order_processing])
order_processing_to_direct_delivery = OperatorPOWL(operator=Operator.FORK, children=[order_processing, direct_delivery])
direct_delivery_to_customer_feedback = OperatorPOWL(operator=Operator.FORK, children=[direct_delivery, customer_feedback])

# Define the process tree
root = StrictPartialOrder(nodes=[
    milk_sourcing_to_quality_testing,
    quality_testing_to_starter_culture,
    starter_culture_to_milk_pasturize,
    milk_pasturize_to_curd_cutting,
    curd_cutting_to_whey_draining,
    whey_draining_to_pressing_cheese,
    pressing_cheese_to_salting_stage,
    salting_stage_to_fermentation,
    fermentation_to_aging_control,
    aging_control_to_flavor_tasting,
    flavor_tasting_to_packaging_artisanal,
    packaging_artisanal_to_label_printing,
    label_printing_to_order_processing,
    order_processing_to_direct_delivery,
    direct_delivery_to_customer_feedback
])
root.order.add_edge(milk_sourcing_to_quality_testing, quality_testing_to_starter_culture)
root.order.add_edge(quality_testing_to_starter_culture, starter_culture_to_milk_pasturize)
root.order.add_edge(starter_culture_to_milk_pasturize, milk_pasturize_to_curd_cutting)
root.order.add_edge(milk_pasturize_to_curd_cutting, curd_cutting_to_whey_draining)
root.order.add_edge(curd_cutting_to_whey_draining, whey_draining_to_pressing_cheese)
root.order.add_edge(whey_draining_to_pressing_cheese, pressing_cheese_to_salting_stage)
root.order.add_edge(pressing_cheese_to_salting_stage, salting_stage_to_fermentation)
root.order.add_edge(salting_stage_to_fermentation, fermentation_to_aging_control)
root.order.add_edge(fermentation_to_aging_control, aging_control_to_flavor_tasting)
root.order.add_edge(aging_control_to_flavor_tasting, flavor_tasting_to_packaging_artisanal)
root.order.add_edge(flavor_tasting_to_packaging_artisanal, packaging_artisanal_to_label_printing)
root.order.add_edge(packaging_artisanal_to_label_printing, label_printing_to_order_processing)
root.order.add_edge(label_printing_to_order_processing, order_processing_to_direct_delivery)
root.order.add_edge(order_processing_to_direct_delivery, direct_delivery_to_customer_feedback)

print(root)