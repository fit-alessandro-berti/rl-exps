import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
isolicit = Transition(label='Idea Solicitation')
afilter = Transition(label='AI Filtering')
cvoting = Transition(label='Community Voting')
ereview = Transition(label='Expert Review')
pbuild = Transition(label='Prototype Build')
utesting = Transition(label='User Testing')
iterate = Transition(label='Iterate Feedback')
risk = Transition(label='Risk Assess')
compliance = Transition(label='Compliance Check')
plaunch = Transition(label='Pilot Launch')
performance = Transition(label='Performance Track')
impact = Transition(label='Impact Analyze')
insight = Transition(label='Insight Gather')
cycle = Transition(label='Cycle Adjust')
fr = Transition(label='Final Report')

# Define the iterative testing loop: User Testing -> Iterate Feedback -> User Testing ...
# Body (B): Iterate Feedback -> User Testing
body = StrictPartialOrder(nodes=[iterate, utesting])
body.order.add_edge(iterate, utesting)

# Loop: do User Testing, then optionally do Body and repeat
loop = OperatorPOWL(operator=Operator.LOOP, children=[utesting, body])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    isolicit, afilter, cvoting, ereview, pbuild,
    loop, risk, compliance, plaunch,
    performance, impact, insight, cycle, fr
])

# Sequential edges
root.order.add_edge(isolicit, afilter)
root.order.add_edge(afilter, cvoting)
root.order.add_edge(cvoting, ereview)
root.order.add_edge(ereview, pbuild)

# After prototype build, enter the iterative testing loop
root.order.add_edge(pbuild, loop)

# After iterative testing loop, do risk, compliance, and launch
root.order.add_edge(loop, risk)
root.order.add_edge(risk, compliance)
root.order.add_edge(compliance, plaunch)

# After launch, track performance and analyze impact
root.order.add_edge(plaunch, performance)
root.order.add_edge(performance, impact)

# Finally, gather insights and adjust the cycle
root.order.add_edge(impact, insight)
root.order.add_edge(insight, cycle)

# The final report is generated at the end
root.order.add_edge(cycle, fr)