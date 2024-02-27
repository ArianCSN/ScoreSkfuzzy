import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import time
import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox

class CustomDialog(simpledialog.Dialog):
    def __init__(self, parent, title, prompt, default=0):
        self.prompt = prompt
        super().__init__(parent, title=title)

    def body(self, master):
        tk.Label(master, text=self.prompt).grid(row=0)
        self.entry = tk.Entry(master, width=30)
        self.entry.grid(row=1)
        return self.entry


    def apply(self):
        self.result = self.entry.get()


precision=0.1
EndTerm = ctrl.Antecedent(np.arange(0, 20.0001, precision), "EndTerm")
EndTerm["bad"] = fuzz.zmf(EndTerm.universe, 7,10)
EndTerm["normal"] = fuzz.trapmf(EndTerm.universe, [10.01, 11, 13, 14.1])
EndTerm["good"] = fuzz.trapmf(EndTerm.universe, [13.9, 15, 17, 18])
EndTerm["verygood"] = fuzz.smf(EndTerm.universe, 17.9, 18.5)
MidTerm = ctrl.Antecedent(np.arange(0, 20.0001, precision), "MidTerm")
MidTerm["bad"] = fuzz.zmf(MidTerm.universe, 7, 10)
MidTerm["normal"] = fuzz.trapmf(MidTerm.universe, [9.9, 11, 13, 14])
MidTerm["good"] = fuzz.trapmf(MidTerm.universe, [13.9, 15, 17, 18])
MidTerm["verygood"] = fuzz.smf(MidTerm.universe, 17.9, 18.5)
HomeWorks = ctrl.Antecedent(np.arange(0, 5.0001, precision), "HomeWorks")
HomeWorks["lazy"] = fuzz.zmf(HomeWorks.universe, 1.5, 2)
HomeWorks["normal"] = fuzz.trapmf(HomeWorks.universe, [1.998, 2.2, 3.5, 4])
HomeWorks["hardwork"] = fuzz.smf(HomeWorks.universe, 3.998, 4.3)
ClassActivity = ctrl.Antecedent(np.arange(0, 100.0001, precision), "ClassActivity")
ClassActivity["very lazy"] = fuzz.zmf(ClassActivity.universe, 20, 25)
ClassActivity["lazy"] = fuzz.trapmf(ClassActivity.universe, [24.9, 30, 45 , 50])
ClassActivity["normal"] = fuzz.trapmf(ClassActivity.universe, [49.9, 54 , 70, 75])
ClassActivity["hardwork"] = fuzz.smf(ClassActivity.universe, 74.9, 80)
Score = ctrl.Consequent(np.arange(0, 20.0001, precision), "Score")
Score["F"] = fuzz.zmf(Score.universe, 7, 10)
Score["D"] = fuzz.trapmf(Score.universe, [9.5, 10.4454, 13, 14])
Score["C"] = fuzz.trapmf(Score.universe, [13.5, 13.9799, 15.5, 16])
Score["B"] = fuzz.trapmf(Score.universe, [15.5, 16, 17.5, 18])
Score["A"] = fuzz.smf(Score.universe, 17.5, 18)

EndTerm.view()
MidTerm.view()
HomeWorks.view()
ClassActivity.view()
#Score.view()

rule01 = ctrl.Rule(EndTerm['bad'] & MidTerm["bad"] & HomeWorks["lazy"] & ClassActivity["very lazy"] , Score["F"])
rule02 = ctrl.Rule(EndTerm['normal'] & MidTerm["bad"] & HomeWorks["lazy"] & ClassActivity["very lazy"] , Score["F"])
rule03 = ctrl.Rule(EndTerm['good'] & MidTerm["bad"] & HomeWorks["lazy"] & ClassActivity["very lazy"] , Score["F"])
rule04 = ctrl.Rule(EndTerm['verygood'] & MidTerm["bad"] & HomeWorks["lazy"] & ClassActivity["very lazy"] , Score["F"])
rule05 = ctrl.Rule(EndTerm['bad'] & MidTerm["normal"] & HomeWorks["lazy"] & ClassActivity["very lazy"] , Score["F"])
rule06 = ctrl.Rule(EndTerm['normal'] & MidTerm["normal"] & HomeWorks["lazy"] & ClassActivity["very lazy"] , Score["F"])
rule07 = ctrl.Rule(EndTerm['good'] & MidTerm["normal"] & HomeWorks["lazy"] & ClassActivity["very lazy"] , Score["F"])
rule08 = ctrl.Rule(EndTerm['verygood'] & MidTerm["normal"] & HomeWorks["lazy"] & ClassActivity["very lazy"] , Score["D"])
rule09 = ctrl.Rule(EndTerm['bad'] & MidTerm["good"] & HomeWorks["lazy"] & ClassActivity["very lazy"] , Score["F"])
rule10 = ctrl.Rule(EndTerm['normal'] & MidTerm["good"] & HomeWorks["lazy"] & ClassActivity["very lazy"] , Score["F"])
rule11 = ctrl.Rule(EndTerm['good'] & MidTerm["good"] & HomeWorks["lazy"] & ClassActivity["very lazy"] , Score["D"])
rule12 = ctrl.Rule(EndTerm['verygood'] & MidTerm["good"] & HomeWorks["lazy"] & ClassActivity["very lazy"] , Score["D"])
rule13 = ctrl.Rule(EndTerm['bad'] & MidTerm["verygood"] & HomeWorks["lazy"] & ClassActivity["very lazy"] , Score["F"])
rule14 = ctrl.Rule(EndTerm['normal'] & MidTerm["verygood"] & HomeWorks["lazy"] & ClassActivity["very lazy"] , Score["D"])
rule15 = ctrl.Rule(EndTerm['good'] & MidTerm["verygood"] & HomeWorks["lazy"] & ClassActivity["very lazy"] , Score["D"])
rule16 = ctrl.Rule(EndTerm['verygood'] & MidTerm["verygood"] & HomeWorks["lazy"] & ClassActivity["very lazy"] , Score["C"])

