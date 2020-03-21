a = str(input())
b = str(input())
def common_end(a, b):
    a_len = len(a)-1
    b_len = len(b)-1
    if a[0] == b[0] or a[a_len] == b[b_len]:
        return True
    return False
print(common_end(a, b))