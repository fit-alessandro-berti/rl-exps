import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
brand_audit = Transition(label='Brand Audit')
equity_review = Transition(label='Equity Review')
market_analysis = Transition(label='Market Analysis')
legal_clearance = Transition(label='Legal Clearance')
trademark_check = Transition(label='Trademark Check')
portfolio_merge = Transition(label='Portfolio Merge')
customer_sync = Transition(label='Customer Sync')
cultural_align = Transition(label='Cultural Align')
internal_brief = Transition(label='Internal Brief')
campaign_design = Transition(label='Campaign Design')
resource_plan = Transition(label='Resource Plan')
stakeholder_meet = Transition(label='Stakeholder Meet')
launch_prep = Transition(label='Launch Prep')
feedback_loop = Transition(label='Feedback Loop')
performance_track = Transition(label='Performance Track')

# Define the silent transitions
skip = SilentTransition()

# Define the structure of the process
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[equity_review, market_analysis])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[legal_clearance, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[trademark_check, skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[portfolio_merge, skip])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[customer_sync, skip])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[cultural_align, skip])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[internal_brief, skip])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[campaign_design, skip])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[resource_plan, skip])
xor9 = OperatorPOWL(operator=Operator.XOR, children=[stakeholder_meet, skip])
xor10 = OperatorPOWL(operator=Operator.XOR, children=[launch_prep, skip])
xor11 = OperatorPOWL(operator=Operator.XOR, children=[feedback_loop, skip])
xor12 = OperatorPOWL(operator=Operator.XOR, children=[performance_track, skip])

root = StrictPartialOrder(nodes=[loop1, xor1, xor2, xor3, xor4, xor5, xor6, xor7, xor8, xor9, xor10, xor11, xor12])
root.order.add_edge(loop1, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, xor8)
root.order.add_edge(xor8, xor9)
root.order.add_edge(xor9, xor10)
root.order.add_edge(xor10, xor11)
root.order.add_edge(xor11, xor12)

# Print the root model
print(root)