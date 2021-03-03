# Waterlow Pressure Area Risk Assessment
# http://www.healthcareimprovementscotland.org/programmes/patient_safety/tissue_viability_resources/waterlow_risk_assessment_chart.aspx
# http://www.judy-waterlow.co.uk/downloads/Waterlow%20Score%20Card-front.pdf

# Example - Nursing Student code for "Malnutrition Universal Screening Tool"
# https://www.bapen.org.uk/pdfs/must/must_full.pdf
# (This is the student example as found)

def get_bmi():
    BMI = int(input("enter your BMI: "))
    if BMI < 20:
        return 3
    elif BMI < 25:
        return 0
    elif BMI < 30:
        return 1
    else:
        return 2


def get_sex():
    Sex = input("enter your Sex: M or F: ")
    if Sex == "M":
        return 1
    if Sex == "F":
        return 2


def get_age():
    Age = int(input("enter your Age: "))
    if Age < 50:
        return 1
    if Age < 65:
        return 2
    if Age < 75:
        return 3
    if Age < 81:
        return 4
    if Age >= 81:
        return 5


def get_skin():
    print("1=healthy")
    print("2=tissue_paper")
    print("3=dry")
    print("4=oedematous")
    print("5=clammy,pyrexia")
    print("6=discoloured graded 1")
    print("7=broken/spots_grade_2-4")
    Skin = int(input("enter Skin type: "))
    if Skin == 1:
        return 0
    if Skin == 2:
        return 1
    if Skin == 3:
        return 1
    if Skin == 4:
        return 1
    if Skin == 5:
        return 1
    if Skin == 6:
        return 2
    if Skin == 7:
        return 3


def get_continence():
    print("1=complete/catheterised")
    print("2=urine_incontinence")
    print("3=faecal_incontinence")
    print("4=urinary_&_faecal_incontinence")
    Continence = int(input("enter_continence_level: "))
    if Continence == 1:
        return 0
    if Continence == 2:
        return 1
    if Continence == 3:
        return 2
    if Continence == 4:
        return 3


def get_mobility():
    print("1=fully")
    print("2=restless_fidgety")
    print("3=apathetic")
    print("4=restricted")
    print("5=bedbound_&_traction")
    print("6=chairbound")
    Mobility = int(input("enter_mobility_level: "))
    if Mobility == 1:
        return 0
    if Mobility == 2:
        return 1
    if Mobility == 3:
        return 2
    if Mobility == 4:
        return 3
    if Mobility == 5:
        return 4
    if Mobility == 6:
        return 5


def get_tissue_malnutrition():
    print("1=terminal_cachexia")
    print("2=multiple_organ_failure")
    print("3=single_organ_failure")
    print("4=peripheral_vascular_disease")
    print("5=anaemia_Hb<8")
    print("6=smoking")
    print("7=none")
    Tissue_Malnutrition = int(input("enter_tissue_malnutrition: "))
    if Tissue_Malnutrition == 1:
        return 8
    if Tissue_Malnutrition == 2:
        return 8
    if Tissue_Malnutrition == 3:
        return 5
    if Tissue_Malnutrition == 4:
        return 5
    if Tissue_Malnutrition == 5:
        return 2
    if Tissue_Malnutrition == 6:
        return 1
    if Tissue_Malnutrition == 7:
        return 0


def get_major_surgerie():
    print("1=orthopaedic/spinal")
    print("2=on_table_>2_HR")
    print("3=on_table_>_6_HR")
    print("4=none")
    Major_Surgerie = int(input("enter_major_surgerie: "))
    if Major_Surgerie == 1:
        return 5
    if Major_Surgerie == 2:
        return 5
    if Major_Surgerie == 3:
        return 8
    if Major_Surgerie == 4:
        return 0

def get_malnutrition_screening_tool():
    def B():
        print("1=0.5-5kg")
        print("2=5-10kg")
        print("3=10-15kg")
        print("4=>15kg")
        print("5=unsure")
        B = int(input("Weight_loss_score: "))
        if B == 1:
            return 1
        if B == 2:
            return 2
        if B == 3:
            return 3
        if B == 4:
            return 4
        if B == 5:
            return 2
    def C():
        print("1=No")
        print("2=Yes")
        C = int(input("Patient_eating_poorly/lack_of_apetite: "))
        if C == 1:
            return 0
        if C == 2:
            return 1
    print("1=Yes")
    print("2=No")
    print("3=Unsure")
    malnutrition_screening_tool = int(input("Has_patient_lost_weight_recently? "))
    if malnutrition_screening_tool == 1:
        return B()
    if malnutrition_screening_tool == 2:
        return C()
    if malnutrition_screening_tool == 3:
        return C() + 2


total_score = (
        get_bmi() +
        get_sex() +
        get_age() +
        get_skin() +
        get_continence() +
        get_mobility() +
        get_tissue_malnutrition() +
        get_major_surgerie() +
        get_malnutrition_screening_tool()
)
print(total_score)
