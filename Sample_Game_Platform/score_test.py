import pickle
score_dict = {'123':12}
with open('score.pkl', 'ab') as file:
    pickle.dump(score_dict, file)
with open('score.pkl', 'rb') as file:
    while True:
        try:
            score_list = pickle.load(file)
            for i in score_list:
            # if '123' in score_list:
                print(i, "   ",score_list[i])
        except EOFError:
            break