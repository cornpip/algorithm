score = [0,3,2,1,0,1,2,3]
template = {
    "R":0, "C":0, "J":0, "A":0
}
template_r = {
    "T":0, "F":0, "M":0, "N":0
}

def solution(survey, choices):
    template_c = { key:val for key,val in template.items() }
    template_r_c = { key:val for key,val in template_r.items() }
    ans = ''

    for f, choice in zip(survey, choices):
        f1, f2 = f
        # print(f1, f2, choice)
        try:
            if choice < 4:
                if template_c.get(f1) != None:
                    template_c[f1] += score[choice]
                else:
                    template_r_c[f1] += score[choice]
            if choice > 4:
                if template_c.get(f2) != None:
                    template_c[f2] += score[choice]
                else:
                    template_r_c[f2] += score[choice]
        except Exception as e:
            print(template_c, template_r_c)
            print("!!!!", e)
    
    for f1, f2 in zip(template_c.items(), template_r_c.items()):
        # print((f1[0] if f1[1]>f2[1] or f1[1]==f2[1] else f2[0]))
        ans += (f1[0] if f1[1]>f2[1] or f1[1]==f2[1] else f2[0])
        
    return ans