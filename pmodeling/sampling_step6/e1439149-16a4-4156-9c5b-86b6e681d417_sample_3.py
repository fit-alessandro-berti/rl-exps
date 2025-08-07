import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
Trend_Scan = Transition(label='Trend Scan')
Idea_Harvest = Transition(label='Idea Harvest')
Workshop_Host = Transition(label='Workshop Host')
Concept_Filter = Transition(label='Concept Filter')
Prototype_Build = Transition(label='Prototype Build')
Expert_Review = Transition(label='Expert Review')
Feasibility_Check = Transition(label='Feasibility Check')
Risk_Assess = Transition(label='Risk Assess')
Pilot_Launch = Transition(label='Pilot Launch')
Data_Capture = Transition(label='Data Capture')
Performance_Review = Transition(label='Performance Review')
Scale_Plan = Transition(label='Scale Plan')
Resource_Align = Transition(label='Resource Align')
Learn_Share = Transition(label='Learn Share')
Culture_Embed = Transition(label='Culture Embed')

# Define the root process
root = StrictPartialOrder(nodes=[
    Trend_Scan,
    Idea_Harvest,
    Workshop_Host,
    Concept_Filter,
    Prototype_Build,
    Expert_Review,
    Feasibility_Check,
    Risk_Assess,
    Pilot_Launch,
    Data_Capture,
    Performance_Review,
    Scale_Plan,
    Resource_Align,
    Learn_Share,
    Culture_Embed
])

# The order of the nodes is not explicitly defined in the problem statement, so we'll assume they are concurrent.
# If there is a specific order, it should be added here.

# Print the root process
print(root)