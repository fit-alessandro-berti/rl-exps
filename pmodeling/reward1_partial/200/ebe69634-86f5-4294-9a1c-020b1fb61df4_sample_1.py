import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
Client_Intake = Transition(label='Client Intake')
Needs_Analysis = Transition(label='Needs Analysis')
Developer_Match = Transition(label='Developer Match')
Expert_Vetting = Transition(label='Expert Vetting')
Prototype_Build = Transition(label='Prototype Build')
Feedback_Loop = Transition(label='Feedback Loop')
Model_Refinement = Transition(label='Model Refinement')
License_Draft = Transition(label='License Draft')
IP_Negotiation = Transition(label='IP Negotiation')
Contract_Sign = Transition(label='Contract Sign')
Deployment_Prep = Transition(label='Deployment Prep')
Go_Live = Transition(label='Go Live')
Monitor_Model = Transition(label='Monitor Model')
Optimize_AI = Transition(label='Optimize AI')
Support_Handoff = Transition(label='Support Handoff')
Compliance_Check = Transition(label='Compliance Check')
Final_Review = Transition(label='Final Review')

# Define the partial order
root = StrictPartialOrder(nodes=[Client_Intake, Needs_Analysis, Developer_Match, Expert_Vetting, Prototype_Build, Feedback_Loop, Model_Refinement, License_Draft, IP_Negotiation, Contract_Sign, Deployment_Prep, Go_Live, Monitor_Model, Optimize_AI, Support_Handoff, Compliance_Check, Final_Review])

# Define the order between nodes
root.order.add_edge(Client_Intake, Needs_Analysis)
root.order.add_edge(Needs_Analysis, Developer_Match)
root.order.add_edge(Developer_Match, Expert_Vetting)
root.order.add_edge(Expert_Vetting, Prototype_Build)
root.order.add_edge(Prototype_Build, Feedback_Loop)
root.order.add_edge(Feedback_Loop, Model_Refinement)
root.order.add_edge(Model_Refinement, License_Draft)
root.order.add_edge(License_Draft, IP_Negotiation)
root.order.add_edge(IP_Negotiation, Contract_Sign)
root.order.add_edge(Contract_Sign, Deployment_Prep)
root.order.add_edge(Deployment_Prep, Go_Live)
root.order.add_edge(Go_Live, Monitor_Model)
root.order.add_edge(Monitor_Model, Optimize_AI)
root.order.add_edge(Optimize_AI, Support_Handoff)
root.order.add_edge(Support_Handoff, Compliance_Check)
root.order.add_edge(Compliance_Check, Final_Review)