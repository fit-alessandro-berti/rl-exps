import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

check_inventory = Transition(label='Check current inventory level')
inspect_stock = Transition(label='Inspect stock for quality')
place_order = Transition(label='Place order with suppliers')
place_stock_storage = Transition(label='Place stock in storage')
place_stock_shelves = Transition(label='Place stock on shelves')
receive_stock = Transition(label='Receive stock')
record_stock = Transition(label='Record stock in system')
manual_alert = Transition(label='Send a manual alert')
automated_alert = Transition(label='Send an automated alert')
update_inventory_levels = Transition(label='Update inventory levels')
update_inventory_system = Transition(label='Update inventory system with expected delivery dates')

# Define silent transitions for automated alerts
skip_manual_alert = SilentTransition()
skip_automated_alert = SilentTransition()

# Define loop for placing order with suppliers and updating inventory system
loop = OperatorPOWL(operator=Operator.LOOP, children=[place_order, update_inventory_system])

# Define exclusive choice for receiving stock and updating inventory system
xor = OperatorPOWL(operator=Operator.XOR, children=[receive_stock, skip_automated_alert])

# Define exclusive choice for updating inventory system and automated alert
xor2 = OperatorPOWL(operator=Operator.XOR, children=[update_inventory_system, automated_alert])

# Define exclusive choice for receiving stock and automated alert
xor3 = OperatorPOWL(operator=Operator.XOR, children=[xor, skip_manual_alert])

# Define exclusive choice for receiving stock and manual alert
xor4 = OperatorPOWL(operator=Operator.XOR, children=[xor2, manual_alert])

# Define exclusive choice for receiving stock and automated alert
xor5 = OperatorPOWL(operator=Operator.XOR, children=[xor3, skip_automated_alert])

# Define exclusive choice for receiving stock and manual alert
xor6 = OperatorPOWL(operator=Operator.XOR, children=[xor4, automated_alert])

# Define exclusive choice for receiving stock and automated alert
xor7 = OperatorPOWL(operator=Operator.XOR, children=[xor5, skip_manual_alert])

# Define exclusive choice for receiving stock and manual alert
xor8 = OperatorPOWL(operator=Operator.XOR, children=[xor6, automated_alert])

# Define exclusive choice for receiving stock and automated alert
xor9 = OperatorPOWL(operator=Operator.XOR, children=[xor7, skip_manual_alert])

# Define exclusive choice for receiving stock and manual alert
xor10 = OperatorPOWL(operator=Operator.XOR, children=[xor8, automated_alert])

# Define exclusive choice for receiving stock and automated alert
xor11 = OperatorPOWL(operator=Operator.XOR, children=[xor9, skip_manual_alert])

# Define exclusive choice for receiving stock and manual alert
xor12 = OperatorPOWL(operator=Operator.XOR, children=[xor10, automated_alert])

# Define exclusive choice for receiving stock and automated alert
xor13 = OperatorPOWL(operator=Operator.XOR, children=[xor11, skip_manual_alert])

# Define exclusive choice for receiving stock and manual alert
xor14 = OperatorPOWL(operator=Operator.XOR, children=[xor12, automated_alert])

# Define exclusive choice for receiving stock and automated alert
xor15 = OperatorPOWL(operator=Operator.XOR, children=[xor13, skip_manual_alert])

# Define exclusive choice for receiving stock and manual alert
xor16 = OperatorPOWL(operator=Operator.XOR, children=[xor14, automated_alert])

# Define exclusive choice for receiving stock and automated alert
xor17 = OperatorPOWL(operator=Operator.XOR, children=[xor15, skip_manual_alert])

# Define exclusive choice for receiving stock and manual alert
xor18 = OperatorPOWL(operator=Operator.XOR, children=[xor16, automated_alert])

# Define exclusive choice for receiving stock and automated alert
xor19 = OperatorPOWL(operator=Operator.XOR, children=[xor17, skip_manual_alert])

# Define exclusive choice for receiving stock and manual alert
xor20 = OperatorPOWL(operator=Operator.XOR, children=[xor18, automated_alert])

# Define exclusive choice for receiving stock and automated alert
xor21 = OperatorPOWL(operator=Operator.XOR, children=[xor19, skip_manual_alert])

# Define exclusive choice for receiving stock and manual alert
xor22 = OperatorPOWL(operator=Operator.XOR, children=[xor20, automated_alert])

# Define exclusive choice for receiving stock and automated alert
xor23 = OperatorPOWL(operator=Operator.XOR, children=[xor21, skip_manual_alert])

# Define exclusive choice for receiving stock and manual alert
xor24 = OperatorPOWL(operator=Operator.XOR, children=[xor22, automated_alert])

