import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
InitialReview = Transition(label='Initial Review')
ProvenanceCheck = Transition(label='Provenance Check')
MaterialTest = Transition(label='Material Test')
ExpertConsult = Transition(label='Expert Consult')
DatabaseSearch = Transition(label='Database Search')
ConditionReport = Transition(label='Condition Report')
RiskAssess = Transition(label='Risk Assess')
MarketAnalysis = Transition(label='Market Analysis')
StakeholderMeet = Transition(label='Stakeholder Meet')
LegalReview = Transition(label='Legal Review')
InsuranceQuote = Transition(label='Insurance Quote')
PriceNegotiation = Transition(label='Price Negotiation')
ContractDraft = Transition(label='Contract Draft')
FinalApproval = Transition(label='Final Approval')
AssetRegistration = Transition(label='Asset Registration')

skip = SilentTransition()

loop1 = OperatorPOWL(operator=Operator.LOOP, children=[ProvenanceCheck, MaterialTest, ExpertConsult, DatabaseSearch])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[ConditionReport, RiskAssess, MarketAnalysis])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[StakeholderMeet, LegalReview, InsuranceQuote, PriceNegotiation, ContractDraft])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[FinalApproval, AssetRegistration])

xor = OperatorPOWL(operator=Operator.XOR, children=[skip, loop1])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[skip, loop2])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[skip, loop3])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[skip, loop4])

root = StrictPartialOrder(nodes=[xor, xor2, xor3, xor4])
root.order.add_edge(xor, xor2)
root.order.add_edge(xor, xor3)
root.order.add_edge(xor, xor4)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor2, xor4)
root.order.add_edge(xor3, xor4)