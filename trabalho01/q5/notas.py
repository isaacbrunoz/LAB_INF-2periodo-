def media(notas):
    if not notas:
        return 0
    return sum(notas) / len(notas)

def maior(notas):
    if not notas:
        return None
    return max(notas)

def menor(notas):
    if not notas:
        return None
    return min(notas)