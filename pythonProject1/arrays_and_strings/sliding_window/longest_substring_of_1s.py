def count_1_substring(s: str):
    left = right = answer = 0
    count = 0

    for right in range(len(s)):
        if s[right] == '0':
            count += 1

        while count > 1:
            if s[left] == '0':
                count -= 1
            left += 1

        answer = max(answer, right - left + 1)

    return answer


if __name__ == "__main__":
    s = "1101100111"
    print(count_1_substring(s))
