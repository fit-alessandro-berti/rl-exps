import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define loop and exclusive choice structures
milk_fermentation_loop = OperatorPOWL(operator=Operator.LOOP, children=[milk_fermentation, starter_culture])
quality_testing_loop = OperatorPOWL(operator=Operator.LOOP, children=[quality_testing, starter_culture])
aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[cave_aging, starter_culture])
sample_tasting_loop = OperatorPOWL(operator=Operator.LOOP, children=[sample_tasting, starter_culture])
flavor_profiling_loop = OperatorPOWL(operator=Operator.LOOP, children=[flavor_profiling, starter_culture])
packaging_design_loop = OperatorPOWL(operator=Operator.LOOP, children=[packaging_design, starter_culture])
cold_storage_loop = OperatorPOWL(operator=Operator.LOOP, children=[cold_storage, starter_culture])
logistics_planning_loop = OperatorPOWL(operator=Operator.LOOP, children=[logistics_planning, starter_culture])
pop_up_sales_loop = OperatorPOWL(operator=Operator.LOOP, children=[pop_up_sales, starter_culture])
customer_feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[customer_feedback, starter_culture])
recipe_adjusting_loop = OperatorPOWL(operator=Operator.LOOP, children=[recipe_adjusting, starter_culture])

# Define exclusive choices
exclusive_choice_1 = OperatorPOWL(operator=Operator.XOR, children=[milk_fermentation_loop, starter_culture])
exclusive_choice_2 = OperatorPOWL(operator=Operator.XOR, children=[quality_testing_loop, starter_culture])
exclusive_choice_3 = OperatorPOWL(operator=Operator.XOR, children=[aging_loop, starter_culture])
exclusive_choice_4 = OperatorPOWL(operator=Operator.XOR, children=[sample_tasting_loop, starter_culture])
exclusive_choice_5 = OperatorPOWL(operator=Operator.XOR, children=[flavor_profiling_loop, starter_culture])
exclusive_choice_6 = OperatorPOWL(operator=Operator.XOR, children=[packaging_design_loop, starter_culture])
exclusive_choice_7 = OperatorPOWL(operator=Operator.XOR, children=[cold_storage_loop, starter_culture])
exclusive_choice_8 = OperatorPOWL(operator=Operator.XOR, children=[logistics_planning_loop, starter_culture])
exclusive_choice_9 = OperatorPOWL(operator=Operator.XOR, children=[pop_up_sales_loop, starter_culture])
exclusive_choice_10 = OperatorPOWL(operator=Operator.XOR, children=[customer_feedback_loop, starter_culture])
exclusive_choice_11 = OperatorPOWL(operator=Operator.XOR, children=[recipe_adjusting_loop, starter_culture])

# Define root POWL model
root = StrictPartialOrder(nodes=[
    exclusive_choice_1,
    exclusive_choice_2,
    exclusive_choice_3,
    exclusive_choice_4,
    exclusive_choice_5,
    exclusive_choice_6,
    exclusive_choice_7,
    exclusive_choice_8,
    exclusive_choice_9,
    exclusive_choice_10,
    exclusive_choice_11
])

# Add edges to the root model
root.order.add_edge(exclusive_choice_1, exclusive_choice_2)
root.order.add_edge(exclusive_choice_2, exclusive_choice_3)
root.order.add_edge(exclusive_choice_3, exclusive_choice_4)
root.order.add_edge(exclusive_choice_4, exclusive_choice_5)
root.order.add_edge(exclusive_choice_5, exclusive_choice_6)
root.order.add_edge(exclusive_choice_6, exclusive_choice_7)
root.order.add_edge(exclusive_choice_7, exclusive_choice_8)
root.order.add_edge(exclusive_choice_8, exclusive_choice_9)
root.order.add_edge(exclusive_choice_9, exclusive_choice_10)
root.order.add_edge(exclusive_choice_10, exclusive_choice_11)
root.order.add_edge(exclusive_choice_11, exclusive_choice_1)

print(root)