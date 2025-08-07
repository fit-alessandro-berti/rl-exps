import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the partial order
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

# Define the dependencies
root.order.add_edge(Trend_Scan, Idea_Harvest)
root.order.add_edge(Trend_Scan, Workshop_Host)
root.order.add_edge(Idea_Harvest, Concept_Filter)
root.order.add_edge(Idea_Harvest, Prototype_Build)
root.order.add_edge(Workshop_Host, Concept_Filter)
root.order.add_edge(Workshop_Host, Prototype_Build)
root.order.add_edge(Expert_Review, Feasibility_Check)
root.order.add_edge(Feasibility_Check, Risk_Assess)
root.order.add_edge(Pilot_Launch, Data_Capture)
root.order.add_edge(Pilot_Launch, Performance_Review)
root.order.add_edge(Performance_Review, Scale_Plan)
root.order.add_edge(Performance_Review, Resource_Align)
root.order.add_edge(Performance_Review, Learn_Share)
root.order.add_edge(Performance_Review, Culture_Embed)

# Save the result in the variable 'root'
print(root)