rule17 = ctrl.Rule(EndTerm['bad'] & MidTerm["bad"] & HomeWorks["normal"] & ClassActivity["very lazy"] , Score["F"])
rule18 = ctrl.Rule(EndTerm['normal'] & MidTerm["bad"] & HomeWorks["normal"] & ClassActivity["very lazy"] , Score["F"])
rule19 = ctrl.Rule(EndTerm['good'] & MidTerm["bad"] & HomeWorks["normal"] & ClassActivity["very lazy"] , Score["F"])
rule20 = ctrl.Rule(EndTerm['verygood'] & MidTerm["bad"] & HomeWorks["normal"] & ClassActivity["very lazy"] , Score["D"])
rule21 = ctrl.Rule(EndTerm['bad'] & MidTerm["normal"] & HomeWorks["normal"] & ClassActivity["very lazy"] , Score["F"])
rule22 = ctrl.Rule(EndTerm['normal'] & MidTerm["normal"] & HomeWorks["normal"] & ClassActivity["very lazy"] , Score["F"])
rule23 = ctrl.Rule(EndTerm['good'] & MidTerm["normal"] & HomeWorks["normal"] & ClassActivity["very lazy"] , Score["D"])
rule24 = ctrl.Rule(EndTerm['verygood'] & MidTerm["normal"] & HomeWorks["normal"] & ClassActivity["very lazy"] , Score["D"])
rule25 = ctrl.Rule(EndTerm['bad'] & MidTerm["good"] & HomeWorks["normal"] & ClassActivity["very lazy"] , Score["F"])
rule26 = ctrl.Rule(EndTerm['normal'] & MidTerm["good"] & HomeWorks["normal"] & ClassActivity["very lazy"] , Score["D"])
rule27 = ctrl.Rule(EndTerm['good'] & MidTerm["good"] & HomeWorks["normal"] & ClassActivity["very lazy"] , Score["D"])
rule28 = ctrl.Rule(EndTerm['verygood'] & MidTerm["good"] & HomeWorks["normal"] & ClassActivity["very lazy"] , Score["C"])
rule29 = ctrl.Rule(EndTerm['bad'] & MidTerm["verygood"] & HomeWorks["normal"] & ClassActivity["very lazy"] , Score["D"])
rule30 = ctrl.Rule(EndTerm['normal'] & MidTerm["verygood"] & HomeWorks["normal"] & ClassActivity["very lazy"] , Score["D"])
rule31 = ctrl.Rule(EndTerm['good'] & MidTerm["verygood"] & HomeWorks["normal"] & ClassActivity["very lazy"] , Score["C"])
rule32 = ctrl.Rule(EndTerm['verygood'] & MidTerm["verygood"] & HomeWorks["normal"] & ClassActivity["very lazy"] , Score["C"])

