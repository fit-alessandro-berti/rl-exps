import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define the root POWL model
root = StrictPartialOrder(nodes=[
    milk_sourcing, quality_testing, starter_culture, milk_fermentation, curd_cutting,
    whey_draining, pressing_cheese, cave_aging, sample_tasting, flavor_profiling,
    packaging_design, cold_storage, logistics_planning, pop_up_sales, customer_feedback,
    recipe_adjusting
])

# Since there are no explicit dependencies in the description provided, we assume that all activities are concurrent
# If there are dependencies, they would be added to the 'root.order' attribute accordingly

# The 'root' variable now holds the POWL model for the process