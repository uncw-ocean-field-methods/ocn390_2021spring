# Getting started
This is meant to serve as a collection of necessary steps to set up and use a datalogging CO2 sensor, relying heavily on other getting started guides that the various manufacturers have written. If a link is broken, please try to find an appropriate replacement getting started guide and/or datasheet on the web. Detailed steps are not included on this page since they are written elsewhere.

We will begin with just the Adafruit Feather M0 Adalogger, a USB cable, and a computer (your laptop). No other hardware is required at this time.

## Step 1. Set up Adafruit Feather M0 Adalogger
Here is a link to the product page: https://www.adafruit.com/product/2796. And here is a link to the Adalogger getting started guide: https://learn.adafruit.com/adafruit-feather-m0-adalogger. Read through the guide and follow along beginning with Arduino IDE setup.

Follow the instructions through Blink and test the Blink example on your Adalogger. 

## Step 2. Test SD card functionality
Continue at the Adalogger getting started guide and check that you can compile the example logging sketch in order to demonstrate the ability to write to and read from SD card. Do not just trust that everything has worked but also verify this by disconnecting the USB cord from the Adalogger (disconnect the battery as well if you have been using one) so that it is no longer powered, remove the micro-SD card from the Adalogger, and plug it into your computer using the supplied micro-SD card adapter.

## Step 3. Breadboarding the PowerBoost circuit
**UNPLUG BATTERY AND UNPLUG USB CABLE. LEAVE THEM UNPLUGGED FOR THIS ENTIRE STEP UNTIL YOUR BREADBOARDED CIRCUIT HAS BEEN VERIFIED.**

The K-30 which we are using as our CO2 sensor requires > 5 V input. A laptop's USB port can supply up to 5 V but when the power draw is large enough, voltage dips below 5 V and the K-30 can behave erratically. Accordingly, we are using an Adafruit PowerBoost 500 (https://www.adafruit.com/product/1944) to boost a rechargeable LiPo battery's output up to 5 V so that we do not have to be concerned about (1) relying on an unsatisfactory USB power supply, (2) adding a separate higher voltage battery just for the K-30, or (3) challenges related to recharging our single rechargeable battery if we were to use a different type of battery or wiring.

We will use the "Bat," "GND," and "5Vo" connections on the edge of the PowerBoost 500 PCB. The PowerBoost 500 does not isolate grounds but rather shares them so our battery ground (input) and 5 V ground (output) are shared.