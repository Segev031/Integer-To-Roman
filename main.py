def intToRoman(num):
        """
        :type num: int
        :rtype: str
        """
        s = ''
        s += 'M' * (num // 1000)
        
        num %= 1000
        p = num // 100
        if p == 9:
            s += 'CM'
        elif p == 4:
            s += 'CD'
        else:
            s += 'D' * (p // 5) + 'C' * (p % 5)
        
        num %= 100
        p = num // 10
        if p == 9:
            s += 'XC'
        elif p == 4:
            s += 'XL'
        else:
            s += 'L' * (p // 5) + 'X' * (p % 5)
        
        
        num %= 10
        if num == 9:
            s += 'IX'
        elif num == 4:
            s += 'IV'
        else:
            s += 'V' * (num // 5) + 'I' * (num % 5)
        return s