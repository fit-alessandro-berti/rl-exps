import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the POWL model
Asset_ID = Transition(label='Asset ID')
Value_Assess = Transition(label='Value Assess')
Risk_Scan = Transition(label='Risk Scan')
Market_Review = Transition(label='Market Review')
Initial_Offer = Transition(label='Initial Offer')
Counter_Offer = Transition(label='Counter Offer')
Negotiation = Transition(label='Negotiation')
Contract_Draft = Transition(label='Contract Draft')
Legal_Review = Transition(label='Legal Review')
Digital_Sign = Transition(label='Digital Sign')
Royalty_Setup = Transition(label='Royalty Setup')
Transfer_Record = Transition(label='Transfer Record')
Compliance_Check = Transition(label='Compliance Check')
Audit_Schedule = Transition(label='Audit Schedule')
Market_Feedback = Transition(label='Market Feedback')
Strategy_Update = Transition(label='Strategy Update')

# Define the partial order
root = StrictPartialOrder(
    nodes=[
        Asset_ID,
        Value_Assess,
        Risk_Scan,
        Market_Review,
        Initial_Offer,
        Counter_Offer,
        Negotiation,
        Contract_Draft,
        Legal_Review,
        Digital_Sign,
        Royalty_Setup,
        Transfer_Record,
        Compliance_Check,
        Audit_Schedule,
        Market_Feedback,
        Strategy_Update
    ],
    order={
        Asset_ID: Value_Assess,
        Value_Assess: Risk_Scan,
        Risk_Scan: Market_Review,
        Market_Review: Initial_Offer,
        Initial_Offer: Counter_Offer,
        Counter_Offer: Negotiation,
        Negotiation: Contract_Draft,
        Contract_Draft: Legal_Review,
        Legal_Review: Digital_Sign,
        Digital_Sign: Royalty_Setup,
        Royalty_Setup: Transfer_Record,
        Transfer_Record: Compliance_Check,
        Compliance_Check: Audit_Schedule,
        Audit_Schedule: Market_Feedback,
        Market_Feedback: Strategy_Update
    }
)

# Print the root POWL model
print(root)