import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
Alert_Trigger = Transition(label='Alert Trigger')
Initial_Assess = Transition(label='Initial Assess')
Stakeholder_Notify = Transition(label='Stakeholder Notify')
Resource_Check = Transition(label='Resource Check')
Risk_Analyze = Transition(label='Risk Analyze')
Command_Setup = Transition(label='Command Setup')
Deploy_Teams = Transition(label='Deploy Teams')
Data_Collect = Transition(label='Data Collect')
Situation_Update = Transition(label='Situation Update')
Priority_Adjust = Transition(label='Priority Adjust')
External_Liaison = Transition(label='External Liaison')
Supply_Dispatch = Transition(label='Supply Dispatch')
Media_Brief = Transition(label='Media Brief')
Impact_Review = Transition(label='Impact Review')
Recovery_Plan = Transition(label='Recovery Plan')
Process_Audit = Transition(label='Process Audit')

skip = SilentTransition()

# Define the POWL model
root = StrictPartialOrder(nodes=[
    Alert_Trigger,
    Initial_Assess,
    Stakeholder_Notify,
    Resource_Check,
    Risk_Analyze,
    Command_Setup,
    Deploy_Teams,
    Data_Collect,
    Situation_Update,
    Priority_Adjust,
    External_Liaison,
    Supply_Dispatch,
    Media_Brief,
    Impact_Review,
    Recovery_Plan,
    Process_Audit
])

# Define the order of activities
root.order.add_edge(Alert_Trigger, Initial_Assess)
root.order.add_edge(Initial_Assess, Stakeholder_Notify)
root.order.add_edge(Stakeholder_Notify, Resource_Check)
root.order.add_edge(Resource_Check, Risk_Analyze)
root.order.add_edge(Risk_Analyze, Command_Setup)
root.order.add_edge(Command_Setup, Deploy_Teams)
root.order.add_edge(Deploy_Teams, Data_Collect)
root.order.add_edge(Data_Collect, Situation_Update)
root.order.add_edge(Situation_Update, Priority_Adjust)
root.order.add_edge(Priority_Adjust, External_Liaison)
root.order.add_edge(External_Liaison, Supply_Dispatch)
root.order.add_edge(Supply_Dispatch, Media_Brief)
root.order.add_edge(Media_Brief, Impact_Review)
root.order.add_edge(Impact_Review, Recovery_Plan)
root.order.add_edge(Recovery_Plan, Process_Audit)