rule33 = ctrl.Rule(EndTerm['bad'] & MidTerm["bad"] & HomeWorks["hardwork"] & ClassActivity["very lazy"] , Score["F"])
rule34 = ctrl.Rule(EndTerm['normal'] & MidTerm["bad"] & HomeWorks["hardwork"] & ClassActivity["very lazy"] , Score["F"])
rule35 = ctrl.Rule(EndTerm['good'] & MidTerm["bad"] & HomeWorks["hardwork"] & ClassActivity["very lazy"] , Score["D"])
rule36 = ctrl.Rule(EndTerm['verygood'] & MidTerm["bad"] & HomeWorks["hardwork"] & ClassActivity["very lazy"] , Score["D"])
rule37 = ctrl.Rule(EndTerm['bad'] & MidTerm["normal"] & HomeWorks["hardwork"] & ClassActivity["very lazy"] , Score["F"])
rule38 = ctrl.Rule(EndTerm['normal'] & MidTerm["normal"] & HomeWorks["hardwork"] & ClassActivity["very lazy"] , Score["D"])
rule39 = ctrl.Rule(EndTerm['good'] & MidTerm["normal"] & HomeWorks["hardwork"] & ClassActivity["very lazy"] , Score["D"])
rule40 = ctrl.Rule(EndTerm['verygood'] & MidTerm["normal"] & HomeWorks["hardwork"] & ClassActivity["very lazy"] , Score["C"])
rule41 = ctrl.Rule(EndTerm['bad'] & MidTerm["good"] & HomeWorks["hardwork"] & ClassActivity["very lazy"] , Score["D"])
rule42 = ctrl.Rule(EndTerm['normal'] & MidTerm["good"] & HomeWorks["hardwork"] & ClassActivity["very lazy"] , Score["D"])
rule43 = ctrl.Rule(EndTerm['good'] & MidTerm["good"] & HomeWorks["hardwork"] & ClassActivity["very lazy"] , Score["C"])
rule44 = ctrl.Rule(EndTerm['verygood'] & MidTerm["good"] & HomeWorks["hardwork"] & ClassActivity["very lazy"] , Score["C"])
rule45 = ctrl.Rule(EndTerm['bad'] & MidTerm["verygood"] & HomeWorks["hardwork"] & ClassActivity["very lazy"] , Score["D"])
rule46 = ctrl.Rule(EndTerm['normal'] & MidTerm["verygood"] & HomeWorks["hardwork"] & ClassActivity["very lazy"] , Score["C"])
rule47 = ctrl.Rule(EndTerm['good'] & MidTerm["verygood"] & HomeWorks["hardwork"] & ClassActivity["very lazy"] , Score["C"])
rule48 = ctrl.Rule(EndTerm['verygood'] & MidTerm["verygood"] & HomeWorks["hardwork"] & ClassActivity["very lazy"] , Score["B"])

rule49 = ctrl.Rule(EndTerm['bad'] & MidTerm["bad"] & HomeWorks["lazy"] & ClassActivity["lazy"] , Score["F"])
rule50 = ctrl.Rule(EndTerm['normal'] & MidTerm["bad"] & HomeWorks["lazy"] & ClassActivity["lazy"] , Score["F"])
rule51 = ctrl.Rule(EndTerm['good'] & MidTerm["bad"] & HomeWorks["lazy"] & ClassActivity["lazy"] , Score["F"])
rule52 = ctrl.Rule(EndTerm['verygood'] & MidTerm["bad"] & HomeWorks["lazy"] & ClassActivity["lazy"] , Score["D"])
rule53 = ctrl.Rule(EndTerm['bad'] & MidTerm["normal"] & HomeWorks["lazy"] & ClassActivity["lazy"] , Score["F"])
rule54 = ctrl.Rule(EndTerm['normal'] & MidTerm["normal"] & HomeWorks["lazy"] & ClassActivity["lazy"] , Score["F"])
rule55 = ctrl.Rule(EndTerm['good'] & MidTerm["normal"] & HomeWorks["lazy"] & ClassActivity["lazy"] , Score["D"])
rule56 = ctrl.Rule(EndTerm['verygood'] & MidTerm["normal"] & HomeWorks["lazy"] & ClassActivity["lazy"] , Score["D"])
rule57 = ctrl.Rule(EndTerm['bad'] & MidTerm["good"] & HomeWorks["lazy"] & ClassActivity["lazy"] , Score["F"])
rule58 = ctrl.Rule(EndTerm['normal'] & MidTerm["good"] & HomeWorks["lazy"] & ClassActivity["lazy"] , Score["D"])
rule59 = ctrl.Rule(EndTerm['good'] & MidTerm["good"] & HomeWorks["lazy"] & ClassActivity["lazy"] , Score["D"])
rule60 = ctrl.Rule(EndTerm['verygood'] & MidTerm["good"] & HomeWorks["lazy"] & ClassActivity["lazy"] , Score["C"])
rule61 = ctrl.Rule(EndTerm['bad'] & MidTerm["verygood"] & HomeWorks["lazy"] & ClassActivity["lazy"] , Score["D"])
rule62 = ctrl.Rule(EndTerm['normal'] & MidTerm["verygood"] & HomeWorks["lazy"] & ClassActivity["lazy"] , Score["D"])
rule63 = ctrl.Rule(EndTerm['good'] & MidTerm["verygood"] & HomeWorks["lazy"] & ClassActivity["lazy"] , Score["C"])
rule64 = ctrl.Rule(EndTerm['verygood'] & MidTerm["verygood"] & HomeWorks["lazy"] & ClassActivity["lazy"] , Score["C"])

