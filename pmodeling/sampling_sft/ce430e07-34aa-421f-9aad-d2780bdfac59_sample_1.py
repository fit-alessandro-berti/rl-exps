import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define activities
ra = Transition(label='Risk Assess')
sa = Transition(label='Source Alternatives')
su = Transition(label='Supplier Audit')
cr = Transition(label='Contract Review')
rc = Transition(label='Regulation Check')
isv = Transition(label='Inventory Scan')
lr = Transition(label='Logistics Reroute')
cn = Transition(label='Customs Notify')
sa_alert = Transition(label='Stakeholder Alert')
da = Transition(label='Data Analyze')
cf = Transition(label='Cost Forecast')
cv = Transition(label='Compliance Verify')
sp = Transition(label='Scenario Plan')
dg = Transition(label='Decision Gate')
fl = Transition(label='Feedback Loop')
rg = Transition(label='Report Generate')
mm = Transition(label='Market Monitor')
ts = Transition(label='Team Sync')

# Build the partial order
root = StrictPartialOrder(nodes=[ra, sa, su, cr, rc, isv, lr, cn, sa_alert, da, cf, cv, sp, dg, fl, rg, mm, ts])

# Define the control-flow dependencies
# Initial setup: Assess -> Source Alternatives
root.order.add_edge(ra, sa)

# After Source Alternatives, audit and review suppliers
root.order.add_edge(sa, su)
root.order.add_edge(sa, cr)

# After both audits, perform compliance and regulation checks
root.order.add_edge(su, rc)
root.order.add_edge(cr, rc)

# After all initial tasks, scan inventory and analyze data
root.order.add_edge(su, isv)
root.order.add_edge(cr, isv)
root.order.add_edge(isv, da)

# After data analysis, generate cost forecast and compliance report
root.order.add_edge(da, cf)
root.order.add_edge(da, cv)

# After compliance, plan scenarios and make a decision
root.order.add_edge(cf, sp)
root.order.add_edge(cv, sp)
root.order.add_edge(sp, dg)

# After decision, notify stakeholders and generate feedback loop
root.order.add_edge(dg, sa_alert)
root.order.add_edge(dg, fl)

# After feedback, reroute logistics, notify customs, and monitor market
root.order.add_edge(fl, lr)
root.order.add_edge(fl, cn)
root.order.add_edge(fl, mm)

# Finally, generate a report and sync the team
root.order.add_edge(lr, rg)
root.order.add_edge(cn, rg)
root.order.add_edge(mm, rg)
root.order.add_edge(rg, ts)

# All other dependencies are implicit and concurrent