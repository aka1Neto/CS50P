answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything?");
a = answer.strip().lower();
if a == "42" or a == "forty-two" or a == "forty two":
    print("Yes");

else:
    print("No");