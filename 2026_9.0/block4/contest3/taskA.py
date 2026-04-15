import sys


def main():

    n, *balls = map(int, input().split())

    stack = []
    destroyed = 0

    for color in balls:
        if stack and stack[-1][0] == color:
            stack[-1][1] += 1
        else:
            stack.append([color, 1])
    
        # проверяем удаление
        if stack[-1][1] >= 3:
            destroyed += stack[-1][1]
            stack.pop()
        
        # после удаления может произойти схлопывание
            while len(stack) >= 2 and stack[-1][0] == stack[-2][0]:
                stack[-2][1] += stack[-1][1]
                stack.pop()
            
                if stack[-1][1] >= 3:
                    destroyed += stack[-1][1]
                    stack.pop()
                else:
                    break

    print(destroyed)
    


if __name__ == '__main__':
    main()
