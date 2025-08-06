import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
Site_Survey = Transition(label='Site Survey')
Climate_Plan = Transition(label='Climate Plan')
System_Design = Transition(label='System Design')
AI_Setup = Transition(label='AI Setup')
Seed_Sourcing = Transition(label='Seed Sourcing')
Nutrient_Mix = Transition(label='Nutrient Mix')
Install_Hydro = Transition(label='Install Hydro')
Energy_Audit = Transition(label='Energy Audit')
Staff_Training = Transition(label='Staff Training')
Trial_Growth = Transition(label='Trial Growth')
Yield_Measure = Transition(label='Yield Measure')
Waste_Cycle = Transition(label='Waste Cycle')
Compliance_Check = Transition(label='Compliance Check')
Market_Study = Transition(label='Market Study')
Community_Meet = Transition(label='Community Meet')
Optimize_Environment = Transition(label='Optimize Environment')

# Define the partial order
root = StrictPartialOrder(nodes=[
    Site_Survey, Climate_Plan, System_Design, AI_Setup, Seed_Sourcing, Nutrient_Mix, Install_Hydro, Energy_Audit,
    Staff_Training, Trial_Growth, Yield_Measure, Waste_Cycle, Compliance_Check, Market_Study, Community_Meet,
    Optimize_Environment
])

# Define the dependencies between activities
root.order.add_edge(Site_Survey, Climate_Plan)
root.order.add_edge(Climate_Plan, System_Design)
root.order.add_edge(System_Design, AI_Setup)
root.order.add_edge(AI_Setup, Seed_Sourcing)
root.order.add_edge(Seed_Sourcing, Nutrient_Mix)
root.order.add_edge(Nutrient_Mix, Install_Hydro)
root.order.add_edge(Install_Hydro, Energy_Audit)
root.order.add_edge(Energy_Audit, Staff_Training)
root.order.add_edge(Staff_Training, Trial_Growth)
root.order.add_edge(Trial_Growth, Yield_Measure)
root.order.add_edge(Yield_Measure, Waste_Cycle)
root.order.add_edge(Waste_Cycle, Compliance_Check)
root.order.add_edge(Compliance_Check, Market_Study)
root.order.add_edge(Market_Study, Community_Meet)
root.order.add_edge(Community_Meet, Optimize_Environment)