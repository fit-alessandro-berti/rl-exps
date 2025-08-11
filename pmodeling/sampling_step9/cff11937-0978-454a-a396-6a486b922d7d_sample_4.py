import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

# Define silent activities
skip = SilentTransition()

# Define the POWL model
loop_milk_fermentation = OperatorPOWL(operator=Operator.LOOP, children=[milk_fermentation, curd_cutting, whey_draining, pressing_cheese])
loop_cave_aging = OperatorPOWL(operator=Operator.LOOP, children=[cave_aging])
xor_sampling = OperatorPOWL(operator=Operator.XOR, children=[sample_tasting, flavor_profiling])
xor_packaging = OperatorPOWL(operator=Operator.XOR, children=[packaging_design, skip])
xor_logistics = OperatorPOWL(operator=Operator.XOR, children=[logistics_planning, skip])
xor_sales = OperatorPOWL(operator=Operator.XOR, children=[pop_up_sales, skip])
xor_feedback = OperatorPOWL(operator=Operator.XOR, children=[customer_feedback, skip])
xor_adjusting = OperatorPOWL(operator=Operator.XOR, children=[recipe_adjusting, skip])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[milk_sourcing, quality_testing, starter_culture, loop_milk_fermentation, loop_cave_aging, xor_sampling, xor_packaging, xor_logistics, xor_sales, xor_feedback, xor_adjusting])
root.order.add_edge(milk_sourcing, quality_testing)
root.order.add_edge(quality_testing, starter_culture)
root.order.add_edge(starter_culture, loop_milk_fermentation)
root.order.add_edge(loop_milk_fermentation, loop_cave_aging)
root.order.add_edge(loop_cave_aging, xor_sampling)
root.order.add_edge(xor_sampling, xor_packaging)
root.order.add_edge(xor_packaging, xor_logistics)
root.order.add_edge(xor_logistics, xor_sales)
root.order.add_edge(xor_sales, xor_feedback)
root.order.add_edge(xor_feedback, xor_adjusting)