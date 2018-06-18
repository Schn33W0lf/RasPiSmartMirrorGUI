# GPIO Info
| GPIO (BOARD) Pin | GPIO (BCM) Pin | Used for | Action |
| --- | --- | --- | --- |
| 1 | +3.3V | | |
| 2 | +5V | W1 Pullup, W1 **(+)** | |
| 3 | I-2 | B1 I/O | Reload image (Menu: Shutdown) |
| 4 | +5V | _?433MHz **(+)**?_ | |
| 5 | I-3 | B2 I/O | Enter Menu (Menu: Exit Menu) |
| 6 | 0V | W1 **(&ndash;)** | |
| 7 | I-4 | B3 I/O | Reload header (Menu: Exit GUI) |
| 8 | IO-14 | W1 Data | Get temperatures |
| 9 | 0V | B1 - B3 **(&ndash;)** | |
| 10 | IO-15 | | |
| 11 | O-17 | D1-RED | statusLed('RED') |
| 12 | IO-18 | | |
| 13 | O-27 | D1-GREEN | statusLed('GRN') |
| 14 | 0V | _?433MHz **(&ndash;)**?_ | |
| 15 | IO-22 | _?433MHz I/O?_ | _?_ |
| 16 | IO-23 | | |
| 17 | +3.3V | B1 - B3 **(+)**, B1 - B3 Pullup | |
| 18 | IO-24 | | |
| 19 | IO-10 | | |
| 20 | 0V | | |

# SmartMirrorHAT Part list
| No. | Amount | Part description | details
| --- | --- | --- | --- |
| 1. | 1 | female pin headers | 2x10 0° 2.54mm |
| 2. | 1 | female pin headers | 1x4 90° 2.54mm |
| 3. | 1 | male pin headers | 1x3 0° (for jumper) |
| 4. | 1 | jumper cabs | 1x2 2.54mm |
| 5. | 1 | potentiometer | (play a bit around with the values I've used any from a kit. min: ~500Ω, max: ~30kΩ) |
| 6. | 1 | resistor | (play a bit around with the values I've used 10kΩ - and it's not very good :P) |
| 7. | 3 | resistors | +/-5% 10kΩ (10000 Ohm) |
| 8. | 4 | PCB connectors and cables | [like those](https://www.reichelt.com/PCB-Connectors/PS-25-3W-BR/3/index.html?ACTION=3&GROUPID=7525&ARTICLE=14828) |
| 9. | 1 | Display panel (eg old laptop), driverboard (eBay or so), power supply and HDMI cable ||
| 10. | 1 | Rpi power supply | 5.1V 2.5A |
# Circuits & Plans
## Circuit 1:
[![circuit 1](SmartMirrorHAT-circuit.png)](SmartMirrorHAT-circuit.png)
