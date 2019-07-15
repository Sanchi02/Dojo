for t in range(int(input())):
    N,K = map(int,input().split())
    forgotten_lang = [n for n in input().split(' ')]
    flags = []
    phrases = []
    for i in range(K):
        phrase = [p for p in input().split(' ')]
        phrase.pop(0)
        phrases.append(phrase)
    for forgotten_lang_word in range(len(forgotten_lang)):
        test_flag = False
        for modern_phase in phrases:
            if(modern_phase.count(forgotten_lang[forgotten_lang_word]) != 0):
                test_flag = True
                flags.append("YES")
                break
        if(test_flag == False):
            flags.append("NO")
    print(*flags)