rule65 = ctrl.Rule(EndTerm['bad'] & MidTerm["bad"] & HomeWorks["normal"] & ClassActivity["lazy"] , Score["F"])
rule66 = ctrl.Rule(EndTerm['normal'] & MidTerm["bad"] & HomeWorks["normal"] & ClassActivity["lazy"] , Score["F"])
rule67 = ctrl.Rule(EndTerm['good'] & MidTerm["bad"] & HomeWorks["normal"] & ClassActivity["lazy"] , Score["D"])
rule68 = ctrl.Rule(EndTerm['verygood'] & MidTerm["bad"] & HomeWorks["normal"] & ClassActivity["lazy"] , Score["D"])
rule69 = ctrl.Rule(EndTerm['bad'] & MidTerm["normal"] & HomeWorks["normal"] & ClassActivity["lazy"] , Score["F"])
rule70 = ctrl.Rule(EndTerm['normal'] & MidTerm["normal"] & HomeWorks["normal"] & ClassActivity["lazy"] , Score["D"])
rule71 = ctrl.Rule(EndTerm['good'] & MidTerm["normal"] & HomeWorks["normal"] & ClassActivity["lazy"] , Score["D"])
rule72 = ctrl.Rule(EndTerm['verygood'] & MidTerm["normal"] & HomeWorks["normal"] & ClassActivity["lazy"] , Score["C"])
rule73 = ctrl.Rule(EndTerm['bad'] & MidTerm["good"] & HomeWorks["normal"] & ClassActivity["lazy"] , Score["D"])
rule74 = ctrl.Rule(EndTerm['normal'] & MidTerm["good"] & HomeWorks["normal"] & ClassActivity["lazy"] , Score["D"])
rule75 = ctrl.Rule(EndTerm['good'] & MidTerm["good"] & HomeWorks["normal"] & ClassActivity["lazy"] , Score["C"])
rule76 = ctrl.Rule(EndTerm['verygood'] & MidTerm["good"] & HomeWorks["normal"] & ClassActivity["lazy"] , Score["C"])
rule77 = ctrl.Rule(EndTerm['bad'] & MidTerm["verygood"] & HomeWorks["normal"] & ClassActivity["lazy"] , Score["D"])
rule78 = ctrl.Rule(EndTerm['normal'] & MidTerm["verygood"] & HomeWorks["normal"] & ClassActivity["lazy"] , Score["C"])
rule79 = ctrl.Rule(EndTerm['good'] & MidTerm["verygood"] & HomeWorks["normal"] & ClassActivity["lazy"] , Score["C"])
rule80 = ctrl.Rule(EndTerm['verygood'] & MidTerm["verygood"] & HomeWorks["normal"] & ClassActivity["lazy"] , Score["B"])

rule81 = ctrl.Rule(EndTerm['bad'] & MidTerm["bad"] & HomeWorks["hardwork"] & ClassActivity["lazy"] , Score["F"])
rule82 = ctrl.Rule(EndTerm['normal'] & MidTerm["bad"] & HomeWorks["hardwork"] & ClassActivity["lazy"] , Score["D"])
rule83 = ctrl.Rule(EndTerm['good'] & MidTerm["bad"] & HomeWorks["hardwork"] & ClassActivity["lazy"] , Score["D"])
rule84 = ctrl.Rule(EndTerm['verygood'] & MidTerm["bad"] & HomeWorks["hardwork"] & ClassActivity["lazy"] , Score["C"])
rule85 = ctrl.Rule(EndTerm['bad'] & MidTerm["normal"] & HomeWorks["hardwork"] & ClassActivity["lazy"] , Score["D"])
rule86 = ctrl.Rule(EndTerm['normal'] & MidTerm["normal"] & HomeWorks["hardwork"] & ClassActivity["lazy"] , Score["D"])
rule87 = ctrl.Rule(EndTerm['good'] & MidTerm["normal"] & HomeWorks["hardwork"] & ClassActivity["lazy"] , Score["C"])
rule88 = ctrl.Rule(EndTerm['verygood'] & MidTerm["normal"] & HomeWorks["hardwork"] & ClassActivity["lazy"] , Score["C"])
rule89 = ctrl.Rule(EndTerm['bad'] & MidTerm["good"] & HomeWorks["hardwork"] & ClassActivity["lazy"] , Score["D"])
rule90 = ctrl.Rule(EndTerm['normal'] & MidTerm["good"] & HomeWorks["hardwork"] & ClassActivity["lazy"] , Score["C"])
rule91 = ctrl.Rule(EndTerm['good'] & MidTerm["good"] & HomeWorks["hardwork"] & ClassActivity["lazy"] , Score["C"])
rule92 = ctrl.Rule(EndTerm['verygood'] & MidTerm["good"] & HomeWorks["hardwork"] & ClassActivity["lazy"] , Score["B"])
rule93 = ctrl.Rule(EndTerm['bad'] & MidTerm["verygood"] & HomeWorks["hardwork"] & ClassActivity["lazy"] , Score["C"])
rule94 = ctrl.Rule(EndTerm['normal'] & MidTerm["verygood"] & HomeWorks["hardwork"] & ClassActivity["lazy"] , Score["C"])
rule95 = ctrl.Rule(EndTerm['good'] & MidTerm["verygood"] & HomeWorks["hardwork"] & ClassActivity["lazy"] , Score["B"])
rule96 = ctrl.Rule(EndTerm['verygood'] & MidTerm["verygood"] & HomeWorks["hardwork"] & ClassActivity["lazy"] , Score["B"])

