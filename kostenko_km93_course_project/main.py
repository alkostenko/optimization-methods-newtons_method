def main():
    repeat="так"
    while repeat=="так":
        ans=int(input("Введіть номер частини, яку ви хочете дослідити (1 або2): "))
        if ans==1:
            #part 1 
            import research_part1
            research_part1.best()
        if ans==2:
            #part 2
            import research_part2
            research_part2.best()
        repeat=input("Хочете дослідити ще раз? (введіть \"так\" або \"ні\":")



main()