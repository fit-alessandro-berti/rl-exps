import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator
# Define the activities
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

# Define the control flow operators
xor = OperatorPOWL(operator=Operator.XOR, children=[recipe_adjusting, SilentTransition()])
loop = OperatorPOWL(operator=Operator.LOOP, children=[cave_aging])
partial_order = StrictPartialOrder(nodes=[milk_sourcing, quality_testing, starter_culture, milk_fermentation, curd_cutting, whey_draining, pressing_cheese, loop, sample_tasting, flavor_profiling, packaging_design, cold_storage, logistics_planning, pop_up_sales, customer_feedback, xor])
partial_order.order.add_edge(milk_sourcing, quality_testing)
partial_order.order.add_edge(quality_testing, starter_culture)
partial_order.order.add_edge(starter_culture, milk_fermentation)
partial_order.order.add_edge(milk_fermentation, curd_cutting)
partial_order.order.add_edge(curd_cutting, whey_draining)
partial_order.order.add_edge(whey_draining, pressing_cheese)
partial_order.order.add_edge(pressing_cheese, loop)
partial_order.order.add_edge(loop, sample_tasting)
partial_order.order.add_edge(sample_tasting, flavor_profiling)
partial_order.order.add_edge(flavor_profiling, packaging_design)
partial_order.order.add_edge(packaging_design, cold_storage)
partial_order.order.add_edge(cold_storage, logistics_planning)
partial_order.order.add_edge(logistics_planning, pop_up_sales)
partial_order.order.add_edge(pop_up_sales, customer_feedback)
partial_order.order.add_edge(customer_feedback, recipe_adjusting)
partial_order.order.add_edge(recipe_adjusting, xor)

# Set the root
root = partial_order