rule97 = ctrl.Rule(EndTerm['bad'] & MidTerm["bad"] & HomeWorks["lazy"] & ClassActivity["normal"] , Score["F"])
rule98 = ctrl.Rule(EndTerm['normal'] & MidTerm["bad"] & HomeWorks["lazy"] & ClassActivity["normal"] , Score["F"])
rule99 = ctrl.Rule(EndTerm['good'] & MidTerm["bad"] & HomeWorks["lazy"] & ClassActivity["normal"] , Score["D"])
rule100 = ctrl.Rule(EndTerm['verygood'] & MidTerm["bad"] & HomeWorks["lazy"] & ClassActivity["normal"] , Score["D"])
rule101 = ctrl.Rule(EndTerm['bad'] & MidTerm["normal"] & HomeWorks["lazy"] & ClassActivity["normal"] , Score["D"])
rule102 = ctrl.Rule(EndTerm['normal'] & MidTerm["normal"] & HomeWorks["lazy"] & ClassActivity["normal"] , Score["D"])
rule103 = ctrl.Rule(EndTerm['good'] & MidTerm["normal"] & HomeWorks["lazy"] & ClassActivity["normal"] , Score["D"])
rule104 = ctrl.Rule(EndTerm['verygood'] & MidTerm["normal"] & HomeWorks["lazy"] & ClassActivity["normal"] , Score["C"])
rule105 = ctrl.Rule(EndTerm['bad'] & MidTerm["good"] & HomeWorks["lazy"] & ClassActivity["normal"] , Score["D"])
rule106 = ctrl.Rule(EndTerm['normal'] & MidTerm["good"] & HomeWorks["lazy"] & ClassActivity["normal"] , Score["D"])
rule107 = ctrl.Rule(EndTerm['good'] & MidTerm["good"] & HomeWorks["lazy"] & ClassActivity["normal"] , Score["C"])
rule108 = ctrl.Rule(EndTerm['verygood'] & MidTerm["good"] & HomeWorks["lazy"] & ClassActivity["normal"] , Score["C"])
rule109 = ctrl.Rule(EndTerm['bad'] & MidTerm["verygood"] & HomeWorks["lazy"] & ClassActivity["normal"] , Score["D"])
rule110 = ctrl.Rule(EndTerm['normal'] & MidTerm["verygood"] & HomeWorks["lazy"] & ClassActivity["normal"] , Score["C"])
rule111 = ctrl.Rule(EndTerm['good'] & MidTerm["verygood"] & HomeWorks["lazy"] & ClassActivity["normal"] , Score["C"])
rule112 = ctrl.Rule(EndTerm['verygood'] & MidTerm["verygood"] & HomeWorks["lazy"] & ClassActivity["normal"] , Score["B"])

rule113 = ctrl.Rule(EndTerm['bad'] & MidTerm["bad"] & HomeWorks["normal"] & ClassActivity["normal"] , Score["F"])
rule114 = ctrl.Rule(EndTerm['normal'] & MidTerm["bad"] & HomeWorks["normal"] & ClassActivity["normal"] , Score["D"])
rule115 = ctrl.Rule(EndTerm['good'] & MidTerm["bad"] & HomeWorks["normal"] & ClassActivity["normal"] , Score["D"])
rule116 = ctrl.Rule(EndTerm['verygood'] & MidTerm["bad"] & HomeWorks["normal"] & ClassActivity["normal"] , Score["C"])
rule117 = ctrl.Rule(EndTerm['bad'] & MidTerm["normal"] & HomeWorks["normal"] & ClassActivity["normal"] , Score["D"])
rule118 = ctrl.Rule(EndTerm['normal'] & MidTerm["normal"] & HomeWorks["normal"] & ClassActivity["normal"] , Score["D"])
rule119 = ctrl.Rule(EndTerm['good'] & MidTerm["normal"] & HomeWorks["normal"] & ClassActivity["normal"] , Score["C"])
rule120 = ctrl.Rule(EndTerm['verygood'] & MidTerm["normal"] & HomeWorks["normal"] & ClassActivity["normal"] , Score["C"])
rule121 = ctrl.Rule(EndTerm['bad'] & MidTerm["good"] & HomeWorks["normal"] & ClassActivity["normal"] , Score["D"])
rule122 = ctrl.Rule(EndTerm['normal'] & MidTerm["good"] & HomeWorks["normal"] & ClassActivity["normal"] , Score["C"])
rule123 = ctrl.Rule(EndTerm['good'] & MidTerm["good"] & HomeWorks["normal"] & ClassActivity["normal"] , Score["C"])
rule124 = ctrl.Rule(EndTerm['verygood'] & MidTerm["good"] & HomeWorks["normal"] & ClassActivity["normal"] , Score["B"])
rule125 = ctrl.Rule(EndTerm['bad'] & MidTerm["verygood"] & HomeWorks["normal"] & ClassActivity["normal"] , Score["C"])
rule126 = ctrl.Rule(EndTerm['normal'] & MidTerm["verygood"] & HomeWorks["normal"] & ClassActivity["normal"] , Score["C"])
rule127 = ctrl.Rule(EndTerm['good'] & MidTerm["verygood"] & HomeWorks["normal"] & ClassActivity["normal"] , Score["B"])
rule128 = ctrl.Rule(EndTerm['verygood'] & MidTerm["verygood"] & HomeWorks["normal"] & ClassActivity["normal"] , Score["B"])

