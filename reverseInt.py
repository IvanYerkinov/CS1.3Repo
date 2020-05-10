def reverseNum(num):
    st = list(str(num))
    le = len(str(num))
    for i in range(0, le):
        st.insert(le, st[i])
    return int("".join(st[le:]))
