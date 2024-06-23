semina_list = {
    "Algorithm": 204,
    "DataAnalysis": 207,
    "ArtificialIntelligence": 302,
    "CyberSecurity": "B101",
    "Network": 303,
    "Startup": 501,
    "TestStrategy": 105
}

cnt = int(input())
semina = []
for i in range(cnt):
    semina.append(input())

for classroom in semina :
    print(semina_list[classroom])