NETLIST_FOR_555_BREADBOARD="""
<?xml version='1.0' encoding='UTF-8'?>
<!-- Created with Fritzing (http://www.fritzing.org/) -->
<netlist date="Thu Jul 21 14:20:53 2022" sketch="555.fzz">
 <net>
  <connector name="Pin 1" id="connector0">
   <part label="U1" id="58220" title="555 Timer"/>
  </connector>
  <connector name="-" id="connector0">
   <part label="C2" id="60670" title="Electrolytic Capacitor"/>
  </connector>
  <connector name="1" id="connector1">
   <part label="C1" id="58510" title="Ceramic Capacitor"/>
  </connector>
 </net>
 <net>
  <connector name="+" id="connector1">
   <part label="C2" id="60670" title="Electrolytic Capacitor"/>
  </connector>
  <connector name="Pin 2" id="connector1">
   <part label="U1" id="58220" title="555 Timer"/>
  </connector>
  <connector name="Pin 0" id="connector0">
   <part label="R1" id="58400" title="330kΩ Resistor"/>
  </connector>
  <connector name="Pin 0" id="connector0">
   <part label="R2" id="59130" title="220kΩ Resistor"/>
  </connector>
  <connector name="Pin 6" id="connector5">
   <part label="U1" id="58220" title="555 Timer"/>
  </connector>
 </net>
 <net>
  <connector name="Pin 1" id="connector1">
   <part label="R1" id="58400" title="330kΩ Resistor"/>
  </connector>
  <connector name="Pin 3" id="connector2">
   <part label="U1" id="58220" title="555 Timer"/>
  </connector>
 </net>
 <net>
  <connector name="Pin 4" id="connector3">
   <part label="U1" id="58220" title="555 Timer"/>
  </connector>
  <connector name="Pin 8" id="connector7">
   <part label="U1" id="58220" title="555 Timer"/>
  </connector>
  <connector name="Pin 1" id="connector1">
   <part label="R2" id="59130" title="220kΩ Resistor"/>
  </connector>
 </net>
 <net>
  <connector name="Pin 5" id="connector4">
   <part label="U1" id="58220" title="555 Timer"/>
  </connector>
  <connector name="0" id="connector0">
   <part label="C1" id="58510" title="Ceramic Capacitor"/>
  </connector>
 </net>
 <net>
  <connector name="Pin 7" id="connector6">
   <part label="U1" id="58220" title="555 Timer"/>
  </connector>
 </net>
</netlist>
"""

NETLIST_FOR_555_STRIPBOARD="""
<?xml version='1.0' encoding='UTF-8'?>
<!-- Created with Fritzing (http://www.fritzing.org/) -->
<netlist date="Fri Jul 22 15:29:36 2022" sketch="555-stripboard.fzz">
 <net>
  <connector id="connector0" name="pin1">
   <part label="J2" id="63240" title="Generic female header - 2 pins"/>
  </connector>
  <connector id="connector0" name="cathode">
   <part label="LED1" id="62470" title="Red (633nm) LED"/>
  </connector>
  <connector id="connector1" name="1">
   <part label="C2" id="60590" title="Ceramic Capacitor"/>
  </connector>
  <connector id="connector1" name="pin2">
   <part label="J1" id="58570" title="Screw terminal - 2 pins"/>
  </connector>
  <connector id="connector1" name="+">
   <part label="C3" id="62140" title="Electrolytic Capacitor"/>
  </connector>
  <connector id="connector0" name="Pin 1">
   <part label="U1" id="58540" title="555 Timer"/>
  </connector>
  <connector id="connector0" name="Pin 0">
   <part label="R2" id="59790" title="33kΩ Resistor"/>
  </connector>
 </net>
 <net>
  <connector id="connector2" name="Pin 3">
   <part label="U1" id="58540" title="555 Timer"/>
  </connector>
  <connector id="connector1" name="anode">
   <part label="LED1" id="62470" title="Red (633nm) LED"/>
  </connector>
  <connector id="connector1" name="pin2">
   <part label="J2" id="63240" title="Generic female header - 2 pins"/>
  </connector>
 </net>
 <net>
  <connector id="connector1" name="Pin 2">
   <part label="U1" id="58540" title="555 Timer"/>
  </connector>
  <connector id="connector1" name="Pin 1">
   <part label="R2" id="59790" title="33kΩ Resistor"/>
  </connector>
  <connector id="connector1" name="Pin 1">
   <part label="R1" id="58900" title="220kΩ Resistor"/>
  </connector>
  <connector id="connector5" name="Pin 6">
   <part label="U1" id="58540" title="555 Timer"/>
  </connector>
 </net>
 <net>
  <connector id="connector7" name="Pin 8">
   <part label="U1" id="58540" title="555 Timer"/>
  </connector>
 </net>
 <net>
  <connector id="connector0" name="pin1">
   <part label="J1" id="58570" title="Screw terminal - 2 pins"/>
  </connector>
  <connector id="connector0" name="Pin 0">
   <part label="R1" id="58900" title="220kΩ Resistor"/>
  </connector>
  <connector id="connector3" name="Pin 4">
   <part label="U1" id="58540" title="555 Timer"/>
  </connector>
 </net>
 <net>
  <connector id="connector0" name="-">
   <part label="C3" id="62140" title="Electrolytic Capacitor"/>
  </connector>
 </net>
 <net>
  <connector id="connector0" name="0">
   <part label="C2" id="60590" title="Ceramic Capacitor"/>
  </connector>
  <connector id="connector4" name="Pin 5">
   <part label="U1" id="58540" title="555 Timer"/>
  </connector>
 </net>
 <net>
  <connector id="connector6" name="Pin 7">
   <part label="U1" id="58540" title="555 Timer"/>
  </connector>
 </net>
</netlist>
"""
