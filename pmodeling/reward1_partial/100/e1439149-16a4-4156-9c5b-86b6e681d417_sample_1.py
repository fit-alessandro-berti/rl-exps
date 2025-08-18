import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the silent transitions
skip = SilentTransition()

# Define the operators
xor = OperatorPOWL(operator=Operator.XOR, children=[Concept_Filter, skip])
xor_2 = OperatorPOWL(operator=Operator.XOR, children=[Expert_Review, skip])
xor_3 = OperatorPOWL(operator=Operator.XOR, children=[Feasibility_Check, Risk_Assess])
xor_4 = OperatorPOWL(operator=Operator.XOR, children=[Pilot_Launch, skip])
xor_5 = OperatorPOWL(operator=Operator.XOR, children=[Data_Capture, skip])
xor_6 = OperatorPOWL(operator=Operator.XOR, children=[Performance_Review, skip])
xor_7 = OperatorPOWL(operator=Operator.XOR, children=[Scale_Plan, Resource_Align])
xor_8 = OperatorPOWL(operator=Operator.XOR, children=[Learn_Share, skip])
xor_9 = OperatorPOWL(operator=Operator.XOR, children=[Culture_Embed, skip])

# Define the partial order
root = StrictPartialOrder(nodes=[
    Trend_Scan, Idea_Harvest, Workshop_Host, xor,
    Prototype_Build, xor_2, Expert_Review, xor_3, Risk_Assess, xor_4, Pilot_Launch,
    xor_5, Data_Capture, Performance_Review, xor_6, Scale_Plan, Resource_Align, xor_7,
    Learn_Share, Culture_Embed
])

# Define the order between transitions
root.order.add_edge(Trend_Scan, Idea_Harvest)
root.order.add_edge(Idea_Harvest, Workshop_Host)
root.order.add_edge(Workshop_Host, xor)
root.order.add_edge(xor, Prototype_Build)
root.order.add_edge(Prototype_Build, xor_2)
root.order.add_edge(xor_2, Expert_Review)
root.order.add_edge(Expert_Review, xor_3)
root.order.add_edge(xor_3, Risk_Assess)
root.order.add_edge(Risk_Assess, xor_4)
root.order.add_edge(xor_4, Pilot_Launch)
root.order.add_edge(Pilot_Launch, xor_5)
root.order.add_edge(xor_5, Data_Capture)
root.order.add_edge(Data_Capture, Performance_Review)
root.order.add_edge(Performance_Review, xor_6)
root.order.add_edge(xor_6, Scale_Plan)
root.order.add_edge(Scale_Plan, Resource_Align)
root.order.add_edge(Resource_Align, xor_7)
root.order.add_edge(xor_7, Learn_Share)
root.order.add_edge(Learn_Share, Culture_Embed)