#!/usr/bin/env python3
# ============================================================
#   HACKPATH PHONE ANALYZER v2
#   Created by: Sachin Ser | HackPath
#   Works on: Termux | Linux | Kali
#   Run: python3 phone_analyzer.py
#   No extra install needed — Pure Python!
#   GitHub: github.com/sachin-null/hackpath-phone-analyzer
# ============================================================

import os, sys, json, re, urllib.request, urllib.parse

class C:
    R='\033[91m'; G='\033[92m'; Y='\033[93m'
    M='\033[95m'; CY='\033[96m'; W='\033[97m'
    DIM='\033[2m'; X='\033[0m'; B='\033[1m'

def clear(): os.system('clear' if os.name!='nt' else 'cls')

def banner():
    clear()
    print(C.M+C.B+"""
 ██████╗ ██╗  ██╗ ██████╗ ███╗   ██╗███████╗
 ██╔══██╗██║  ██║██╔═══██╗████╗  ██║██╔════╝
 ██████╔╝███████║██║   ██║██╔██╗ ██║█████╗
 ██╔═══╝ ██╔══██║██║   ██║██║╚██╗██║██╔══╝
 ██║     ██║  ██║╚██████╔╝██║ ╚████║███████╗
 ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝
"""+C.CY+"""
  █████╗ ███╗   ██╗ █████╗ ██╗  ██╗   ██╗███████╗███████╗██████╗
 ██╔══██╗████╗  ██║██╔══██╗██║  ╚██╗ ██╔╝╚════██║██╔════╝██╔══██╗
 ███████║██╔██╗ ██║███████║██║   ╚████╔╝      ██╔╝█████╗  ██████╔╝
 ██╔══██║██║╚██╗██║██╔══██║██║    ╚██╔╝      ██╔╝ ██╔══╝  ██╔══██╗
 ██║  ██║██║ ╚████║██║  ██║███████╗██║       ██║  ███████╗██║  ██║
 ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝╚═╝       ╚═╝  ╚══════╝╚═╝  ╚═╝
"""+C.X)
    print(C.CY+" +--------------------------------------------+")
    print(" |  "+C.M+C.B+"PHONE ANALYZER v2"+C.CY+"  .  "+C.Y+"Sachin Ser"+C.CY+"      |")
    print(" |  "+C.DIM+"HackPath | Termux . Linux . Kali"+C.CY+"          |")
    print(" |  "+C.R+"Educational / Authorized use only!"+C.CY+"       |")
    print(" +--------------------------------------------+"+C.X)
    print()

def sep(t=""):
    if t: print(f"\n{C.CY}{'='*14} {C.Y}{t}{C.CY} {'='*14}{C.X}")
    else: print(f"{C.DIM}{'-'*50}{C.X}")

def ok(m):    print(f"{C.G}[+] {m}{C.X}")
def err(m):   print(f"{C.R}[-] {m}{C.X}")
def inf(m):   print(f"{C.CY}[*] {m}{C.X}")
def fld(k,v): print(f"  {C.Y}{k:<24}{C.X}: {C.W}{v}{C.X}")
def pause():  input(f"\n{C.DIM}Press Enter...{C.X}")
def inp(p):   return input(f"{C.M}  {p} > {C.X}").strip()

def fetch(url):
    try:
        req=urllib.request.Request(url,
            headers={'User-Agent':'Mozilla/5.0'})
        with urllib.request.urlopen(req,timeout=8) as r:
            return json.loads(r.read().decode())
    except: return None

