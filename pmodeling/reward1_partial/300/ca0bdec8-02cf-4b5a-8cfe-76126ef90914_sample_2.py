from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

skip = SilentTransition()

# Define the POWL structure
loop = OperatorPOWL(operator=Operator.LOOP, children=[
    Milk_Sourcing, Quality_Testing, Culture_Prep, Milk_Pasteurize, Curd_Cutting, Whey_Draining, Molding_Cheese, Pressing_Blocks, Salting_Process, Aging_Monitoring, Flavor_Profiling, Packaging_Design, Compliance_Check, Market_Research, Direct_Shipping, Customer_Feedback, Recipe_Adjust])

xor = OperatorPOWL(operator=Operator.XOR, children=[
    skip])

root = StrictPartialOrder(nodes=[loop, xor])

# Define the dependencies
root.order.add_edge(loop, xor)

# Print the POWL model
print(root)