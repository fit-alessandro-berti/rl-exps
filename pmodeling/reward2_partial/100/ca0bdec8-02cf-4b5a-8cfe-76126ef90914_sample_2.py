import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
Milk_Sourcing = Transition(label='Milk Sourcing')
Quality_Testing = Transition(label='Quality Testing')
Culture_Prep = Transition(label='Culture Prep')
Milk_Pasteurize = Transition(label='Milk Pasteurize')
Curd_Cutting = Transition(label='Curd Cutting')
Whey_Draining = Transition(label='Whey Draining')
Molding_Cheese = Transition(label='Molding Cheese')
Pressing_Blocks = Transition(label='Pressing Blocks')
Salting_Process = Transition(label='Salting Process')
Aging_Monitoring = Transition(label='Aging Monitoring')
Flavor_Profiling = Transition(label='Flavor Profiling')
Packaging_Design = Transition(label='Packaging Design')
Compliance_Check = Transition(label='Compliance Check')
Market_Research = Transition(label='Market Research')
Direct_Shipping = Transition(label='Direct Shipping')
Customer_Feedback = Transition(label='Customer Feedback')
Recipe_Adjust = Transition(label='Recipe Adjust')

# Define the partial order
root = StrictPartialOrder(nodes=[
    Milk_Sourcing,
    Quality_Testing,
    Culture_Prep,
    Milk_Pasteurize,
    Curd_Cutting,
    Whey_Draining,
    Molding_Cheese,
    Pressing_Blocks,
    Salting_Process,
    Aging_Monitoring,
    Flavor_Profiling,
    Packaging_Design,
    Compliance_Check,
    Market_Research,
    Direct_Shipping,
    Customer_Feedback,
    Recipe_Adjust
])

# Define the order (dependencies)
root.order.add_edge(Milk_Sourcing, Quality_Testing)
root.order.add_edge(Quality_Testing, Culture_Prep)
root.order.add_edge(Culture_Prep, Milk_Pasteurize)
root.order.add_edge(Milk_Pasteurize, Curd_Cutting)
root.order.add_edge(Curd_Cutting, Whey_Draining)
root.order.add_edge(Whey_Draining, Molding_Cheese)
root.order.add_edge(Molding_Cheese, Pressing_Blocks)
root.order.add_edge(Pressing_Blocks, Salting_Process)
root.order.add_edge(Salting_Process, Aging_Monitoring)
root.order.add_edge(Aging_Monitoring, Flavor_Profiling)
root.order.add_edge(Flavor_Profiling, Packaging_Design)
root.order.add_edge(Packaging_Design, Compliance_Check)
root.order.add_edge(Compliance_Check, Market_Research)
root.order.add_edge(Market_Research, Direct_Shipping)
root.order.add_edge(Direct_Shipping, Customer_Feedback)
root.order.add_edge(Customer_Feedback, Recipe_Adjust)

# Print the final root model
print(root)