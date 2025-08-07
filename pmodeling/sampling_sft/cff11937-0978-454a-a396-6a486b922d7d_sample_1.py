import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
milk_sourcing   = Transition(label='Milk Sourcing')
quality_testing = Transition(label='Quality Testing')
starter_culture = Transition(label='Starter Culture')
milk_fermentation = Transition(label='Milk Fermentation')
curd_cutting    = Transition(label='Curd Cutting')
whey_draining   = Transition(label='Whey Draining')
pressing_cheese = Transition(label='Pressing Cheese')
cave_aging      = Transition(label='Cave Aging')
sample_tasting  = Transition(label='Sample Tasting')
flavor_profiling= Transition(label='Flavor Profiling')
packaging_design= Transition(label='Packaging Design')
cold_storage    = Transition(label='Cold Storage')
logistics_planning= Transition(label='Logistics Planning')
pop_up_sales    = Transition(label='Pop-up Sales')
customer_feedback= Transition(label='Customer Feedback')
recipe_adjusting= Transition(label='Recipe Adjusting')

# Silent transition for loop exit
skip = SilentTransition()

# Define the sampling & profiling loop:
# A = Sample Tasting -> Flavor Profiling
# B = Recipe Adjusting
sampling_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[sample_tasting, flavor_profiling]
)

# Define the packaging & logistics choice:
# A = Packaging Design -> Cold Storage
# B = Logistics Planning
packaging_choice = OperatorPOWL(
    operator=Operator.XOR,
    children=[packaging_design, cold_storage]
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
    sampling_loop,
    packaging_choice,
    pop_up_sales,
    customer_feedback,
    recipe_adjusting
])

# Sequence: Milk Sourcing -> Quality Testing -> Starter Culture -> Milk Fermentation
root.order.add_edge(milk_sourcing, quality_testing)
root.order.add_edge(quality_testing, starter_culture)
root.order.add_edge(starter_culture, milk_fermentation)

# Parallel: Curd Cutting, Whey Draining, Pressing Cheese
for t in [curd_cutting, whey_draining, pressing_cheese]:
    root.order.add_edge(milk_fermentation, t)

# After cheese production: Cave Aging -> Sampling Loop -> Packaging Choice
for t in [cave_aging, sampling_loop, packaging_choice]:
    root.order.add_edge(pressing_cheese, t)

# After packaging & logistics: Pop-up Sales -> Customer Feedback -> Recipe Adjusting
for t in [pop_up_sales, customer_feedback, recipe_adjusting]:
    root.order.add_edge(packaging_choice, t)