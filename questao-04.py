sp = 6783643
rj = 3667866
mg = 2922988
es = 2716548
outros = 1984953

total = sp + rj + mg + es + outros

SP = (sp * total) / total
RJ = (rj * total) / total
MG = (mg * total) / total
ES = (es * total) / total
OUTROS = (outros * total) / total

print(f'{SP/100000:,.2f}%')
print(f'{RJ/100000:,.2f}%')
print(f'{MG/100000:,.2f}%')
print(f'{ES/100000:,.2f}%')
print(f'{OUTROS/100000:,.2f}%')

