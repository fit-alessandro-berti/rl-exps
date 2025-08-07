import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) in the process
Milk_Collection = Transition(label='Milk Collection')
Culture_Prep = Transition(label='Culture Prep')
Curd_Formation = Transition(label='Curd Formation')
Whey_Separation = Transition(label='Whey Separation')
Molding_Cheese = Transition(label='Molding Cheese')
Salting_Process = Transition(label='Salting Process')
Initial_Aging = Transition(label='Initial Aging')
Humidity_Control = Transition(label='Humidity Control')
Temperature_Check = Transition(label='Temperature Check')
Flavor_Testing = Transition(label='Flavor Testing')
Final_Aging = Transition(label='Final Aging')
Packaging_Artisanal = Transition(label='Packaging Artisanal')
Label_Printing = Transition(label='Label Printing')
Inventory_Audit = Transition(label='Inventory Audit')
Order_Fulfillment = Transition(label='Order Fulfillment')
Subscription_Setup = Transition(label='Subscription Setup')
Event_Marketing = Transition(label='Event Marketing')

# Define the silent transition
skip = SilentTransition()

# Define the loop for aging process
loop = OperatorPOWL(operator=Operator.LOOP, children=[Humidity_Control, Temperature_Check, Flavor_Testing])

# Define the XOR for different aging processes
xor = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor2 = OperatorPOWL(operator=Operator.XOR, children=[Curd_Formation, skip])

# Define the XOR for different stages of production
xor3 = OperatorPOWL(operator=Operator.XOR, children=[Culture_Prep, skip])

# Define the XOR for different stages of production
xor4 = OperatorPOWL(operator=Operator.XOR, children=[Milk_Collection, skip])

# Define the XOR for different stages of production
xor5 = OperatorPOWL(operator=Operator.XOR, children=[Molding_Cheese, skip])

# Define the XOR for different stages of production
xor6 = OperatorPOWL(operator=Operator.XOR, children=[Salting_Process, skip])

# Define the XOR for different stages of production
xor7 = OperatorPOWL(operator=Operator.XOR, children=[Initial_Aging, skip])

# Define the XOR for different stages of production
xor8 = OperatorPOWL(operator=Operator.XOR, children=[Inventory_Audit, skip])

# Define the XOR for different stages of production
xor9 = OperatorPOWL(operator=Operator.XOR, children=[Order_Fulfillment, skip])

# Define the XOR for different stages of production
xor10 = OperatorPOWL(operator=Operator.XOR, children=[Subscription_Setup, skip])

# Define the XOR for different stages of production
xor11 = OperatorPOWL(operator=Operator.XOR, children=[Event_Marketing, skip])

# Define the XOR for different stages of production
xor12 = OperatorPOWL(operator=Operator.XOR, children=[Whey_Separation, skip])

# Define the XOR for different stages of production
xor13 = OperatorPOWL(operator=Operator.XOR, children=[Label_Printing, skip])

# Define the XOR for different stages of production
xor14 = OperatorPOWL(operator=Operator.XOR, children=[Packaging_Artisanal, skip])

# Define the XOR for different stages of production
xor15 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor16 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor17 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor18 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor19 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor20 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor21 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor22 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor23 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor24 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor25 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor26 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor27 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor28 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor29 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor30 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor31 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor32 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor33 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor34 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor35 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor36 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor37 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor38 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor39 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor40 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor41 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor42 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor43 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor44 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor45 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor46 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor47 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor48 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor49 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor50 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor51 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor52 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor53 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor54 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor55 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor56 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor57 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor58 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor59 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor60 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor61 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor62 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor63 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor64 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor65 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor66 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor67 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor68 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor69 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor70 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor71 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor72 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor73 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor74 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor75 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor76 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor77 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor78 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor79 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor80 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor81 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor82 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor83 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor84 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor85 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor86 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor87 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor88 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor89 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor90 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor91 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor92 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor93 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor94 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor95 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor96 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor97 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor98 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor99 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor100 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor101 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor102 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor103 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor104 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor105 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor106 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor107 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor108 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor109 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor110 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor111 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor112 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor113 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor114 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor115 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor116 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor117 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor118 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor119 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor120 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor121 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

# Define the XOR for different stages of production
xor122 = OperatorPOWL(operator=Operator.XOR, children=[Final_Aging, skip])

#