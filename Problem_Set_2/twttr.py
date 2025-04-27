str = input("Input: ").strip()

if "a" in str or "e" in str or "i" in str or "o" in str or "u" in str or "A" in str or "E" in str or "I" in str or "O" in str or "U" in str:
    print("Output:", str.replace("a", "").replace("e", "").replace("i", "").replace("o", "").replace("u", "").replace("A", "").replace("E", "").replace("I", "").replace("O", "").replace("U", ""))
else:
    print("Output: ", str)