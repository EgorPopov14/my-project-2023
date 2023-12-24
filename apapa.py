def victory_game():
    import random
    math_example={'65*4':'260','170:5':'34','квад. корень из 625':'25','19^3':'7505','3/5+11/10':'16/10'}
    example,ans=random.choice(list(math_example.items()))
    answer=input(f'сколько будет {example}?:')
    if answer==ans:
        print('верно')
    else:
        print('Неверно')
    print('пока')
victory_game()
