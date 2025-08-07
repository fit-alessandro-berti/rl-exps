import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
t1 = Transition(label='Scenario Setup')
t2 = Transition(label='Resource Mapping')
t3 = Transition(label='Team Briefing')
t4 = Transition(label='Tech Deployment')
t5 = Transition(label='Data Sync')
t6 = Transition(label='Comm Setup')
t7 = Transition(label='Live Monitoring')
t8 = Transition(label='Variable Adjust')
t9 = Transition(label='Incident Injection')
t10 = Transition(label='Response Tracking')
t11 = Transition(label='Interlock Check')
t12 = Transition(label='Real-time Feedback')
t13 = Transition(label='Debrief Session')
t14 = Transition(label='Outcome Analysis')
t15 = Transition(label='Report Generation')
t16 = Transition(label='Improvement Plan')

# Loop for continuous real-time monitoring and feedback
loop_body = StrictPartialOrder(nodes=[t8, t9, t10, t11, t12])
loop_body.order.add_edge(t8, t9)
loop_body.order.add_edge(t9, t10)
loop_body.order.add_edge(t10, t11)
loop_body.order.add_edge(t11, t12)

loop = OperatorPOWL(operator=Operator.LOOP, children=[t7, loop_body])

# Main partial order
root = StrictPartialOrder(nodes=[
    t1, t2, t3, t4, t5, t6,
    loop,
    t13, t14, t15, t16
])

# Control-flow dependencies
root.order.add_edge(t1, t2)
root.order.add_edge(t1, t3)
root.order.add_edge(t2, t4)
root.order.add_edge(t3, t4)
root.order.add_edge(t4, t5)
root.order.add_edge(t5, t6)
root.order.add_edge(t6, loop)
root.order.add_edge(loop, t13)
root.order.add_edge(t13, t14)
root.order.add_edge(t14, t15)
root.order.add_edge(t15, t16)