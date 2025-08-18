import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with their exact names
Site_Survey = Transition(label='Site Survey')
Fleet_Design = Transition(label='Fleet Design')
Permit_Request = Transition(label='Permit Request')
Regulation_Review = Transition(label='Regulation Review')
Stakeholder_Meet = Transition(label='Stakeholder Meet')
Route_Mapping = Transition(label='Route Mapping')
Traffic_Sync = Transition(label='Traffic Sync')
Drone_Assembly = Transition(label='Drone Assembly')
Software_Setup = Transition(label='Software Setup')
Test_Flight = Transition(label='Test Flight')
Data_Integration = Transition(label='Data Integration')
Compliance_Audit = Transition(label='Compliance Audit')
Emergency_Plan = Transition(label='Emergency Plan')
Launch_Prep = Transition(label='Launch Prep')
Feedback_Loop = Transition(label='Feedback Loop')
Performance_Tune = Transition(label='Performance Tune')
Scale_Strategy = Transition(label='Scale Strategy')

# Define the partial order
root = StrictPartialOrder(nodes=[
    Site_Survey, Fleet_Design, Permit_Request, Regulation_Review, Stakeholder_Meet,
    Route_Mapping, Traffic_Sync, Drone_Assembly, Software_Setup, Test_Flight, Data_Integration,
    Compliance_Audit, Emergency_Plan, Launch_Prep, Feedback_Loop, Performance_Tune, Scale_Strategy
])

# Define the dependencies (order) between the transitions
root.order.add_edge(Site_Survey, Fleet_Design)
root.order.add_edge(Fleet_Design, Permit_Request)
root.order.add_edge(Permit_Request, Regulation_Review)
root.order.add_edge(Regulation_Review, Stakeholder_Meet)
root.order.add_edge(Stakeholder_Meet, Route_Mapping)
root.order.add_edge(Route_Mapping, Traffic_Sync)
root.order.add_edge(Traffic_Sync, Drone_Assembly)
root.order.add_edge(Drone_Assembly, Software_Setup)
root.order.add_edge(Software_Setup, Test_Flight)
root.order.add_edge(Test_Flight, Data_Integration)
root.order.add_edge(Data_Integration, Compliance_Audit)
root.order.add_edge(Compliance_Audit, Emergency_Plan)
root.order.add_edge(Emergency_Plan, Launch_Prep)
root.order.add_edge(Launch_Prep, Feedback_Loop)
root.order.add_edge(Feedback_Loop, Performance_Tune)
root.order.add_edge(Performance_Tune, Scale_Strategy)

# Print the final result
print(root)