rule129 = ctrl.Rule(EndTerm['bad'] & MidTerm["bad"] & HomeWorks["hardwork"] & ClassActivity["normal"] , Score["D"])
rule130 = ctrl.Rule(EndTerm['normal'] & MidTerm["bad"] & HomeWorks["hardwork"] & ClassActivity["normal"] , Score["D"])
rule131 = ctrl.Rule(EndTerm['good'] & MidTerm["bad"] & HomeWorks["hardwork"] & ClassActivity["normal"] , Score["C"])
rule132 = ctrl.Rule(EndTerm['verygood'] & MidTerm["bad"] & HomeWorks["hardwork"] & ClassActivity["normal"] , Score["C"])
rule133 = ctrl.Rule(EndTerm['bad'] & MidTerm["normal"] & HomeWorks["hardwork"] & ClassActivity["normal"] , Score["D"])
rule134 = ctrl.Rule(EndTerm['normal'] & MidTerm["normal"] & HomeWorks["hardwork"] & ClassActivity["normal"] , Score["C"])
rule135 = ctrl.Rule(EndTerm['good'] & MidTerm["normal"] & HomeWorks["hardwork"] & ClassActivity["normal"] , Score["C"])
rule136 = ctrl.Rule(EndTerm['verygood'] & MidTerm["normal"] & HomeWorks["hardwork"] & ClassActivity["normal"] , Score["B"])
rule137 = ctrl.Rule(EndTerm['bad'] & MidTerm["good"] & HomeWorks["hardwork"] & ClassActivity["normal"] , Score["C"])
rule138 = ctrl.Rule(EndTerm['normal'] & MidTerm["good"] & HomeWorks["hardwork"] & ClassActivity["normal"] , Score["C"])
rule139 = ctrl.Rule(EndTerm['good'] & MidTerm["good"] & HomeWorks["hardwork"] & ClassActivity["normal"] , Score["B"])
rule140 = ctrl.Rule(EndTerm['verygood'] & MidTerm["good"] & HomeWorks["hardwork"] & ClassActivity["normal"] , Score["B"])
rule141 = ctrl.Rule(EndTerm['bad'] & MidTerm["verygood"] & HomeWorks["hardwork"] & ClassActivity["normal"] , Score["C"])
rule142 = ctrl.Rule(EndTerm['normal'] & MidTerm["verygood"] & HomeWorks["hardwork"] & ClassActivity["normal"] , Score["B"])
rule143 = ctrl.Rule(EndTerm['good'] & MidTerm["verygood"] & HomeWorks["hardwork"] & ClassActivity["normal"] , Score["B"])
rule144 = ctrl.Rule(EndTerm['verygood'] & MidTerm["verygood"] & HomeWorks["hardwork"] & ClassActivity["normal"] , Score["A"])

