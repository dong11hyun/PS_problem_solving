
n, m = map(int, input().split())

n_list = list(map(int, input().split()))
m_list = list(map(int, input().split()))

n_set = set(n_list)
m_set = set(m_list)
gyo_set = n_set & m_set

print(len(n_set)-len(gyo_set) * 2 + len(m_set))