# ── COUNTRY CODES DATABASE ──
COUNTRIES = {
    "1":"USA / Canada","7":"Russia / Kazakhstan",
    "20":"Egypt","27":"South Africa","30":"Greece",
    "31":"Netherlands","32":"Belgium","33":"France",
    "34":"Spain","36":"Hungary","39":"Italy",
    "40":"Romania","41":"Switzerland","43":"Austria",
    "44":"United Kingdom","45":"Denmark","46":"Sweden",
    "47":"Norway","48":"Poland","49":"Germany",
    "51":"Peru","52":"Mexico","53":"Cuba",
    "54":"Argentina","55":"Brazil","56":"Chile",
    "57":"Colombia","58":"Venezuela","60":"Malaysia",
    "61":"Australia","62":"Indonesia","63":"Philippines",
    "64":"New Zealand","65":"Singapore","66":"Thailand",
    "81":"Japan","82":"South Korea","84":"Vietnam",
    "86":"China","90":"Turkey","91":"India",
    "92":"Pakistan","93":"Afghanistan","94":"Sri Lanka",
    "95":"Myanmar","98":"Iran","212":"Morocco",
    "213":"Algeria","216":"Tunisia","218":"Libya",
    "220":"Gambia","221":"Senegal","233":"Ghana",
    "234":"Nigeria","254":"Kenya","255":"Tanzania",
    "256":"Uganda","260":"Zambia","263":"Zimbabwe",
    "355":"Albania","358":"Finland","370":"Lithuania",
    "371":"Latvia","372":"Estonia","373":"Moldova",
    "374":"Armenia","375":"Belarus","380":"Ukraine",
    "381":"Serbia","385":"Croatia","386":"Slovenia",
    "387":"Bosnia","420":"Czech Republic",
    "421":"Slovakia","994":"Azerbaijan",
    "995":"Georgia","996":"Kyrgyzstan","998":"Uzbekistan",
    "880":"Bangladesh","960":"Maldives","977":"Nepal",
    "975":"Bhutan","964":"Iraq","963":"Syria",
    "962":"Jordan","961":"Lebanon","966":"Saudi Arabia",
    "971":"UAE","972":"Israel","973":"Bahrain",
    "974":"Qatar","965":"Kuwait","968":"Oman",
    "967":"Yemen","852":"Hong Kong","853":"Macau",
    "886":"Taiwan","855":"Cambodia","856":"Laos",
    "670":"Timor-Leste","673":"Brunei","679":"Fiji",
}

# ── INDIA CARRIER DATABASE ──
INDIA_CARRIER = {
    # Airtel prefixes
    "9810":"Airtel","9811":"Airtel","9868":"Airtel",
    "9871":"Airtel","9650":"Airtel","9891":"Airtel",
    "9873":"Airtel","9899":"Airtel","9312":"Airtel",
    "9313":"Airtel","9315":"Airtel","9810":"Airtel",
    "7065":"Airtel","8527":"Airtel","9717":"Airtel",
    # Jio prefixes
    "7818":"Jio","7819":"Jio","8955":"Jio",
    "8956":"Jio","8957":"Jio","9321":"Jio",
    "6290":"Jio","6291":"Jio","6292":"Jio",
    "7021":"Jio","7022":"Jio","7023":"Jio",
    "7574":"Jio","7575":"Jio","7576":"Jio",
    "9152":"Jio","9153":"Jio","9154":"Jio",
    # Vi (Vodafone-Idea)
    "9820":"Vi","9821":"Vi","9822":"Vi",
    "9823":"Vi","9824":"Vi","9825":"Vi",
    "9930":"Vi","9869":"Vi","9833":"Vi",
    "9892":"Vi","9004":"Vi","9326":"Vi",
    # BSNL prefixes
    "9436":"BSNL","9435":"BSNL","9434":"BSNL",
    "9433":"BSNL","9432":"BSNL","8794":"BSNL",
    "7005":"BSNL","6012":"BSNL","9774":"BSNL",
    # Aircel (now defunct but numbers still active)
    "9840":"Aircel","9841":"Aircel",
}

# ── INDIA STATES ──
INDIA_STATES = {
    "9400":"Kerala","9447":"Kerala","9446":"Kerala",
    "9495":"Kerala","9895":"Kerala","9847":"Kerala",
    "9496":"Kerala","9745":"Kerala","9746":"Kerala",
    "9747":"Kerala","9048":"Kerala","9388":"Kerala",
    "9249":"Kerala","9539":"Kerala","9447":"Kerala",
    "9810":"Delhi","9811":"Delhi","9871":"Delhi",
    "9312":"Delhi","9717":"Delhi","9999":"Delhi",
    "9910":"Delhi","9650":"Delhi","9891":"Delhi",
    "9820":"Mumbai","9821":"Mumbai","9930":"Mumbai",
    "9869":"Mumbai","9892":"Mumbai","9833":"Mumbai",
    "9004":"Mumbai","9326":"Mumbai","9322":"Mumbai",
    "9840":"Chennai","9841":"Chennai","9884":"Chennai",
    "9176":"Chennai","9790":"Chennai","8122":"Chennai",
    "9900":"Bangalore","9886":"Bangalore",
    "9844":"Bangalore","9980":"Bangalore",
    "9743":"Bangalore","8971":"Bangalore",
    "9830":"Kolkata","9831":"Kolkata",
    "9432":"Kolkata","9433":"Kolkata","9903":"Kolkata",
    "9824":"Gujarat","9825":"Gujarat",
    "9714":"Gujarat","9426":"Gujarat","9879":"Gujarat",
    "9850":"Maharashtra","9860":"Maharashtra",
    "9890":"Maharashtra","9763":"Maharashtra",
    "9876":"Punjab","9815":"Punjab",
    "9914":"Punjab","9872":"Punjab","9417":"Punjab",
    "9001":"Rajasthan","9828":"Rajasthan",
    "9413":"Rajasthan","9414":"Rajasthan",
    "9161":"UP","9839":"UP","9415":"UP","9450":"UP",
    "9451":"UP","9452":"UP","9794":"UP",
    "9908":"Hyderabad","9848":"Hyderabad",
    "9949":"Hyderabad","9618":"Hyderabad",
}

def detect_carrier(n10):
    p4=n10[:4]; p3=n10[:3]
    for prefix,carrier in INDIA_CARRIER.items():
        if p4==prefix or p3==prefix:
            return carrier
    return "Unknown"

def detect_state(n10):
    p4=n10[:4]
    return INDIA_STATES.get(p4,"Unknown region")

def clean_number(raw):
    return raw.replace(' ','').replace('-','') \
               .replace('(','').replace(')','') \
               .replace('.','').replace('+','00') \
               .strip()

def detect_country(number):
    num=number.lstrip('0')
    for l in [3,2,1]:
        prefix=num[:l]
        if prefix in COUNTRIES:
            return prefix, COUNTRIES[prefix], num[l:]
    return "","Unknown",number

# ══════════════════════════════════════════
#   1. SINGLE NUMBER ANALYZE
# ══════════════════════════════════════════
def analyze_single():
    sep("PHONE NUMBER ANALYZER")
    print(f"{C.DIM}  Formats: +91XXXXXXXXXX | 0091XXXXXXXXXX | 91XXXXXXXXXX | 10 digits{C.X}\n")

    raw=inp("Enter phone number")
    if not raw: err("Empty!"); pause(); return

    cleaned=clean_number(raw)
    number=cleaned.lstrip('0')

    sep("FORMAT ANALYSIS")
    fld("Input",raw)
    fld("Cleaned",cleaned)
    fld("Digits only",re.sub(r'\D','',raw))

    # Country detect
    code,country,local=detect_country(number)

    fld("Country Code",f"+{code}" if code else "Not detected")
    fld("Country",country)
    fld("Local Number",local)

    # India specific
    if code=="91" or (len(re.sub(r'\D','',raw))==10
                      and re.sub(r'\D','',raw)[0] in '6789'):
        num10=local if len(local)==10 else re.sub(r'\D','',raw)[-10:]
        if len(num10)==10:
            sep("INDIA ANALYSIS")
            carrier=detect_carrier(num10)
            state=detect_state(num10)
            fld("Number (10d)",num10)
            fld("Carrier",carrier)
            fld("State/Region",state)
            ntype="Mobile" if num10[0] in '6789' else "Landline"
            fld("Type",ntype)
            valid="Valid" if num10[0] in '6789' and len(num10)==10 else "Check number"
            fld("Format",valid)

            # Carrier color
            carrier_colors={
                'Airtel':C.R,'Jio':C.B,
                'Vi':C.M,'BSNL':C.G
            }
            cc=carrier_colors.get(carrier,C.W)
            print(f"\n  Carrier: {cc}{C.B}{carrier}{C.X}")

    # International formats
    sep("NUMBER FORMATS")
    if code:
        fld("E.164",     f"+{code}{local}")
        fld("International",f"+{code} {local}")
        fld("With 00",   f"00{code}{local}")
        fld("Local",     local)
    else:
        fld("As entered",cleaned)

    # Online lookup links
    sep("ONLINE LOOKUP")
    num_search=local if local else number
    print(f"\n  {C.CY}Truecaller:{C.X}")
    print(f"  {C.W}https://www.truecaller.com/search/in/{num_search}{C.X}")
    print(f"\n  {C.CY}Google:{C.X}")
    print(f"  {C.W}https://www.google.com/search?q=%2B{code}{num_search}{C.X}")
    print(f"\n  {C.CY}Spam Check:{C.X}")
    print(f"  {C.W}https://www.shouldianswer.com/phone-number/{num_search}{C.X}")
    print(f"  {C.W}https://www.callerinfo.com/number/{num_search}{C.X}")

    # Online API
    sep("LIVE LOOKUP")
    inf("Checking online...")
    data=fetch(f"https://api.country.is/+{code}{local}")
    if data:
        fld("API Country",data.get('country','N/A'))

    # Save
    if inp("\nSave result? [y/N]").lower()=='y':
        fname=f"phone_{re.sub(r'\\D','',raw)}.txt"
        with open(fname,'w') as f:
            f.write(f"Phone Analysis: {raw}\n")
            f.write(f"{'='*40}\n")
            f.write(f"Cleaned: {cleaned}\n")
            f.write(f"Country: {country}\n")
            f.write(f"Country Code: +{code}\n")
            f.write(f"Local: {local}\n")
            if code=="91":
                num10=local[-10:] if len(local)>=10 else local
                f.write(f"Carrier: {detect_carrier(num10)}\n")
                f.write(f"State: {detect_state(num10)}\n")
        ok(f"Saved → {fname}")
    pause()

# ══════════════════════════════════════════
#   2. BULK ANALYZE
# ══════════════════════════════════════════
def bulk_analyze():
    sep("BULK PHONE ANALYZER")
    fname=inp("Input file (one number per line)")
    if not os.path.exists(fname):
        err(f"File not found: {fname}"); pause(); return

    outfile=inp("Output file [results.txt]") or "results.txt"
    inf(f"Analyzing from {fname}...")

    results=[]
    errors=[]

    with open(fname,'r') as f:
        numbers=[l.strip() for l in f if l.strip()]

    inf(f"Found {len(numbers)} numbers")

    for raw in numbers:
        try:
            cleaned=clean_number(raw)
            number=cleaned.lstrip('0')
            code,country,local=detect_country(number)

            carrier="N/A"; state="N/A"
            if code=="91":
                num10=local[-10:] if len(local)>=10 else local
                carrier=detect_carrier(num10)
                state=detect_state(num10)

            result={
                'input':raw,'code':code,'country':country,
                'local':local,'carrier':carrier,'state':state
            }
            results.append(result)

            cc={'Airtel':C.R,'Jio':C.B,'Vi':C.M,'BSNL':C.G}.get(carrier,C.W)
            print(f"  {C.G}✓{C.X} {raw:<20} +{code:<4} {country:<20} {cc}{carrier}{C.X} {state}")

        except Exception as e:
            errors.append(f"{raw}: {e}")
            print(f"  {C.R}✗{C.X} {raw} — Error")

    # Save results
    with open(outfile,'w') as f:
        f.write("Input|Code|Country|Local|Carrier|State\n")
        f.write("="*70+"\n")
        for r in results:
            f.write(f"{r['input']}|+{r['code']}|{r['country']}|"
                   f"{r['local']}|{r['carrier']}|{r['state']}\n")

    sep("SUMMARY")
    ok(f"Analyzed: {len(results)} numbers")
    if errors: err(f"Errors: {len(errors)}")
    ok(f"Saved → {outfile}")

    # Stats
    if results:
        from collections import Counter
        countries=Counter(r['country'] for r in results)
        carriers=Counter(r['carrier'] for r in results
                        if r['carrier']!='N/A')
        sep("STATS")
        print(f"\n  {C.Y}Top Countries:{C.X}")
        for c,n in countries.most_common(5):
            print(f"    {C.W}{c:<30}{C.X} {C.G}{n}{C.X}")
        if carriers:
            print(f"\n  {C.Y}India Carriers:{C.X}")
            for c,n in carriers.most_common():
                print(f"    {C.W}{c:<20}{C.X} {C.G}{n}{C.X}")
    pause()

# ══════════════════════════════════════════
#   3. COUNTRY CODE LOOKUP
# ══════════════════════════════════════════
def country_lookup():
    sep("COUNTRY CODE LOOKUP")
    search=inp("Search country name or code (Enter for all)")
    print()

    found=0
    for code,country in sorted(COUNTRIES.items(),key=lambda x:int(x[0])):
        if not search or search.lower() in country.lower() or search in code:
            print(f"  {C.Y}+{code:<6}{C.X} {C.W}{country}{C.X}")
            found+=1

    print(f"\n  {C.DIM}Found {found} countries{C.X}")
    pause()