rule145 = ctrl.Rule(EndTerm['bad'] & MidTerm["bad"] & HomeWorks["lazy"] & ClassActivity["hardwork"] , Score["F"])
rule146 = ctrl.Rule(EndTerm['normal'] & MidTerm["bad"] & HomeWorks["lazy"] & ClassActivity["hardwork"] , Score["D"])
rule147 = ctrl.Rule(EndTerm['good'] & MidTerm["bad"] & HomeWorks["lazy"] & ClassActivity["hardwork"] , Score["D"])
rule148 = ctrl.Rule(EndTerm['verygood'] & MidTerm["bad"] & HomeWorks["lazy"] & ClassActivity["hardwork"] , Score["C"])
rule149 = ctrl.Rule(EndTerm['bad'] & MidTerm["normal"] & HomeWorks["lazy"] & ClassActivity["hardwork"] , Score["D"])
rule150 = ctrl.Rule(EndTerm['normal'] & MidTerm["normal"] & HomeWorks["lazy"] & ClassActivity["hardwork"] , Score["D"])
rule151 = ctrl.Rule(EndTerm['good'] & MidTerm["normal"] & HomeWorks["lazy"] & ClassActivity["hardwork"] , Score["C"])
rule152 = ctrl.Rule(EndTerm['verygood'] & MidTerm["normal"] & HomeWorks["lazy"] & ClassActivity["hardwork"] , Score["C"])
rule153 = ctrl.Rule(EndTerm['bad'] & MidTerm["good"] & HomeWorks["lazy"] & ClassActivity["hardwork"] , Score["D"])
rule154 = ctrl.Rule(EndTerm['normal'] & MidTerm["good"] & HomeWorks["lazy"] & ClassActivity["hardwork"] , Score["C"])
rule155 = ctrl.Rule(EndTerm['good'] & MidTerm["good"] & HomeWorks["lazy"] & ClassActivity["hardwork"] , Score["C"])
rule156 = ctrl.Rule(EndTerm['verygood'] & MidTerm["good"] & HomeWorks["lazy"] & ClassActivity["hardwork"] , Score["B"])
rule157 = ctrl.Rule(EndTerm['bad'] & MidTerm["verygood"] & HomeWorks["lazy"] & ClassActivity["hardwork"] , Score["C"])
rule158 = ctrl.Rule(EndTerm['normal'] & MidTerm["verygood"] & HomeWorks["lazy"] & ClassActivity["hardwork"] , Score["C"])
rule159 = ctrl.Rule(EndTerm['good'] & MidTerm["verygood"] & HomeWorks["lazy"] & ClassActivity["hardwork"] , Score["B"])
rule160 = ctrl.Rule(EndTerm['verygood'] & MidTerm["verygood"] & HomeWorks["lazy"] & ClassActivity["hardwork"] , Score["B"])

rule161 = ctrl.Rule(EndTerm['bad'] & MidTerm["bad"] & HomeWorks["normal"] & ClassActivity["hardwork"] , Score["D"])
rule162 = ctrl.Rule(EndTerm['normal'] & MidTerm["bad"] & HomeWorks["normal"] & ClassActivity["hardwork"] , Score["D"])
rule163 = ctrl.Rule(EndTerm['good'] & MidTerm["bad"] & HomeWorks["normal"] & ClassActivity["hardwork"] , Score["C"])
rule164 = ctrl.Rule(EndTerm['verygood'] & MidTerm["bad"] & HomeWorks["normal"] & ClassActivity["hardwork"] , Score["C"])
rule165 = ctrl.Rule(EndTerm['bad'] & MidTerm["normal"] & HomeWorks["normal"] & ClassActivity["hardwork"] , Score["D"])
rule166 = ctrl.Rule(EndTerm['normal'] & MidTerm["normal"] & HomeWorks["normal"] & ClassActivity["hardwork"] , Score["C"])
rule167 = ctrl.Rule(EndTerm['good'] & MidTerm["normal"] & HomeWorks["normal"] & ClassActivity["hardwork"] , Score["C"])
rule168 = ctrl.Rule(EndTerm['verygood'] & MidTerm["normal"] & HomeWorks["normal"] & ClassActivity["hardwork"] , Score["B"])
rule169 = ctrl.Rule(EndTerm['bad'] & MidTerm["good"] & HomeWorks["normal"] & ClassActivity["hardwork"] , Score["C"])
rule170 = ctrl.Rule(EndTerm['normal'] & MidTerm["good"] & HomeWorks["normal"] & ClassActivity["hardwork"] , Score["C"])
rule171 = ctrl.Rule(EndTerm['good'] & MidTerm["good"] & HomeWorks["normal"] & ClassActivity["hardwork"] , Score["B"])
rule172 = ctrl.Rule(EndTerm['verygood'] & MidTerm["good"] & HomeWorks["normal"] & ClassActivity["hardwork"] , Score["B"])
rule173 = ctrl.Rule(EndTerm['bad'] & MidTerm["verygood"] & HomeWorks["normal"] & ClassActivity["hardwork"] , Score["C"])
rule174 = ctrl.Rule(EndTerm['normal'] & MidTerm["verygood"] & HomeWorks["normal"] & ClassActivity["hardwork"] , Score["B"])
rule175 = ctrl.Rule(EndTerm['good'] & MidTerm["verygood"] & HomeWorks["normal"] & ClassActivity["hardwork"] , Score["B"])
rule176 = ctrl.Rule(EndTerm['verygood'] & MidTerm["verygood"] & HomeWorks["normal"] & ClassActivity["hardwork"] , Score["A"])

