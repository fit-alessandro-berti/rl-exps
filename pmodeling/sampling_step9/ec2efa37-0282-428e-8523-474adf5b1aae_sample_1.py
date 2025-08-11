import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

Quantum_Init = Transition(label='Quantum Init')
Data_Ingest = Transition(label='Data Ingest')
AI_Forecast = Transition(label='AI Forecast')
Inventory_Sync = Transition(label='Inventory Sync')
Procurement_Plan = Transition(label='Procurement Plan')
Production_Align = Transition(label='Production Align')
Distribution_Map = Transition(label='Distribution Map')
IoT_Monitor = Transition(label='IoT Monitor')
Risk_Assess = Transition(label='Risk Assess')
Maintenance_Alert = Transition(label='Maintenance Alert')
Quantum_Compute = Transition(label='Quantum Compute')
Feedback_Loop = Transition(label='Feedback Loop')
Schedule_Adjust = Transition(label='Schedule Adjust')
Demand_Update = Transition(label='Demand Update')
Delivery_Track = Transition(label='Delivery Track')
Compliance_Check = Transition(label='Compliance Check')

skip = SilentTransition()
xor = OperatorPOWL(operator=Operator.XOR, children=[Maintenance_Alert, skip])

loop = OperatorPOWL(operator=Operator.LOOP, children=[Procurement_Plan, Production_Align])

xor2 = OperatorPOWL(operator=Operator.XOR, children=[Risk_Assess, skip])

loop2 = OperatorPOWL(operator=Operator.LOOP, children=[IoT_Monitor, Feedback_Loop])

xor3 = OperatorPOWL(operator=Operator.XOR, children=[Compliance_Check, skip])

xor4 = OperatorPOWL(operator=Operator.XOR, children=[Schedule_Adjust, skip])

xor5 = OperatorPOWL(operator=Operator.XOR, children=[Delivery_Track, skip])

root = StrictPartialOrder(nodes=[Quantum_Init, Data_Ingest, AI_Forecast, Inventory_Sync, Procurement_Plan, Production_Align, Distribution_Map, IoT_Monitor, Risk_Assess, Maintenance_Alert, Quantum_Compute, Feedback_Loop, Schedule_Adjust, Demand_Update, Delivery_Track, Compliance_Check, xor, loop, xor2, loop2, xor3, xor4, xor5])
root.order.add_edge(Quantum_Init, Data_Ingest)
root.order.add_edge(Data_Ingest, AI_Forecast)
root.order.add_edge(AI_Forecast, Inventory_Sync)
root.order.add_edge(Inventory_Sync, Procurement_Plan)
root.order.add_edge(Procurement_Plan, Production_Align)
root.order.add_edge(Production_Align, Distribution_Map)
root.order.add_edge(Distribution_Map, IoT_Monitor)
root.order.add_edge(IoT_Monitor, Risk_Assess)
root.order.add_edge(Risk_Assess, Maintenance_Alert)
root.order.add_edge(Maintenance_Alert, Quantum_Compute)
root.order.add_edge(Quantum_Compute, Feedback_Loop)
root.order.add_edge(Feedback_Loop, Schedule_Adjust)
root.order.add_edge(Schedule_Adjust, Demand_Update)
root.order.add_edge(Demand_Update, Delivery_Track)
root.order.add_edge(Delivery_Track, Compliance_Check)
root.order.add_edge(Quantum_Init, xor)
root.order.add_edge(xor, loop)
root.order.add_edge(loop, xor2)
root.order.add_edge(xor2, loop2)
root.order.add_edge(loop2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)