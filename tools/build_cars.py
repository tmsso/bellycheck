# Build cars.json for Belly Check from the vehicle-makes-models dataset (ODbL 1.0).
# Usage: python3 -I tools/build_cars.py <path to data/json/all.json> <output cars.json>
import json, re, sys, statistics, collections, datetime
src, out = sys.argv[1], sys.argv[2]
data = json.load(open(src))

def mm_from(text):
    if not text: return None
    m = re.search(r'\(([\d.,]+)\s*mm\)', text)
    if not m: return None
    v = float(m.group(1).replace(',', ''))
    return v

def tyre_mm(text):
    if not text: return None
    m = re.search(r'(\d{3})\s*/\s*(\d{2})\s*[A-Z]*\s*R?\s*(\d{2}(?:\.\d)?)', text)
    if not m: return None
    return round(int(m.group(1)) * int(m.group(2)) / 100 * 2 + float(m.group(3)) * 25.4)

def mode(vals):
    vals = [v for v in vals if v]
    if not vals: return None
    c = collections.Counter(vals).most_common()
    top = c[0][1]
    return int(statistics.median(sorted(v for v, n in c if n == top)))

def clean_model(make, model):
    for p in (make, make.upper(), make.replace('Š', 'S').upper(), make.split()[0], make.split()[0].upper()):
        if model.upper().startswith(p.upper() + ' '):
            return model[len(p) + 1:].strip()
    return model

makes_out = []
stats = collections.Counter()
for grp in data:
    for mk in grp['makes']:
        mname = mk['name']; models_out = []
        for mo in mk['models']:
            gens_out = []
            for g in mo.get('generations') or []:
                eng = g.get('engines') or []
                L = mode([e.get('lengthMm') for e in eng]); WB = mode([e.get('wheelbaseMm') for e in eng])
                if not (L and WB and 2000 < L < 7000 and 1500 < WB < 5000 and WB < L): stats['skip_nodims'] += 1; continue
                W = mode([e.get('widthMm') for e in eng]); H = mode([e.get('heightMm') for e in eng])
                gcs = [mm_from((e.get('specs') or {}).get('DIMENSIONS / Ground Clearance')) for e in eng]
                gcs = [v for v in gcs if v and 80 <= v <= 400]
                gc = int(min(gcs)) if gcs else 0          # lowest listed variant: the one most likely to scrape
                gcVar = (max(gcs) - min(gcs)) > 15 if gcs else False
                ty = mode([tyre_mm((e.get('specs') or {}).get('TIRES SPECS / Tire Size')) for e in eng]) or 0
                if ty and not 500 < ty < 1000: ty = 0
                y0, y1 = g.get('yearStart'), g.get('yearEnd')
                rest = g['name']
                mclean = clean_model(mname, mo['name'])
                for p in (mo['name'], mclean):
                    if rest.upper().startswith(p.upper()): rest = rest[len(p):].strip()
                rest = re.sub(r'^\(?\d{4}\)?$', '', rest).strip()
                stats['gens'] += 1; stats['gc'] += bool(gc); stats['tyre'] += bool(ty)
                gens_out.append([y0 or 0, y1 or 0, g.get('bodyType') or '', rest, L, W or 0, H or 0, WB, gc, int(gcVar), ty, len(eng)])
            if gens_out:
                gens_out.sort(key=lambda r: (-(r[0] or 0), r[3]))
                models_out.append([clean_model(mname, mo['name']), gens_out])
        if models_out:
            models_out.sort(key=lambda r: r[0].lower())
            makes_out.append([mname, models_out])
makes_out.sort(key=lambda r: r[0].lower())
doc = {
    'v': 1,
    'built': datetime.date.today().isoformat(),
    'license': 'ODbL-1.0',
    'source': 'vehicle-makes-models (https://github.com/gor3a/vehicle-makes-models), data from autoevolution.com; adapted for Belly Check',
    'fields': ['yearStart', 'yearEnd', 'body', 'variant', 'lengthMm', 'widthMm', 'heightMm', 'wheelbaseMm', 'groundClearanceMm (lowest listed, 0 = unknown)', 'groundClearanceVaries', 'tyreDiameterMm (0 = unknown)', 'engineVariants'],
    'makes': makes_out,
}
s = json.dumps(doc, ensure_ascii=False, separators=(',', ':'))
open(out, 'w').write(s)
print(dict(stats), 'makes', len(makes_out), 'bytes', len(s))
