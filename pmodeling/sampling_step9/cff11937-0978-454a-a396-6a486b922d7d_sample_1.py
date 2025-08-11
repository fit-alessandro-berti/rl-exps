import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
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

# Define silent transitions
skip = SilentTransition()

# Define the loop node
cave_aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[milk_sourcing, quality_testing, starter_culture, milk_fermentation, curd_cutting, whey_draining, pressing_cheese, cave_aging, sample_tasting, flavor_profiling, packaging_design, cold_storage, logistics_planning, pop_up_sales, customer_feedback, recipe_adjusting])

# Define the choice of other POWL models
pop_up_sales_choice = OperatorPOWL(operator=Operator.XOR, children=[pop_up_sales, skip])

# Define the root
root = StrictPartialOrder(nodes=[cave_aging_loop, pop_up_sales_choice])
root.order.add_edge(cave_aging_loop, pop_up_sales_choice)

# Print the root
print(root)