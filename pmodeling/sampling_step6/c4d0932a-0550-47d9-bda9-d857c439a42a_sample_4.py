import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
milk_sourcing = Transition(label='Milk Sourcing')
quality_testing = Transition(label='Quality Testing')
starter_culture = Transition(label='Starter Culture')
coagulation = Transition(label='Coagulation')
curd_cutting = Transition(label='Curd Cutting')
whey_draining = Transition(label='Whey Draining')
molding_cheese = Transition(label='Molding Cheese')
pressing_block = Transition(label='Pressing Block')
brining_bath = Transition(label='Brining Bath')
aging_control = Transition(label='Aging Control')
flavor_profiling = Transition(label='Flavor Profiling')
packaging_design = Transition(label='Packaging Design')
demand_forecast = Transition(label='Demand Forecast')
retail_outreach = Transition(label='Retail Outreach')
customer_feedback = Transition(label='Customer Feedback')

# Define the partial order model
root = StrictPartialOrder(nodes=[
    milk_sourcing, 
    quality_testing, 
    starter_culture, 
    coagulation, 
    curd_cutting, 
    whey_draining, 
    molding_cheese, 
    pressing_block, 
    brining_bath, 
    aging_control, 
    flavor_profiling, 
    packaging_design, 
    demand_forecast, 
    retail_outreach, 
    customer_feedback
])

# Define dependencies (if any, in this case, all activities are concurrent)
# Since the activities are concurrent, no explicit dependencies are needed.
# The root variable now contains the complete POWL model for the process.

# Print the root model
print(root)