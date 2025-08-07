import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
milk_sourcing = Transition(label='Milk Sourcing')
quality_testing = Transition(label='Quality Testing')
culture_prep = Transition(label='Culture Prep')
milk_pasteurize = Transition(label='Milk Pasteurize')
curd_cutting = Transition(label='Curd Cutting')
whey_draining = Transition(label='Whey Draining')
molding_cheese = Transition(label='Molding Cheese')
pressing_blocks = Transition(label='Pressing Blocks')
salting_process = Transition(label='Salting Process')
aging_monitoring = Transition(label='Aging Monitoring')
flavor_profiling = Transition(label='Flavor Profiling')
packaging_design = Transition(label='Packaging Design')
compliance_check = Transition(label='Compliance Check')
market_research = Transition(label='Market Research')
direct_shipping = Transition(label='Direct Shipping')
customer_feedback = Transition(label='Customer Feedback')
recipe_adjust = Transition(label='Recipe Adjust')

# Loop for seasonal and environmental adaptation
# Body A: Aging Monitoring -> Flavor Profiling -> Packaging Design
body_A = StrictPartialOrder(nodes=[aging_monitoring, flavor_profiling, packaging_design])
body_A.order.add_edge(aging_monitoring, flavor_profiling)
body_A.order.add_edge(flavor_profiling, packaging_design)

# Body B: Recipe Adjust
body_B = Transition(label='Recipe Adjust')

# LOOP(operator=LOOP, children=[A, B])
aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[body_A, body_B])

# Build the root partial order
root = StrictPartialOrder(nodes=[
    milk_sourcing,
    quality_testing,
    culture_prep,
    milk_pasteurize,
    curd_cutting,
    whey_draining,
    molding_cheese,
    pressing_blocks,
    salting_process,
    aging_loop,
    compliance_check,
    market_research,
    direct_shipping,
    customer_feedback
])

# Define the control-flow dependencies
root.order.add_edge(milk_sourcing, quality_testing)
root.order.add_edge(quality_testing, culture_prep)
root.order.add_edge(culture_prep, milk_pasteurize)
root.order.add_edge(milk_pasteurize, curd_cutting)
root.order.add_edge(curd_cutting, whey_draining)
root.order.add_edge(whey_draining, molding_cheese)
root.order.add_edge(molding_cheese, pressing_blocks)
root.order.add_edge(pressing_blocks, salting_process)
root.order.add_edge(salting_process, aging_loop)
root.order.add_edge(aging_loop, compliance_check)
root.order.add_edge(compliance_check, market_research)
root.order.add_edge(market_research, direct_shipping)
root.order.add_edge(direct_shipping, customer_feedback)

print(root)