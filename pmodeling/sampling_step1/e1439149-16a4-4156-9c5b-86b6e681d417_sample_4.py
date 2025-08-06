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

# Define silent transitions
skip = SilentTransition()

# Define loops and choices
workshop_loop = OperatorPOWL(operator=Operator.LOOP, children=[Workshop_Host, Concept_Filter, Prototype_Build, Expert_Review, Feasibility_Check, Risk_Assess])
risk_loop = OperatorPOWL(operator=Operator.LOOP, children=[Risk_Assess, Feasibility_Check, Pilot_Launch, Data_Capture, Performance_Review, Scale_Plan])
resource_loop = OperatorPOWL(operator=Operator.LOOP, children=[Resource_Align, Learn_Share, Culture_Embed])

# Define the root partial order
root = StrictPartialOrder(nodes=[Trend_Scan, Idea_Harvest, workshop_loop, risk_loop, resource_loop])

# Add edges to define the partial order
root.order.add_edge(Trend_Scan, Idea_Harvest)
root.order.add_edge(Idea_Harvest, workshop_loop)
root.order.add_edge(workshop_loop, risk_loop)
root.order.add_edge(risk_loop, resource_loop)
root.order.add_edge(resource_loop, risk_loop)
root.order.add_edge(resource_loop, workshop_loop)