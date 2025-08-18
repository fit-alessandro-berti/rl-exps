import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL nodes
milk_sourcing = Transition(label='Milk Sourcing')
quality_testing = Transition(label='Quality Testing')
starter_culture = Transition(label='Starter Culture')
milk_fermentation = Transition(label='Milk Fermentation')
curd_cutting = Transition(label='Curd Cutting')
whey_draining = Transition(label='Whey Draining')
pressing_cheese = Transition(label='Pressing Cheese')
cave_aging = Transition(label='Cave Aging')
sample_tasting = Transition(label='Sample Tasting')
flavor_profiling = Transition(label='Flavor Profiling')
packaging_design = Transition(label='Packaging Design')
cold_storage = Transition(label='Cold Storage')
logistics_planning = Transition(label='Logistics Planning')
pop_up_sales = Transition(label='Pop-up Sales')
customer_feedback = Transition(label='Customer Feedback')
recipe_adjusting = Transition(label='Recipe Adjusting')

# Define the POWL operators
xor_1 = OperatorPOWL(operator=Operator.XOR, children=[starter_culture, milk_fermentation])
xor_2 = OperatorPOWL(operator=Operator.XOR, children=[curd_cutting, whey_draining])
xor_3 = OperatorPOWL(operator=Operator.XOR, children=[pressing_cheese, cave_aging])
xor_4 = OperatorPOWL(operator=Operator.XOR, children=[sample_tasting, flavor_profiling])
xor_5 = OperatorPOWL(operator=Operator.XOR, children=[packaging_design, cold_storage])
xor_6 = OperatorPOWL(operator=Operator.XOR, children=[logistics_planning, pop_up_sales])
xor_7 = OperatorPOWL(operator=Operator.XOR, children=[customer_feedback, recipe_adjusting])

# Define the POWL partial order
root = StrictPartialOrder(nodes=[milk_sourcing, quality_testing, xor_1, xor_2, xor_3, xor_4, xor_5, xor_6, xor_7])
root.order.add_edge(milk_sourcing, quality_testing)
root.order.add_edge(quality_testing, xor_1)
root.order.add_edge(xor_1, starter_culture)
root.order.add_edge(xor_1, milk_fermentation)
root.order.add_edge(milk_fermentation, xor_2)
root.order.add_edge(xor_2, curd_cutting)
root.order.add_edge(xor_2, whey_draining)
root.order.add_edge(whey_draining, xor_3)
root.order.add_edge(xor_3, pressing_cheese)
root.order.add_edge(xor_3, cave_aging)
root.order.add_edge(cave_aging, xor_4)
root.order.add_edge(xor_4, sample_tasting)
root.order.add_edge(xor_4, flavor_profiling)
root.order.add_edge(flavor_profiling, xor_5)
root.order.add_edge(xor_5, packaging_design)
root.order.add_edge(xor_5, cold_storage)
root.order.add_edge(cold_storage, xor_6)
root.order.add_edge(xor_6, logistics_planning)
root.order.add_edge(xor_6, pop_up_sales)
root.order.add_edge(pop_up_sales, xor_7)
root.order.add_edge(xor_7, customer_feedback)
root.order.add_edge(xor_7, recipe_adjusting)

# Print the root of the POWL model
print(root)