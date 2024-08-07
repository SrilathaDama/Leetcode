class Solution:
    def numberToWords(self, num: int) -> str:
        below_twenty = ["","One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens_places = ["","","Twenty","Thirty","Forty", "Fifty", "Sixty","Seventy","Eighty","Ninety"]

        if num == 0:
            return "Zero"
        def two_digit(num):
            if num < 20:
                return below_twenty[num]
            else:
                tens = num//10
                ones = num % 10
                return tens_places[tens] + ('' if ones == 0 else ' ' + below_twenty[ones])

        
        def three_digit(num):
            if not num:
                return ''
            if not num//100:
                return two_digit(num)
            return below_twenty[num//100] + ' ' + 'Hundred' + (' ' + two_digit(num % 100) if num % 100 else '')

        billion = num//1000000000
        million = (num//1000000) % 1000
        thousand = (num//1000) % 1000
        hundred = num % 1000

        res = ''
        if billion:
            res += three_digit(billion) + ' Billion'
        if million:
            if res:
                res += ' '
            res += three_digit(million) + ' Million'

        if thousand:
            if res:
                res += ' '
            res += three_digit(thousand) + ' Thousand'
        
        if hundred:
            if res:
                res += ' '
            res += three_digit(hundred)
        
        return res.strip()


        
