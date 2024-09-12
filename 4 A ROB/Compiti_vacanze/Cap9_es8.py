def is_palindrome(s):
    return s == s[::-1]

def main():
    for km in range(100000, 1000000):
        km_str = str(km)
        if is_palindrome(km_str[2:]):
            if is_palindrome(str(km + 1)[1:]):
                if is_palindrome(str(km + 2)[1:5]):
                    if is_palindrome(str(km + 3)):
                        print(f"Il contachilometri segnava: {km}")
                
                    
if __name__ == "__main__":
    main()
