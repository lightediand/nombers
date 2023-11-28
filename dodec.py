def dodec(n: int):
    dodec = []
    for i in range(n):
        dodecahedron = (i*(3*i-1)*(3*i-2))//2
        if dodecahedron < n:
            dodec.append(dodecahedron)
    return dodec