# Define exclusive choice for receiving stock and automated alert
xor25 = OperatorPOWL(operator=Operator.XOR, children=[xor23, skip_manual_alert])

# Define exclusive choice for receiving stock and manual alert
xor26 = OperatorPOWL(operator=Operator.XOR, children=[xor24, automated_alert])

# Define exclusive choice for receiving stock and automated alert
xor27 = OperatorPOWL(operator=Operator.XOR, children=[xor25, skip_manual_alert])

# Define exclusive choice for receiving stock and manual alert
xor28 = OperatorPOWL(operator=Operator.XOR, children=[xor26, automated_alert])

# Define exclusive choice for receiving stock and automated alert
xor29 = OperatorPOWL(operator=Operator.XOR, children=[xor27, skip_manual_alert])

# Define exclusive choice for receiving stock and manual alert
xor30 = OperatorPOWL(operator=Operator.XOR, children=[xor28, automated_alert])

# Define exclusive choice for receiving stock and automated alert
xor31 = OperatorPOWL(operator=Operator.XOR, children=[xor29, skip_manual_alert])

# Define exclusive choice for receiving stock and manual alert
xor32 = OperatorPOWL(operator=Operator.XOR, children=[xor30, automated_alert])

# Define exclusive choice for receiving stock and automated alert
xor33 = OperatorPOWL(operator=Operator.XOR, children=[xor31, skip_manual_alert])

# Define exclusive choice for receiving stock and manual alert
xor34 = OperatorPOWL(operator=Operator.XOR, children=[xor32, automated_alert])

# Define exclusive choice for receiving stock and automated alert
xor35 = OperatorPOWL(operator=Operator.XOR, children=[xor33, skip_manual_alert])

# Define exclusive choice for receiving stock and manual alert
xor36 = OperatorPOWL(operator=Operator.XOR, children=[xor34, automated_alert])

# Define exclusive choice for receiving stock and automated alert
xor37 = OperatorPOWL(operator=Operator.XOR, children=[xor35, skip_manual_alert])

# Define exclusive choice for receiving stock and manual alert
xor38 = OperatorPOWL(operator=Operator.XOR, children=[xor36, automated_alert])

# Define exclusive choice for receiving stock and automated alert
xor39 = OperatorPOWL(operator=Operator.XOR, children=[xor37, skip_manual_alert])

# Define exclusive choice for receiving stock and manual alert
xor40 = OperatorPOWL(operator=Operator.XOR, children=[xor38, automated_alert])

# Define exclusive choice for receiving stock and automated alert
xor41 = OperatorPOWL(operator=Operator.XOR, children=[xor39, skip_manual_alert])

# Define exclusive choice for receiving stock and manual alert
xor42 = OperatorPOWL(operator=Operator.XOR, children=[xor40, automated_alert])

# Define exclusive choice for receiving stock and automated alert
xor43 = OperatorPOWL(operator=Operator.XOR, children=[xor41, skip_manual_alert])

# Define exclusive choice for receiving stock and manual alert
xor44 = OperatorPOWL(operator=Operator.XOR, children=[xor42, automated_alert])

# Define exclusive choice for receiving stock and automated alert
xor45 = OperatorPOWL(operator=Operator.XOR, children=[xor43, skip_manual_alert])

# Define exclusive choice for receiving stock and manual alert
xor46 = OperatorPOWL(operator=Operator.XOR, children=[xor44, automated_alert])

# Define exclusive choice for receiving stock and automated alert
xor47 = OperatorPOWL(operator=Operator.XOR, children=[xor45, skip_manual_alert])

# Define exclusive choice for receiving stock and manual alert
xor48 = OperatorPOWL(operator=Operator.XOR, children=[xor46, automated_alert])

# Define exclusive choice for receiving stock and automated alert
xor49 = OperatorPOWL(operator=Operator.XOR, children=[xor47, skip_manual_alert])

# Define exclusive choice for receiving stock and manual alert
xor50 = OperatorPOWL(operator=Operator.XOR, children=[xor48, automated_alert])

# Define exclusive choice for receiving stock and automated alert
xor51 = OperatorPOWL(operator=Operator.XOR, children=[xor49, skip_manual_alert])

# Define exclusive choice for receiving stock and manual alert
xor52 = OperatorPOWL(operator=Operator.XOR, children=[xor50, automated_alert])

# Define exclusive choice for receiving stock and automated alert
xor53 = OperatorPOWL(operator=Operator.XOR, children=[xor51, skip_manual_alert])

# Define exclusive choice for receiving stock and manual alert
xor54 = OperatorPOWL(operator=Operator.XOR, children=[xor52, automated_alert])

