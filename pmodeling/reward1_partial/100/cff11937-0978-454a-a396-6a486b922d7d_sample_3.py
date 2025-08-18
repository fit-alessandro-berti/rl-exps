import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
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

# Define operators
xor = OperatorPOWL(operator=Operator.XOR, children=[recipe_adjusting, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[pop_up_sales, skip])
loop = OperatorPOWL(operator=Operator.LOOP, children=[cave_aging, sample_tasting])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[logistics_planning, xor2])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[quality_testing, starter_culture])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[milk_fermentation, curd_cutting])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[whey_draining, pressing_cheese])
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[packaging_design, cold_storage])
root = StrictPartialOrder(nodes=[milk_sourcing, loop3, loop4, loop5, loop6, loop2, loop, xor, xor2])
root.order.add_edge(milk_sourcing, loop3)
root.order.add_edge(loop3, loop4)
root.order.add_edge(loop4, loop5)
root.order.add_edge(loop5, loop6)
root.order.add_edge(loop6, loop2)
root.order.add_edge(loop2, xor2)
root.order.add_edge(xor2, loop)
root.order.add_edge(loop, xor)
root.order.add_edge(xor, pop_up_sales)
root.order.add_edge(pop_up_sales, customer_feedback)