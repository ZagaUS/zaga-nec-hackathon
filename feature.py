import pandas as pd
data = [
    {"experience_years": 2, "education_level": 1},
    {"experience_years": 5, "education_level": 2},
    {"experience_years": 10, "education_level": 3}
]
df = pd.DataFrame(data)
da=data
#da=data["experience_years": 2, "education_level": 1 ,"experience_edu":None],
#["experience_years": 5, "education_level": 2 ,"experience_edu":None],
#["experience_years": 2, "education_level": 3 ,"experience_edu":None]
da = da["experience_ed"].fullna("experience_years" * "education_level")
print(da)