def solution(s, skip, index):
    answer = ''
    alphabet = "abcdefghijklmnopqrstuvwxyz"
               #acefghijklmnop rstuv xyz
    secret_alphabet = ""
    for char in alphabet:
        if char not in skip:
            secret_alphabet += char
    alpha_len = len(secret_alphabet)
    for char_to_encrypt in s:
        current_pos = secret_alphabet.find(char_to_encrypt)
        new_pos = (current_pos + index) % alpha_len
        answer += secret_alphabet[new_pos]
    return answer


s = "aukks"
skip = "wbqd"
index = 5
print(f"암호화 결과: {solution(s, skip, index)}") 