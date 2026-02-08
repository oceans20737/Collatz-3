#!/usr/bin/env python
# coding: utf-8

# In[40]:


def collatz3(n):
    """
    Calculates the Collatz-3 trajectory for a given integer n.
    Rules:
    - If divisible by 3: divide by 3.
    - If n ≡ 1 (mod 3): (4n - 1) / 3
    - If n ≡ 2 (mod 3): (4n + 1) / 3
    """
    if n < 1:
        return [], 0

    steps = 0
    path = [n]

    while n != 1:
        if n % 3 == 0:
            n //= 3
        else:
            r = n % 3
            if r == 1:
                n = (4 * n - 1) // 3
            else:  # r == 2
                n = (4 * n + 1) // 3

        path.append(n)
        steps += 1

    return path, steps


if __name__ == "__main__":
    try:
        num = int(input("Enter a positive integer: "))
        path, steps = collatz3(num)
        print("Path:", " → ".join(map(str, path)))
        print("Steps (3-Resistance):", steps)
    except ValueError:
        print("Please enter a valid positive integer.")


# In[ ]:




