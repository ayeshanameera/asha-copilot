#Danger-sign checker v0.3
#Source: MoHFW "My Safe Motherhood" booklet, page 15

#Each item: (question, level)
#level "FRU" = urgent, "PHC" = contact primary health centre
PREGNANCY_SIGNS = [
    # ---Contact PHC---
    ("Burning while passing urine?", "PHC"),
    ("High grade fever or any medical illness?", "PHC"),
    ("Vaginal bleeding in early pregnancy?", "PHC"),
    ("Excessive nausea and vomiting?", "PHC"),
    ("Leaking per vaginum before onset of labour?", "PHC"),
    ("Fainting and/or pain in abdomen?", "PHC"),
    # --Contact FRU---
    ("Vaginal bleeding in advanced pregnancy?", "FRU"),
    ("Decreased or no foetal movements?", "FRU"),
    ("Swelling all over body, palpitations, shortness of breath?", "FRU"),
    ("Swelling all over body and/or blurring of vision?", "FRU"),
    ("High blood pressure detected in ANC?", "FRU"),
    ("Fits?", "FRU"),
    ("Labour pains or leaking before 9th month of pregnancy?", "FRU"),
    ("Leaking for more than 12 hours without labour pains?", "FRU"),
    ("Foul smelling leaking with or without fever?", "FRU"),
    ("Labour pains for more than 12 hours?", "FRU"),
    ("Continuous abdominal pain?", "FRU"),
]

POSTPARTUM_SIGNS = [
    ("Tear in perinium?", "PHC"),
    ("Inability to pass urine?", "PHC"),
    ("Burning in urination?", "PHC"),
    ("Difficulty in breast feeding?", "PHC"),
    ("Pain in lower abdomen?", "PHC"),
    ("Excessive vaginal bleeding?", "FRU"),
    ("Inability to control defecation/urine?", "FRU"),
    ("Foul smelling vaginal discharge?", "FRU"),
    ("Difficulty in breathing?", "FRU"),
    ("Blurred vision and fits?", "FRU"),
    ("Fever?", "FRU"),
    ("Fainting?", "FRU"),
]

NEWBORN_SIGNS = [
    ("Difficulty in breathing?", "MO"),
    ("Inability to suck?", "MO"),
    ("Inability to pass urine and stools?", "MO"),
    ("Umbilical stump is red or has pus?", "MO"),
    ("More than 10 pustules over body or one large boil?", "MO"),
    ("Jaundice?", "MO"),
    ("Fever?",  "MO"),
    ("Diarrhoea?", "MO"),
    ("Dull and lethargic baby?", "MO"),
    ("Seizure?", "MO"),
    ("Eyes are red or infected?", "MO"),
    ("Any birth defects seen?", "MO"),
]

MESSAGES = {
    "FRU": "URGENT: Contact ANM/MO and go to FRU immediately.",
    "MO": "Contact MO/ANM immediately.",
    "PHC": "Contact ANM/MO and visit PHC.",
}

def ask(question):
    answer = input(question + " (y/n): ").strip().lower()
    return answer == "y"

def run_checker(signs):
    flagged = {"FRU": [], "MO":[], "PHC":[]}

    for question, level in signs:
        if ask(question):
            flagged[level]. append(question)

    #Check from most urgent to least urgent
    for level in ["FRU", "MO", "PHC"]:
        if flagged[level]:
            print("\n" + MESSAGES[level])
            for item in flagged[level]:
                print("-", item)
            return
    print("\n No danger signs reported. Continue routine follow-up.")

print("Who are you checking?")
print("1 = Pregnant woman")
print("2 = Mother after delivery")
print("3 = Newborn baby")
choice = input("Enter 1, 2 or 3:").strip()

if choice == "1":
    run_checker(PREGNANCY_SIGNS)
elif choice == "2":
    run_checker(POSTPARTUM_SIGNS)
elif choice == "3":
    run_checker(NEWBORN_SIGNS)
else:
    print("Please enter 1, 2 or 3.")