# Define exclusive choice for receiving stock and automated alert
xor55 = OperatorPOWL(operator=Operator.XOR, children=[xor53, skip_manual_alert])

# Define exclusive choice for receiving stock and manual alert
xor56 = OperatorPOWL(operator=Operator.XOR, children=[xor54, automated_alert])

# Define exclusive choice for receiving stock and automated alert
xor57 = OperatorPOWL(operator=Operator.XOR, children=[xor55, skip_manual_alert])

# Define exclusive choice for receiving stock and manual alert
xor58 = OperatorPOWL(operator=Operator.XOR, children=[xor56, automated_alert])

# Define exclusive choice for receiving stock and automated alert
xor59 = OperatorPOWL(operator=Operator.XOR, children=[xor57, skip_manual_alert])

# Define exclusive choice for receiving stock and manual alert
xor60 = OperatorPOWL(operator=Operator.XOR, children=[xor58, automated_alert])

# Define exclusive choice for receiving stock and automated alert
xor61 = OperatorPOWL(operator=Operator.XOR, children=[xor59, skip_manual_alert])

# Define exclusive choice for receiving stock and manual alert
xor62 = OperatorPOWL(operator=Operator.XOR, children=[xor60, automated_alert])

# Define exclusive choice for receiving stock and automated alert
xor63 = OperatorPOWL(operator=Operator.XOR, children=[xor61, skip_manual_alert])

# Define exclusive choice for receiving stock and manual alert
xor64 = OperatorPOWL(operator=Operator.XOR, children=[xor62, automated_alert])

# Define exclusive choice for receiving stock and automated alert
xor65 = OperatorPOWL(operator=Operator.XOR, children=[xor63, skip_manual_alert])

# Define exclusive choice for receiving stock and manual alert
xor66 = OperatorPOWL(operator=Operator.XOR, children=[xor64, automated_alert])

# Define exclusive choice for receiving stock and automated alert
xor67 = OperatorPOWL(operator=Operator.XOR, children=[xor65, skip_manual_alert])

# Define exclusive choice for receiving stock and manual alert
xor68 = OperatorPOWL(operator=Operator.XOR, children=[xor66, automated_alert])

# Define exclusive choice for receiving stock and automated alert
xor69 = OperatorPOWL(operator=Operator.XOR, children=[xor67, skip_manual_alert])

# Define exclusive choice for receiving stock and manual alert
xor70 = OperatorPOWL(operator=Operator.XOR, children=[xor68, automated_alert])

# Define exclusive choice for receiving stock and automated alert
xor71 = OperatorPOWL(operator=Operator.XOR, children=[xor69, skip_manual_alert])

# Define exclusive choice for receiving stock and manual alert
xor72 = OperatorPOWL(operator=Operator.XOR, children=[xor70, automated_alert])

# Define exclusive choice for receiving stock and automated alert
xor73 = OperatorPOWL(operator=Operator.XOR, children=[xor71, skip_manual_alert])

# Define exclusive choice for receiving stock and manual alert
xor74 = OperatorPOWL(operator=Operator.XOR, children=[xor72, automated_alert])

# Define exclusive choice for receiving stock and automated alert
xor75 = OperatorPOWL(operator=Operator.XOR, children=[xor73, skip_manual_alert])

# Define exclusive choice for receiving stock and manual alert
xor76 = OperatorPOWL(operator=Operator.XOR, children=[xor74, automated_alert])

# Define exclusive choice for receiving stock and automated alert
xor77 = OperatorPOWL(operator=Operator.XOR, children=[xor75, skip_manual_alert])

# Define exclusive choice for receiving stock and manual alert
xor78 = OperatorPOWL(operator=Operator.XOR, children=[xor76, automated_alert])

# Define exclusive choice for receiving stock and automated alert
xor79 = OperatorPOWL(operator=Operator.XOR, children=[xor77, skip_manual_alert])

# Define exclusive choice for receiving stock and manual alert
xor80 = OperatorPOWL(operator=Operator.XOR, children=[xor78, automated_alert])

# Define exclusive choice for receiving stock and automated alert
xor81 = OperatorPOWL(operator=Operator.XOR, children=[xor79, skip_manual_alert])

# Define exclusive choice for receiving stock and manual alert
xor82 = OperatorPOWL(operator=Operator.XOR, children=[xor80, automated_alert])

# Define exclusive choice for receiving stock and automated alert
xor83 = OperatorPOWL(operator=Operator.XOR, children=[xor81, skip_manual_alert])

# Define exclusive choice for receiving stock and manual alert
xor84 = OperatorPOWL(operator=Operator.XOR, children=[xor82, automated_alert])

# Define exclusive choice for receiving stock and automated alert
xor85 = OperatorPOWL(operator=Operator.XOR, children=[xor83, skip_manual_alert])

