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

1. **Your car:** pick make, model and generation from the car list, start from a preset, type in your own measurements, or use **Look up**, which opens a web search for the car's dimensions (inside Claude it fills them in directly). A tape-measure guide is built in. **Body style** (hatchback, saloon, estate, SUV, MPV, coupé, pickup, van, lorry, bus) only changes how the vehicle is drawn and the roof outline used for the door-header check; the clearance measurements stay the same. Fields marked as estimates are worth measuring if the result is tight.
2. **Your ramp:** describe the ramp as pieces from the street to the garage floor. Give each piece a length and one of rise, angle or grade. Lengths can be measured along the surface or horizontally. Add easing pieces at the bottom or top, and use negative values for a ramp down into a basement. You can also drag the ramp's corners in the profile drawing.
3. **Door and width:** set the ramp and door widths, and try driving diagonally across the slope to soften the transitions.

Unapplied edits to the car or ramp show straight away as a dashed violet preview in the drawing and the chart. Press **Update result** to make them the main result, then **Roll it in** or drag the slider. The car creeps along and can stop at the first contact. Undo steps back through earlier versions.

**Copy link to this setup** puts your car and ramp into a link you can send; opening it loads the same setup. On a phone, the result stays pinned to the bottom of the screen while you scroll.

The page works in English and Hungarian, in metric or imperial units (US visitors start in imperial, based on their time zone), with light and dark themes. Your settings are saved in the browser.

## Which cars fit?

**Which cars fit this ramp?** (under the result, or the panel further down) checks every car in the list against your ramp, door and width settings. Filter by build years (the last ten by default), body style and make. The list shows the cars that are likely to fit, with the most room above and below first; variants with the same result are merged. **Load** puts a car into the main check.

The finder uses a quick version of the same model: because the underbody and the ramp are both straight-line pieces, the closest point is always at a corner of one of them, so it checks only the corners, at 5 cm steps. It agrees with the full check to within a few millimetres. Only cars with a listed ground clearance are included, and their bumper heights are estimated, so treat the list as a shortlist and measure before you buy.

## How it works

The ramp is a polyline. Each wheel is a circle resting on it, so in a dip a wheel touches both faces. The rear axle position drives the simulation, and the front axle is found at exactly one wheelbase away along the ground. The underbody is modelled as a polyline from the rear bumper's lowest edge, flat at ground-clearance height between the wheels, to the front bumper's lowest edge. At each 2.5 cm step the page measures the shortest distance from the underbody to the ground and reports the tightest point.

Bumper heights in presets are derived from published or typical approach and departure angles, so treat them as estimates.

## Limits

- Suspension is rigid. Use the safety margin (default 3 cm) for load and dip.
- Diagonal driving assumes one straight diagonal line across the whole ramp. The width check adds the sideways drift and says the largest angle that fits; the clearance model follows the car's centreline.
- Preset dimensions are approximate and vary by trim, suspension and wheel size.

## Car list

The car picker uses `cars.json`, built by `tools/build_cars.py` from the [vehicle-makes-models](https://github.com/gor3a/vehicle-makes-models) dataset, whose data comes from autoevolution.com. For each make, model and generation it keeps length, width, height, wheelbase, the lowest listed ground clearance and the most common tyre size. Front overhang, mirror width and bumper heights aren't in the source, so the page estimates them and marks them as estimates. The data can be wrong or describe a different trim, and the page says so whenever a listed car is in use.

`cars.json` is an adapted version of that database and, like its source, is available under the [Open Database License (ODbL) 1.0](https://opendatacommons.org/licenses/odbl/1-0/).

To rebuild it, clone vehicle-makes-models and run `python3 tools/build_cars.py path/to/data/json/all.json cars.json`.

Missing a car? Use **Can't find your car? Suggest it** under the picker.

## Site settings

`config.js` holds optional settings, all public by design:

- `siteUrl`: the public address. Turns on **Copy link to this setup**.
- `goatcounter`: a [GoatCounter](https://www.goatcounter.com) site code. Turns on cookie-free visit stats and the **Say thanks** button, which is counted as a `thanks` event.
- `web3forms`: a [Web3Forms](https://web3forms.com) access key. Turns on the collapsed **Feedback** form, whose messages arrive by email without exposing the address.

Leave a key empty and its feature stays hidden.

## Running locally

It's a single `index.html` plus `cars.json`, with no build step. Serve the folder with any static web server (for example `python3 -m http.server`); opening the file directly works too, but browsers block the car list that way.
