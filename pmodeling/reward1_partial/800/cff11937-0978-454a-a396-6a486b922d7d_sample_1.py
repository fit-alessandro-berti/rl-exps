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

# Define transitions for quality sampling and custom packaging design
quality_sampling = OperatorPOWL(operator=Operator.LOOP, children=[quality_testing, starter_culture])
custom_packaging = OperatorPOWL(operator=Operator.LOOP, children=[packaging_design, customer_feedback])

# Define transitions for cold-chain logistics coordination
cold_chain_logistics = OperatorPOWL(operator=Operator.LOOP, children=[logistics_planning, pop_up_sales])

# Define transitions for market trend analysis and flavor adjustments
market_trend_analysis = OperatorPOWL(operator=Operator.XOR, children=[flavor_profiling, recipe_adjusting])

# Define the root POWL model
root = StrictPartialOrder(nodes=[milk_sourcing, quality_sampling, custom_packaging, cold_chain_logistics, market_trend_analysis])
root.order.add_edge(milk_sourcing, quality_sampling)
root.order.add_edge(quality_sampling, custom_packaging)
root.order.add_edge(custom_packaging, cold_chain_logistics)
root.order.add_edge(cold_chain_logistics, market_trend_analysis)

print(root)