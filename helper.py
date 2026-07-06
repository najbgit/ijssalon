def sum(dictionary):
    totaal = 0
    for waarde in dictionary.values():
        totaal = totaal + waarde
    return totaal