rule177 = ctrl.Rule(EndTerm['bad'] & MidTerm["bad"] & HomeWorks["hardwork"] & ClassActivity["hardwork"] , Score["D"])
rule178 = ctrl.Rule(EndTerm['normal'] & MidTerm["bad"] & HomeWorks["hardwork"] & ClassActivity["hardwork"] , Score["C"])
rule179 = ctrl.Rule(EndTerm['good'] & MidTerm["bad"] & HomeWorks["hardwork"] & ClassActivity["hardwork"] , Score["C"])
rule180 = ctrl.Rule(EndTerm['verygood'] & MidTerm["bad"] & HomeWorks["hardwork"] & ClassActivity["hardwork"] , Score["B"])
rule181 = ctrl.Rule(EndTerm['bad'] & MidTerm["normal"] & HomeWorks["hardwork"] & ClassActivity["hardwork"] , Score["C"])
rule182 = ctrl.Rule(EndTerm['normal'] & MidTerm["normal"] & HomeWorks["hardwork"] & ClassActivity["hardwork"] , Score["C"])
rule183 = ctrl.Rule(EndTerm['good'] & MidTerm["normal"] & HomeWorks["hardwork"] & ClassActivity["hardwork"] , Score["B"])
rule184 = ctrl.Rule(EndTerm['verygood'] & MidTerm["normal"] & HomeWorks["hardwork"] & ClassActivity["hardwork"] , Score["B"])
rule185 = ctrl.Rule(EndTerm['bad'] & MidTerm["good"] & HomeWorks["hardwork"] & ClassActivity["hardwork"] , Score["B"])
rule186 = ctrl.Rule(EndTerm['normal'] & MidTerm["good"] & HomeWorks["hardwork"] & ClassActivity["hardwork"] , Score["B"])
rule187 = ctrl.Rule(EndTerm['good'] & MidTerm["good"] & HomeWorks["hardwork"] & ClassActivity["hardwork"] , Score["A"])
rule188 = ctrl.Rule(EndTerm['verygood'] & MidTerm["good"] & HomeWorks["hardwork"] & ClassActivity["hardwork"] , Score["A"])
rule189 = ctrl.Rule(EndTerm['bad'] & MidTerm["verygood"] & HomeWorks["hardwork"] & ClassActivity["hardwork"] , Score["A"])
rule190 = ctrl.Rule(EndTerm['normal'] & MidTerm["verygood"] & HomeWorks["hardwork"] & ClassActivity["hardwork"] , Score["A"])
rule191 = ctrl.Rule(EndTerm['good'] & MidTerm["verygood"] & HomeWorks["hardwork"] & ClassActivity["hardwork"] , Score["A"])
rule192 = ctrl.Rule(EndTerm['verygood'] & MidTerm["verygood"] & HomeWorks["hardwork"] & ClassActivity["hardwork"] , Score["A"])

Scoring_ctrl = ctrl.ControlSystem([rule01,rule02,rule03,rule04,rule05,rule06,rule07,rule08,rule09
,rule10,rule11,rule12,rule13,rule14,rule15,rule16,rule17,rule18,rule19,rule20,rule21,rule22,rule23
,rule24,rule25,rule26,rule27,rule28,rule29,rule30,rule31,rule32,rule33,rule34,rule35,rule36,rule37
,rule38,rule39,rule40,rule41,rule42,rule43,rule44,rule45,rule46,rule47,rule49,rule50,rule51,rule52
,rule53,rule54,rule55,rule56,rule57,rule58,rule59,rule60,rule61,rule62,rule63,rule64,rule65,rule66
,rule67,rule68,rule69,rule70,rule71,rule72,rule73,rule74,rule75,rule76,rule77,rule78,rule79,rule80
,rule81,rule82,rule83,rule84,rule85,rule86,rule87,rule88,rule89,rule90,rule91,rule92,rule93,rule94
,rule95,rule96,rule97,rule98,rule99,rule100,rule101,rule102,rule103,rule104,rule105,rule106,rule107
,rule108,rule109,rule110,rule111,rule112,rule113,rule114,rule115,rule116,rule117,rule118,rule119
,rule120,rule121,rule122,rule123,rule124,rule125,rule126,rule127,rule128,rule129,rule130,rule131
,rule132,rule133,rule134,rule135,rule136,rule137,rule138,rule139,rule140,rule141,rule142,rule143
,rule144,rule145,rule146,rule147,rule148,rule149,rule150,rule151,rule152,rule153,rule154,rule155
,rule156,rule157,rule158,rule158,rule159,rule160,rule161,rule162,rule163,rule164,rule165,rule166
,rule167,rule168,rule169,rule170,rule171,rule172,rule173,rule174,rule175,rule176,rule177,rule178
,rule179,rule180,rule181,rule182,rule183,rule184,rule185,rule186,rule187,rule188,rule189,rule190
,rule191,rule192])

Scoring = ctrl.ControlSystemSimulation(Scoring_ctrl)

Scoring.input['EndTerm'] = 15
Scoring.input['MidTerm'] = 18
Scoring.input['HomeWorks'] = 3
Scoring.input['ClassActivity'] = 2


Scoring.compute()
Score.view(sim=Scoring)

while True: 
	answer = CustomDialog(None, "Exit", "result = {} \nFor Exit enter 1".format(Scoring.output['Score'])).result
	if answer == "1": 
		break


