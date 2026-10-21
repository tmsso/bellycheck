# Belly Check

Will your car scrape on the garage ramp? Belly Check rolls a to-scale car up (or down) your ramp and shows exactly where it gets tight.

**Live:** https://bellycheck.tmsso.com

## What it checks

- **Front and rear bumpers** at the dips, where the ramp gets steeper (approach and departure)
- **Underbody** at the crests, where the ramp flattens out (breakover)
- **Roof against the door header**, with the door at the top or bottom of the ramp or anywhere along it
- **Width** of the ramp and the door opening, with mirrors open or folded, and against walls or low curbs

## How to use it

Inputs come in three numbered steps.

1. **Your car:** pick a preset, type in your own measurements, or use **Look up**, which opens a web search for the car's dimensions (inside Claude it fills them in directly). A tape-measure guide is built in. Fields marked as estimates are worth measuring if the result is tight.
2. **Your ramp:** describe the ramp as pieces from the street to the garage floor. Give each piece a length and one of rise, angle or grade. Lengths can be measured along the surface or horizontally. Add easing pieces at the bottom or top, and use negative values for a ramp down into a basement. You can also drag the ramp's corners in the profile drawing.
3. **Door and width:** set the ramp and door widths, and try driving diagonally across the slope to soften the transitions.

Unapplied edits to the car or ramp show straight away as a dashed violet preview in the drawing and the chart. Press **Update result** to make them the main result, then **Roll it in** or drag the slider. The car creeps along and can stop at the first contact. Undo steps back through earlier versions.

**Copy link to this setup** puts your car and ramp into a link you can send; opening it loads the same setup. On a phone, the result stays pinned to the bottom of the screen while you scroll.

The page works in English and Hungarian, in metric or imperial units (US visitors start in imperial, based on their time zone), with light and dark themes. Your settings are saved in the browser.

## How it works

The ramp is a polyline. Each wheel is a circle resting on it, so in a dip a wheel touches both faces. The rear axle position drives the simulation, and the front axle is found at exactly one wheelbase away along the ground. The underbody is modelled as a polyline from the rear bumper's lowest edge, flat at ground-clearance height between the wheels, to the front bumper's lowest edge. At each 2.5 cm step the page measures the shortest distance from the underbody to the ground and reports the tightest point.

Bumper heights in presets are derived from published or typical approach and departure angles, so treat them as estimates.

## Limits

- Suspension is rigid. Use the safety margin (default 3 cm) for load and dip.
- Diagonal driving is modelled along the car's centreline only.
- Preset dimensions are approximate and vary by trim, suspension and wheel size.

## Site settings

`config.js` holds optional settings, all public by design:

- `siteUrl`: the public address. Turns on **Copy link to this setup**.
- `goatcounter`: a [GoatCounter](https://www.goatcounter.com) site code. Turns on cookie-free visit stats and the **Say thanks** button, which is counted as a `thanks` event.
- `web3forms`: a [Web3Forms](https://web3forms.com) access key. Turns on the collapsed **Feedback** form, whose messages arrive by email without exposing the address.

Leave a key empty and its feature stays hidden.

## Running locally

It's a single `index.html` with no build step. Open it in a browser.
