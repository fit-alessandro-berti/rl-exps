import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
Initial_Review = Transition(label='Initial Review')
Provenance_Check = Transition(label='Provenance Check')
Material_Test = Transition(label='Material Test')
Expert_Consult = Transition(label='Expert Consult')
Database_Search = Transition(label='Database Search')
Condition_Report = Transition(label='Condition Report')
Risk_Assess = Transition(label='Risk Assess')
Market_Analysis = Transition(label='Market Analysis')
Stakeholder_Meet = Transition(label='Stakeholder Meet')
Legal_Review = Transition(label='Legal Review')
Insurance_Quote = Transition(label='Insurance Quote')
Price_Negotiation = Transition(label='Price Negotiation')
Contract_Draft = Transition(label='Contract Draft')
Final_Approval = Transition(label='Final Approval')
Asset_Registration = Transition(label='Asset Registration')

# Define the POWL model
root = StrictPartialOrder(nodes=[
    Initial_Review,
    Provenance_Check,
    Material_Test,
    Expert_Consult,
    Database_Search,
    Condition_Report,
    Risk_Assess,
    Market_Analysis,
    Stakeholder_Meet,
    Legal_Review,
    Insurance_Quote,
    Price_Negotiation,
    Contract_Draft,
    Final_Approval,
    Asset_Registration
])

# Define dependencies between activities
root.order.add_edge(Initial_Review, Provenance_Check)
root.order.add_edge(Provenance_Check, Material_Test)
root.order.add_edge(Material_Test, Expert_Consult)
root.order.add_edge(Expert_Consult, Database_Search)
root.order.add_edge(Database_Search, Condition_Report)
root.order.add_edge(Condition_Report, Risk_Assess)
root.order.add_edge(Risk_Assess, Market_Analysis)
root.order.add_edge(Market_Analysis, Stakeholder_Meet)
root.order.add_edge(Stakeholder_Meet, Legal_Review)
root.order.add_edge(Legal_Review, Insurance_Quote)
root.order.add_edge(Insurance_Quote, Price_Negotiation)
root.order.add_edge(Price_Negotiation, Contract_Draft)
root.order.add_edge(Contract_Draft, Final_Approval)
root.order.add_edge(Final_Approval, Asset_Registration)

# The 'root' variable now contains the POWL model for the process.