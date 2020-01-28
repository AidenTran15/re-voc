import random

dicts = [
    {
        'name': 'Malware',
        'wordclass': 'Noun',
        'Definition': 'Phần mềm độc hại'
    },

        {
        'name': 'Invoke',
        'wordclass': 'Verb',
        'Definition': 'Gọi'
    },

        {
        'name': 'Integrity',
        'wordclass': 'Adj',
        'Definition': 'Chính trực'
    },

        {
        'name': 'Cipher',
        'wordclass': 'Noun',
        'Definition': 'Mật mã'
    },

        {
        'name': 'Possess',
        'wordclass': 'Noun',
        'Definition': 'Sở hữu'
    },

        {
        'name': 'Discrete',
        'wordclass': 'Adj',
        'Definition': 'Không liền mạch'
    },

        {
        'name': 'Imperative',
        'wordclass': 'Adj',
        'Definition': 'Mệnh lệch'
    },

        {
        'name': 'Insidious',
        'wordclass': 'Adj',
        'Definition': 'Xạo quyệt'
    },

        {
        'name': 'Eavesdrop',
        'wordclass': 'Verb',
        'Definition': 'Nghe lén'
    },

        {
        'name': 'Immense',
        'wordclass': 'Adj',
        'Definition': 'Bao La'
    },

        {
        'name': 'Scrutiny',
        'wordclass': 'Noun',
        'Definition': 'Giám sát'
    },

        {
        'name': 'Deviation',
        'wordclass': 'Noun',
        'Definition': 'Không chính xác'
    },

        {
        'name': 'Grasp',
        'wordclass': 'Noun',
        'Definition': 'Sự hiểu biết'
    },

        {
        'name': 'Disaster',
        'wordclass': 'Noun',
        'Definition': 'Thảm họa'
    },

        {
        'name': 'Semantic',
        'wordclass': 'Adj',
        'Definition': 'Ý nghĩa của từ'
    },

        {
        'name': 'Incident',
        'wordclass': 'Adj',
        'Definition': 'Biến cố'
    },

        {
        'name': 'Conceal',
        'wordclass': 'Noun',
        'Definition': 'Che giấu'
    },

        {
        'name': 'Sublime',
        'wordclass': 'Adj',
        'Definition': 'Cao siêu'
    },

        {
        'name': 'Penetration',
        'wordclass': 'Noun',
        'Definition': 'Xâm nhập'
    },

        {
        'name': 'Eager',
        'wordclass': 'Adj',
        'Definition': 'Hăng hái'
    },

        {
        'name': 'Emulate',
        'wordclass': 'Verb',
        'Definition': 'Thi đua'
    },

        {
        'name': 'Deliberate',
        'wordclass': 'Adj',
        'Definition': 'Cố tính'
    },

        {
        'name': '',
        'wordclass': '',
        'Definition': ''
    },

        {
        'name': '',
        'wordclass': '',
        'Definition': ''
    },

        {
        'name': '',
        'wordclass': '',
        'Definition': ''
    },

        {
        'name': '',
        'wordclass': '',
        'Definition': ''
    },

        {
        'name': '',
        'wordclass': '',
        'Definition': ''
    },

        {
        'name': '',
        'wordclass': '',
        'Definition': ''
    },

        {
        'name': '',
        'wordclass': '',
        'Definition': ''
    },

        {
        'name': '',
        'wordclass': '',
        'Definition': ''
    },

        {
        'name': '',
        'wordclass': '',
        'Definition': ''
    },

        {
        'name': '',
        'wordclass': '',
        'Definition': ''
    },

        {
        'name': '',
        'wordclass': '',
        'Definition': ''
    },

        {
        'name': '',
        'wordclass': '',
        'Definition': ''
    },

        {
        'name': '',
        'wordclass': '',
        'Definition': ''
    },

        {
        'name': '',
        'wordclass': '',
        'Definition': ''
    },

        {
        'name': '',
        'wordclass': '',
        'Definition': ''
    },

        {
        'name': '',
        'wordclass': '',
        'Definition': ''
    },

        {
        'name': '',
        'wordclass': '',
        'Definition': ''
    },

        {
        'name': '',
        'wordclass': '',
        'Definition': ''
    },

        {
        'name': '',
        'wordclass': '',
        'Definition': ''
    },

        {
        'name': '',
        'wordclass': '',
        'Definition': ''
    },

        {
        'name': '',
        'wordclass': '',
        'Definition': ''
    },

        {
        'name': '',
        'wordclass': '',
        'Definition': ''
    },

        {
        'name': '',
        'wordclass': '',
        'Definition': ''
    },

        {
        'name': '',
        'wordclass': '',
        'Definition': ''
    },

        {
        'name': '',
        'wordclass': '',
        'Definition': ''
    },

        {
        'name': '',
        'wordclass': '',
        'Definition': ''
    },












]


score = 0


for i in range(10):
    ran_num = random.randint(0,100)
    question =  dicts[ran)] ['Definition']
    answer = 
    print(question)
    Ans = input("> ")

    if Ans == :
        print('You\'re correct')
        score += 1
        run = True
        print(score)
    else:
        print("incorrect")
        print("the answer is " + dicts[ran] ['name'])
        print(score)
