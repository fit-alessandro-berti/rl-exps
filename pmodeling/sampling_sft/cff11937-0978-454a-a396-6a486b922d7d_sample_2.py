import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
milk_sourcing     = Transition(label='Milk Sourcing')
quality_testing   = Transition(label='Quality Testing')
starter_culture   = Transition(label='Starter Culture')
milk_fermentation = Transition(label='Milk Fermentation')
curd_cutting      = Transition(label='Curd Cutting')
whey_draining     = Transition(label='Whey Draining')
pressing_cheese   = Transition(label='Pressing Cheese')
cave_aging        = Transition(label='Cave Aging')
sample_tasting    = Transition(label='Sample Tasting')
flavor_profiling  = Transition(label='Flavor Profiling')
packaging_design  = Transition(label='Packaging Design')
cold_storage      = Transition(label='Cold Storage')
logistics_planning= Transition(label='Logistics Planning')
pop_up_sales      = Transition(label='Pop-up Sales')
customer_feedback = Transition(label='Customer Feedback')
recipe_adjusting  = Transition(label='Recipe Adjusting')

# Loop for continuous quality and flavor profiling
quality_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[sample_tasting, flavor_profiling]
)

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    milk_sourcing,
    quality_testing,
    starter_culture,
    milk_fermentation,
    curd_cutting,
    whey_draining,
    pressing_cheese,
    cave_aging,
    quality_loop,
    packaging_design,
    cold_storage,
    logistics_planning,
    pop_up_sales,
    customer_feedback,
    recipe_adjusting
])

# Define the control-flow dependencies
root.order.add_edge(milk_sourcing, quality_testing)
root.order.add_edge(quality_testing, starter_culture)
root.order.add_edge(starter_culture, milk_fermentation)
root.order.add_edge(milk_fermentation, curd_cutting)
root.order.add_edge(curd_cutting, whey_draining)
root.order.add_edge(whey_draining, pressing_cheese)
root.order.add_edge(pressing_cheese, cave_aging)
root.order.add_edge(cave_aging, quality_loop)
root.order.add_edge(quality_loop, packaging_design)
root.order.add_edge(packaging_design, cold_storage)
root.order.add_edge(cold_storage, logistics_planning)
root.order.add_edge(logistics_planning, pop_up_sales)
root.order.add_edge(pop_up_sales, customer_feedback)
root.order.add_edge(customer_feedback, recipe_adjusting)
root.order.add_edge(recipe_adjusting, quality_testing)  # recipe adjustments feed back into quality checks

# Finalize the loop edge
root.order.add_edge(quality_loop, quality_loop)

# Print the model (optional, for verification)
print(root)