# Define exclusive choice for receiving stock and manual alert
xor86 = OperatorPOWL(operator=Operator.XOR, children=[xor84, automated_alert])

# Define exclusive choice for receiving stock and automated alert
xor87 = OperatorPOWL(operator=Operator.XOR, children=[xor85, skip_manual_alert])

# Define exclusive choice for receiving stock and manual alert
xor88 = OperatorPOWL(operator=Operator.XOR, children=[xor86, automated_alert])

# Define exclusive choice for receiving stock and automated alert
xor89 = OperatorPOWL(operator=Operator.XOR, children=[xor87, skip_manual_alert])

# Define exclusive choice for receiving stock and manual alert
xor90 = OperatorPOWL(operator=Operator.XOR, children=[xor88, automated_alert])

# Define exclusive choice for receiving stock and automated alert
xor91 = OperatorPOWL(operator=Operator.XOR, children=[xor89, skip_manual_alert])

# Define exclusive choice for receiving stock and manual alert
xor92 = OperatorPOWL(operator=Operator.XOR, children=[xor90, automated_alert])

# Define exclusive choice for receiving stock and automated alert
xor93 = OperatorPOWL(operator=Operator.XOR, children=[xor91, skip_manual_alert])

# Define exclusive choice for receiving stock and manual alert
xor94 = OperatorPOWL(operator=Operator.XOR, children=[xor92, automated_alert])

# Define exclusive choice for receiving stock and automated alert
xor95 = OperatorPOWL(operator=Operator.XOR, children=[xor93, skip_manual_alert])

# Define exclusive choice for receiving stock and manual alert
xor96 = OperatorPOWL(operator=Operator.XOR, children=[xor94, automated_alert])

# Define exclusive choice for receiving stock and automated alert
xor97 = OperatorPOWL(operator=Operator.XOR, children=[xor95, skip_manual_alert])

# Define exclusive choice for receiving stock and manual alert
xor98 = OperatorPOWL(operator=Operator.XOR, children=[xor96, automated_alert])

# Define exclusive choice for receiving stock and automated alert
xor99 = OperatorPOWL(operator=Operator.XOR, children=[xor97, skip_manual_alert])

# Define exclusive choice for receiving stock and manual alert
xor100 = OperatorPOWL(operator=Operator.XOR, children=[xor98, automated_alert])

# Define exclusive choice for receiving stock and automated alert
xor101 = OperatorPOWL(operator=Operator.XOR, children=[xor99, skip_manual_alert])

# Define exclusive choice for receiving stock and manual alert
xor102 = OperatorPOWL(operator=Operator.XOR, children=[xor100, automated_alert])

# Define exclusive choice for receiving stock and automated alert
xor103 = OperatorPOWL(operator=Operator.XOR, children=[xor101, skip_manual_alert])

# Define exclusive choice for receiving stock and manual alert
xor104 = OperatorPOWL(operator=Operator.XOR, children=[xor102, automated_alert])

# Define exclusive choice for receiving stock and automated alert
xor105 = OperatorPOWL(operator=Operator.XOR, children=[xor103, skip_manual_alert])

# Define exclusive choice for receiving stock and manual alert
xor106 = OperatorPOWL(operator=Operator.XOR, children=[xor104, automated_alert])

# Define exclusive choice for receiving stock and automated alert
xor107 = OperatorPOWL(operator=Operator.XOR, children=[xor105, skip_manual_alert])

# Define exclusive choice for receiving stock and manual alert
xor108 = OperatorPOWL(operator=Operator.XOR, children=[xor106, automated_alert])

# Define exclusive choice for receiving stock and automated alert
xor109 = OperatorPOWL(operator=Operator.XOR, children=[xor107, skip_manual_alert])

# Define exclusive choice for receiving stock and manual alert
xor110 = OperatorPOWL(operator=Operator.XOR, children=[xor108, automated_alert])

# Define exclusive choice for receiving stock and automated alert
xor111 = OperatorPOWL(operator=Operator.XOR, children=[xor109, skip_manual_alert])

# Define exclusive choice for receiving stock and manual alert
xor112 = OperatorPOWL(operator=Operator.XOR, children=[xor110, automated_alert])

# Define exclusive choice for receiving stock and automated alert
xor113 = OperatorPOWL(operator=Operator.XOR, children=[xor111, skip_manual_alert])

# Define exclusive choice for receiving stock and manual alert
xor114 = OperatorPOWL(operator=Operator.XOR, children=[xor112, automated_alert])

# Define exclusive choice for receiving stock and automated alert
xor115 = OperatorPOWL(operator=Operator.XOR, children=[xor113, skip_manual_alert])

# Define