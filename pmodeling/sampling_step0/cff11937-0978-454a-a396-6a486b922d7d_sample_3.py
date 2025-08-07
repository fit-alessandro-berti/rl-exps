import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
MilkSourcing = Transition(label='Milk Sourcing')
QualityTesting = Transition(label='Quality Testing')
StarterCulture = Transition(label='Starter Culture')
MilkFermentation = Transition(label='Milk Fermentation')
CurdCutting = Transition(label='Curd Cutting')
WheyDraining = Transition(label='Whey Draining')
PressingCheese = Transition(label='Pressing Cheese')
CaveAging = Transition(label='Cave Aging')
SampleTasting = Transition(label='Sample Tasting')
FlavorProfiling = Transition(label='Flavor Profiling')
PackagingDesign = Transition(label='Packaging Design')
ColdStorage = Transition(label='Cold Storage')
LogisticsPlanning = Transition(label='Logistics Planning')
PopUpSales = Transition(label='Pop-up Sales')
CustomerFeedback = Transition(label='Customer Feedback')
RecipeAdjusting = Transition(label='Recipe Adjusting')

# Define the silent transition for skipping activities
skip = SilentTransition()

# Define the POWL model structure
loop_cave_aging = OperatorPOWL(operator=Operator.LOOP, children=[CaveAging, skip])
loop_cold_storage = OperatorPOWL(operator=Operator.LOOP, children=[ColdStorage, skip])
loop_logistics_planning = OperatorPOWL(operator=Operator.LOOP, children=[LogisticsPlanning, skip])
loop_pop_up_sales = OperatorPOWL(operator=Operator.LOOP, children=[PopUpSales, skip])
loop_recipe_adjusting = OperatorPOWL(operator=Operator.LOOP, children=[RecipeAdjusting, skip])

xor_sample_tasting_flavor_profiling = OperatorPOWL(operator=Operator.XOR, children=[SampleTasting, FlavorProfiling])
xor_packaging_design = OperatorPOWL(operator=Operator.XOR, children=[PackagingDesign, skip])

xor_customer_feedback_recipe_adjusting = OperatorPOWL(operator=Operator.XOR, children=[CustomerFeedback, RecipeAdjusting])

root = StrictPartialOrder(nodes=[
    loop_cave_aging, loop_cold_storage, loop_logistics_planning, loop_pop_up_sales, loop_recipe_adjusting,
    xor_sample_tasting_flavor_profiling, xor_packaging_design, xor_customer_feedback_recipe_adjusting
])

root.order.add_edge(loop_cave_aging, xor_sample_tasting_flavor_profiling)
root.order.add_edge(loop_cold_storage, xor_packaging_design)
root.order.add_edge(loop_logistics_planning, loop_pop_up_sales)
root.order.add_edge(loop_pop_up_sales, xor_customer_feedback_recipe_adjusting)
root.order.add_edge(loop_recipe_adjusting, xor_customer_feedback_recipe_adjusting)

# Print the root node
print(root)