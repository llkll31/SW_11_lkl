import random
import base64

print('Welcome To Your Password Generator')

# 사용할 문자셋 정의
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*().,?0123456789'

# 생성할 비밀번호 개수 및 길이 입력
number = int(input('Amount of passwords to generate: '))
length = int(input('Input your password length: '))

print('\nHere are your passwords, their strengths, and base64 encoded versions:\n')

# 비밀번호 강도 평가 함수
def evaluate_password_strength(password):
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in '!@#$%^&*().,?' for c in password)
    
    # 강도 평가 조건
    if len(password) >= 12 and has_lower and has_upper and has_digit and has_special:
        return "매우 강함"
    elif len(password) >= 8 and has_lower and has_upper and has_digit and has_special:
        return "강함"
    elif len(password) >= 6 and (has_lower + has_upper + has_digit + has_special >= 3):
        return "보통"
    else:
        return "약함"

# 비밀번호 생성 및 강도 평가
for pwd in range(number):
    password = ''.join(random.choice(chars) for c in range(length))  # 비밀번호 생성
    strength = evaluate_password_strength(password)  # 강도 평가

    # base64 인코딩
    encoded_password = base64.b64encode(password.encode('utf-8')).decode('utf-8')

    # 결과 출력
    print(f'{password}  -> 강도: {strength}  -> Base64: {encoded_password}')