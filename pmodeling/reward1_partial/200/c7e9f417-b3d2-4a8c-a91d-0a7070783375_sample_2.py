import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
Brand_Audit = Transition(label='Brand Audit')
Equity_Review = Transition(label='Equity Review')
Market_Analysis = Transition(label='Market Analysis')
Legal_Clearance = Transition(label='Legal Clearance')
Trademark_Check = Transition(label='Trademark Check')
Portfolio_Merge = Transition(label='Portfolio Merge')
Customer_Sync = Transition(label='Customer Sync')
Cultural_Align = Transition(label='Cultural Align')
Internal_Brief = Transition(label='Internal Brief')
Campaign_Design = Transition(label='Campaign Design')
Resource_Plan = Transition(label='Resource Plan')
Stakeholder_Meet = Transition(label='Stakeholder Meet')
Launch_Prep = Transition(label='Launch Prep')
Feedback_Loop = Transition(label='Feedback Loop')
Performance_Track = Transition(label='Performance Track')

# Define silent transitions for dependencies or no action
skip = SilentTransition()

# Define the partial order structure
root = StrictPartialOrder(
    nodes=[
        Brand_Audit,
        Equity_Review,
        Market_Analysis,
        Legal_Clearance,
        Trademark_Check,
        Portfolio_Merge,
        Customer_Sync,
        Cultural_Align,
        Internal_Brief,
        Campaign_Design,
        Resource_Plan,
        Stakeholder_Meet,
        Launch_Prep,
        Feedback_Loop,
        Performance_Track
    ],
    order={
        Brand_Audit: [Equity_Review],
        Equity_Review: [Market_Analysis],
        Market_Analysis: [Legal_Clearance, Trademark_Check],
        Legal_Clearance: [Portfolio_Merge],
        Trademark_Check: [Portfolio_Merge],
        Portfolio_Merge: [Customer_Sync, Cultural_Align],
        Customer_Sync: [Internal_Brief],
        Cultural_Align: [Internal_Brief],
        Internal_Brief: [Campaign_Design, Resource_Plan],
        Campaign_Design: [Stakeholder_Meet],
        Resource_Plan: [Stakeholder_Meet],
        Stakeholder_Meet: [Launch_Prep],
        Launch_Prep: [Feedback_Loop],
        Feedback_Loop: [Performance_Track]
    }
)

# Example usage: print the root
print(root)