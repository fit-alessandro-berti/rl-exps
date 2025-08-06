from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with exact names as given in the description
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

# Define the transitions that are silent (empty labels)
Skip_1 = SilentTransition()
Skip_2 = SilentTransition()
Skip_3 = SilentTransition()
Skip_4 = SilentTransition()
Skip_5 = SilentTransition()
Skip_6 = SilentTransition()
Skip_7 = SilentTransition()
Skip_8 = SilentTransition()
Skip_9 = SilentTransition()
Skip_10 = SilentTransition()
Skip_11 = SilentTransition()
Skip_12 = SilentTransition()
Skip_13 = SilentTransition()
Skip_14 = SilentTransition()

# Define the POWL model
root = StrictPartialOrder(
    nodes=[
        Trend_Scan, Idea_Harvest, Workshop_Host, Concept_Filter, Prototype_Build, Expert_Review, Feasibility_Check,
        Risk_Assess, Pilot_Launch, Data_Capture, Performance_Review, Scale_Plan, Resource_Align, Learn_Share,
        Culture_Embed, Skip_1, Skip_2, Skip_3, Skip_4, Skip_5, Skip_6, Skip_7, Skip_8, Skip_9, Skip_10, Skip_11,
        Skip_12, Skip_13, Skip_14
    ],
    order=[
        (Trend_Scan, Idea_Harvest),
        (Idea_Harvest, Workshop_Host),
        (Workshop_Host, Concept_Filter),
        (Concept_Filter, Prototype_Build),
        (Prototype_Build, Expert_Review),
        (Expert_Review, Feasibility_Check),
        (Feasibility_Check, Risk_Assess),
        (Risk_Assess, Pilot_Launch),
        (Pilot_Launch, Data_Capture),
        (Data_Capture, Performance_Review),
        (Performance_Review, Scale_Plan),
        (Scale_Plan, Resource_Align),
        (Resource_Align, Learn_Share),
        (Learn_Share, Culture_Embed)
    ]
)

# Add the loop nodes for parallel assessments
root.order.add_edge(Expert_Review, Expert_Review)
root.order.add_edge(Feasibility_Check, Feasibility_Check)
root.order.add_edge(Risk_Assess, Risk_Assess)
root.order.add_edge(Pilot_Launch, Pilot_Launch)

# Add the xor nodes for cross-functional ideation
root.order.add_edge(Idea_Harvest, Skip_1)
root.order.add_edge(Workshop_Host, Skip_2)
root.order.add_edge(Concept_Filter, Skip_3)
root.order.add_edge(Prototype_Build, Skip_4)
root.order.add_edge(Expert_Review, Skip_5)
root.order.add_edge(Feasibility_Check, Skip_6)
root.order.add_edge(Risk_Assess, Skip_7)
root.order.add_edge(Pilot_Launch, Skip_8)
root.order.add_edge(Data_Capture, Skip_9)
root.order.add_edge(Performance_Review, Skip_10)
root.order.add_edge(Scale_Plan, Skip_11)
root.order.add_edge(Resource_Align, Skip_12)
root.order.add_edge(Learn_Share, Skip_13)
root.order.add_edge(Culture_Embed, Skip_14)

# Add the loop nodes for parallel assessments
root.order.add_edge(Skip_1, Skip_1)
root.order.add_edge(Skip_2, Skip_2)
root.order.add_edge(Skip_3, Skip_3)
root.order.add_edge(Skip_4, Skip_4)
root.order.add_edge(Skip_5, Skip_5)
root.order.add_edge(Skip_6, Skip_6)
root.order.add_edge(Skip_7, Skip_7)
root.order.add_edge(Skip_8, Skip_8)
root.order.add_edge(Skip_9, Skip_9)
root.order.add_edge(Skip_10, Skip_10)
root.order.add_edge(Skip_11, Skip_11)
root.order.add_edge(Skip_12, Skip_12)
root.order.add_edge(Skip_13, Skip_13)
root.order.add_edge(Skip_14, Skip_14)