# ══════════════════════════════════════════
#   4. INDIA CARRIER LOOKUP
# ══════════════════════════════════════════
def india_carrier_lookup():
    sep("INDIA CARRIER LOOKUP")
    print(f"{C.DIM}  Enter 10-digit Indian mobile number{C.X}\n")

    num=inp("Number (10 digits)")
    num=re.sub(r'\D','',num)
    if num.startswith('91') and len(num)==12:
        num=num[2:]
    if len(num)!=10:
        err("Please enter 10-digit number!"); pause(); return

    sep("CARRIER INFO")
    fld("Number",num)
    fld("Carrier",detect_carrier(num))
    fld("State/Region",detect_state(num))
    fld("Type","Mobile" if num[0] in '6789' else "Landline")
    fld("Format","Valid" if num[0] in '6789' else "Invalid")
    fld("E.164",f"+91{num}")

    # Prefix info
    fld("Prefix (4d)",num[:4])
    fld("Prefix (3d)",num[:3])

    print(f"\n  {C.CY}Search online:{C.X}")
    print(f"  {C.W}https://www.truecaller.com/search/in/{num}{C.X}")
    pause()

# ══════════════════════════════════════════
#   5. NUMBER FORMATTER
# ══════════════════════════════════════════
def number_formatter():
    sep("NUMBER FORMATTER")
    raw=inp("Phone number")
    if not raw: err("Empty!"); pause(); return

    cleaned=clean_number(raw)
    number=cleaned.lstrip('0')
    code,country,local=detect_country(number)

    sep("ALL FORMATS")
    if code:
        fld("E.164",          f"+{code}{local}")
        fld("International",  f"+{code} {local}")
        fld("National (00)",  f"00{code}{local}")
        fld("Local only",     local)
        fld("Digits only",    f"{code}{local}")
        if code=="91" and len(local)>=10:
            n10=local[-10:]
            fld("India format",   f"0{n10}")
            fld("India (space)",  f"{n10[:5]} {n10[5:]}")
            fld("India (dash)",   f"{n10[:5]}-{n10[5:]}")
    else:
        fld("As cleaned",cleaned)
        fld("Digits only",re.sub(r'\D','',raw))
    pause()

# ══════════════════════════════════════════
#   6. SPAM CHECK LINKS
# ══════════════════════════════════════════
def spam_check():
    sep("SPAM CHECK LINKS")
    raw=inp("Phone number")
    if not raw: err("Empty!"); pause(); return

    cleaned=clean_number(raw)
    number=cleaned.lstrip('0')
    code,country,local=detect_country(number)

    num=local if local else number
    intl=f"{code}{local}" if code else number

    sep("SPAM DATABASES")
    links=[
        ("Truecaller",    f"https://www.truecaller.com/search/in/{num}"),
        ("Should I Answer",f"https://www.shouldianswer.com/phone-number/{num}"),
        ("CallerInfo",    f"https://www.callerinfo.com/number/{num}"),
        ("WhoCallsMe",    f"https://whocallsme.com/Phone-Number.aspx/{num}"),
        ("Google Search", f"https://www.google.com/search?q={urllib.parse.quote(raw)}"),
        ("NumLooker",     f"https://www.numlooker.com/{num}"),
    ]

    for name,url in links:
        print(f"\n  {C.Y}{name}:{C.X}")
        print(f"  {C.W}{url}{C.X}")
    pause()

# ══════════════════════════════════════════
#   MAIN MENU
# ══════════════════════════════════════════
def main():
    while True:
        banner()
        print(f"  {C.B}MENU{C.X}")
        print(f"  {C.M}[1]{C.X} Analyze Phone Number")
        print(f"  {C.M}[2]{C.X} Bulk Analyze (from file)")
        print(f"  {C.M}[3]{C.X} Country Code Lookup")
        print(f"  {C.M}[4]{C.X} India Carrier Lookup")
        print(f"  {C.M}[5]{C.X} Number Formatter")
        print(f"  {C.M}[6]{C.X} Spam Check Links")
        print(f"  {C.R}[0]{C.X} Exit")
        print(f"\n{C.DIM}  python3 phone_analyzer.py | HackPath v2{C.X}\n")

        ch=input(f"{C.M}HackPath Phone > {C.X}").strip()
        menu={
            '1':analyze_single,'2':bulk_analyze,
            '3':country_lookup,'4':india_carrier_lookup,
            '5':number_formatter,'6':spam_check,
        }
        if ch in menu: menu[ch]()
        elif ch=='0':
            print(f"\n{C.M}HackPath Phone Analyzer v2 — Bye! 👋{C.X}\n")
            sys.exit(0)
        else:
            print(f"{C.R}Invalid!{C.X}")

if __name__=='__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{C.M}Bye! 👋{C.X}\n")
        sys.exit(0)
