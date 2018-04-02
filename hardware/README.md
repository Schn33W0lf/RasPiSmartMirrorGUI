# GPIO Info
| GPIO (BCM) Pin | GPIO (BOARD) Pin | used for |
| --- | --- | --- |
| 2 | 3 | S1 previous |
| 3 | 5 | S2 reload |
| 4 | 7 | S3 next |
| +5V | 1 | power supply for 433MHz RF Module (and B1/B2/B3 - capacitive sensors instead of switches) |
| +3.3V | 17 |  reference for the gpios (you can toggle it with the jumper) |
| 0V | 6 | ground for the 433MHz RF Module |
| 0V | 9 | reference for the gpios (you can toggle it with the jumper) and ground for the statusLED |
| 17 | 11 | statusLED Red |
| 27 | 13 | statusLED Green |
| 22 | 15 | input 433MHz RF Module |
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