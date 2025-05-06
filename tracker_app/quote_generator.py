import random

Dream = [
'"All our dreams can come true, if we have the courage to pursue them." — Walt Disney',
'"The future belongs to those who believe in the beauty of their dreams." — Eleanor Roosevelt',
'"Dreams come true. Without that possibility, nature would not incite us to have them." — John Updike',
'\"Dream as if you \'ll live forever. Live as if you\'ll die today.\" — James Dean',
'"Some men see things as they are and say why. I dream things that never were and say why not." — George Bernard Shaw',
]

Achieve = [
'\"Show me a person who has never made a mistake and I \'ll show you someone who has never achieved much.\" — Joan Collins',
'\"Failure is the condiment that gives success its flavor.\" — Truman Capote',
'\"Success means doing the best with what we have. Success is the doing, not the getting; in the trying, not the triumph. Success is a personal standard, reaching for the highest that is in us, becoming all that we can be.\" — Zig Ziglar',
'\"I long to accomplish a great and noble task, but it is my chief duty to accomplish small tasks as if they were great and noble.\" — Helen Keller',
'\"A man is a success if he gets up in the morning and gets to bed at night, and in between does what he wants to do.\" — Bob Dylan',
]

Action = [
'\"In a moment of decision, the best thing you can do is the right thing to do, the next best thing is the wrong thing, and the worst thing you can do is nothing.\" — Theodore Roosevelt',
'\"Amateurs sit and wait for inspiration, the rest of us just get up and go to work.\" — Stephen King',
'\"You will never plough a field if you only turn it over in your mind.\" — Irish proverb',
'\"Take the first step in faith. You don\'t have to see the whole staircase, just take the first step.\" — Martin Luther King, Jr.',
'\"Don\'t wait. The time will never be just right.\" — Napoleon Hill',
]

Challenge = [
'\"Strength does not come from winning. Your struggles develop your strengths. When you go through hardships and decide not to surrender, that is strength." — Arnold Schwarzenegger',
'\"When you get into a tight place and everything goes against you, till it seems as though you could not hang on a minute longer, never give up then, for that is just the place and time that the tide will turn.\" — Harriet Beecher Stowe',
'\"The best way out is always through.\" — Robert Frost',
'\"It is not the critic who counts; not the man who points out how the strong man stumbles, or where the doer of deeds could have done better. The credit belongs to the man who is actually in the arena, whose face is marred by dust and sweat and blood ... who at the worst, if he fails, at least fails while daring greatly, so that his place shall never be with those cold and timid souls who neither know victory nor defeat.\" — Theodore Roosevelt.',
'\"The greater the obstacle, the more glory in overcoming it.\" — Molière',
]

discipline = [
    "\"Discipline is the bridge between goals and accomplishment.\" — Jim Rohn",
    "\"We do today what they wont, so tomorrow we can accomplish what they can’t.\" — Dwayne Johnson",
    "\"Without self-discipline, success is impossible, period.\" — Lou Holtz",
    "\"Discipline is choosing between what you want now and what you want most.\" — Abraham Lincoln",
    "\"The pain of self-discipline will never be as great as the pain of regret.\" — Unknown",
    "\"What lies in our power to do, lies in our power not to do.\" — Aristotle",
    "\"Success begins with self-discipline.\" — Sunday Adelaja",
    "\"Self-discipline is the magic power that makes you virtually unstoppable.\" — Dan Kennedy",
    "\"With self-discipline most anything is possible.\" — Theodore Roosevelt",
    "\"Discipline is remembering what you want.\" — David Campbell",
    "\"Discipline is the foundation upon which all success is built.\" — Jim Rohn",
    "\"Freedom is not attained by the satisfaction of desires, but by the removal of desire.\" — Epictetus",
    "\"He who cannot obey himself will be commanded.\" — Friedrich Nietzsche",
    "\"The more I discipline myself, the easier life becomes.\" — Steve Pavlina",
    "\"A disciplined mind leads to happiness, and an undisciplined mind leads to suffering.\" — Dalai Lama"
]

focus = [
    "\"Starve your distractions. Feed your focus.\" — Unknown",
    "\"Where focus goes, energy flows.\" — Tony Robbins",
    "\"The successful warrior is the average man, with laser-like focus.\" — Bruce Lee",
    "\"It’s not always that we need to do more but rather that we need to focus on less.\" — Nathan W. Morris",
    "\"Focus on being productive instead of busy.\" — Tim Ferriss",
    "\"You can’t depend on your eyes when your imagination is out of focus.\" — Mark Twain",
    "\"Concentrate all your thoughts upon the work at hand. The sun's rays do not burn until brought to a focus.\" — Alexander Graham Bell",
    "\"Lack of direction, not lack of time, is the problem. We all have 24-hour days.\" — Zig Ziglar",
    "\"You will never reach your destination if you stop and throw stones at every dog that barks.\" — Winston Churchill",
    "\"The ability to focus attention on important things is a defining characteristic of intelligence.\" — Robert J. Shiller",
    "\"Success demands singleness of purpose.\" — Vince Lombardi",
    "\"Multitasking is the ability to screw everything up simultaneously.\" — Jeremy Clarkson",
    "\"It is those who concentrate on but one thing at a time who advance in this world.\" — Og Mandino",
    "\"Your focus determines your reality.\" — George Lucas",
    "\"Do not dwell in the past, do not dream of the future, concentrate the mind on the present moment.\" — Buddha"
]

motivation = [
    "\"The best way to get started is to quit talking and begin doing.\" — Walt Disney",
    "\"Push yourself, because no one else is going to do it for you.\" — Unknown",
    "\"Great things never come from comfort zones.\" — Roy T. Bennett",
    "\"Dream big and dare to fail.\" — Norman Vaughan",
    "\"Don’t watch the clock; do what it does. Keep going.\" — Sam Levenson",
    "\"Opportunities don't happen. You create them.\" — Chris Grosser",
    "\"Your time is limited, so don’t waste it living someone else’s life.\" — Steve Jobs",
    "\"Hardships often prepare ordinary people for an extraordinary destiny.\" — C.S. Lewis",
    "\"You miss 100% of the shots you don't take.\" — Wayne Gretzky",
    "\"Do something today that your future self will thank you for.\" — Sean Patrick Flanery",
    "\"Believe you can and you're halfway there.\" — Theodore Roosevelt",
    "\"Success is what comes after you stop making excuses.\" — Luis Galarza",
    "\"Everything you’ve ever wanted is on the other side of fear.\" — George Addair",
    "\"The harder you work for something, the greater you'll feel when you achieve it.\" — Unknown",
    "\"Act as if what you do makes a difference. It does.\" — William James"
]

success = [
    "\"Success is the sum of small efforts, repeated day in and day out.\" — Robert Collier",
    "\"Don’t aim for success if you want it; just do what you love and believe in, and it will come naturally.\" — David Frost",
    "\"Success usually comes to those who are too busy to be looking for it.\" — Henry David Thoreau",
    "\"There are no secrets to success. It is the result of preparation, hard work, and learning from failure.\" — Colin Powell",
    "\"The road to success and the road to failure are almost exactly the same.\" — Colin R. Davis",
    "\"Success is not the key to happiness. Happiness is the key to success. If you love what you are doing, you will be successful.\" — Albert Schweitzer",
    "\"The only place where success comes before work is in the dictionary.\" — Vidal Sassoon",
    "\"Success is not in what you have, but who you are.\" — Bo Bennett",
    "\"Success isn’t just about what you accomplish in your life; it’s about what you inspire others to do.\" — Unknown",
    "\"Don’t be afraid to give up the good to go for the great.\" — John D. Rockefeller",
    "\"I never dreamed about success. I worked for it.\" — Estée Lauder",
    "\"Success is walking from failure to failure with no loss of enthusiasm.\" — Winston Churchill",
    "\"Success does not consist in never making mistakes but in never making the same one a second time.\" — George Bernard Shaw",
    "\"Success is how high you bounce when you hit bottom.\" — George S. Patton",
    "\"To be successful, you must act big, think big and talk big.\" — Aristotle Onassis",
    "\"Success seems to be connected with action. Successful people keep moving. They make mistakes but they don't quit.\" — Conrad Hilton",
    "\"The secret of success is to do the common thing uncommonly well.\" — John D. Rockefeller Jr.",
    "\"Success isn’t owned. It’s leased. And rent is due every day.\" — J.J. Watt",
    "\"Success is not about luck. It’s about hard work, perseverance, learning, studying, sacrifice and most of all, love of what you are doing.\" — Pele",
    "\"Success is more permanent when you achieve it without destroying your principles.\" — Walter Cronkite",
    "\"Success is the progressive realization of a worthy goal or ideal.\" — Earl Nightingale",
    "\"Success is liking yourself, liking what you do, and liking how you do it.\" — Maya Angelou",
    "\"Success is no accident. It is hard work, perseverance, learning, studying, sacrifice and most of all, love of what you are doing.\" — Pelé",
    "\"Behind every successful person lies a pack of haters.\" — Eminem",
    "\"Strive not to be a success, but rather to be of value.\" — Albert Einstein",
    "\"Some people dream of success, while others wake up and work hard at it.\" — Napoleon Hill",
    "\"The difference between successful people and very successful people is that very successful people say 'no' to almost everything.\" — Warren Buffett",
    "\"Success is achieved and maintained by those who try and keep trying.\" — W. Clement Stone",
    "\"Success is about creating value.\" — Candice Carpenter",
    "\"Success is doing ordinary things extraordinarily well.\" — Jim Rohn"
]


Persistence = [
'\"The man who moves a mountain begins by carrying away small stones.\" — Confucius',
'\"Failure is success in progress." — Albert Einstein',
'\"If you\'re walking down the right path and you\'re willing to keep walking, eventually you\'ll make progress.\" — Barack Obama',
'\"Without continual growth and progress, such words as improvement, achievement and success have no meaning.\" — Benjamin Franklin',
'\"Great things are not done by impulse, but by a series of small things brought together.\" — Vincent Van Gogh'
]

# while True:
Quotes = [Dream, Achieve, Action, Challenge, discipline, focus, motivation, success, Persistence]

def Quote_Generator():
    print("Welcome to quote generator")
    print("Kindly choose '1' for Dream quote")
    print("Kindly choose '2' for Achieve quote")
    print("Kindly choose '3' for Action quote")
    print("Kindly choose '4' for Challenge quote")
    print("Kindly choose '5' for Persistent quote")
    while True:
        try:
            user_input = int(input("Pick a number between 1 and 9 to choose your type of quote: ")) - 1
            if 0 <= user_input <= 8:
                return user_input
            else:
                print("Pick a number between 1 and 9")
        except:
            print("Pick a number between 1 and 9 using digits")

def Quote_Selector(user_input):
    selected_quote = Quotes[user_input]
    Quote = random.choice(selected_quote)
    return Quote

def main():
    while True:
        user_input = Quote_Generator()
        Quote = Quote_Selector(user_input)
        
        print()
        print(f"Quote: {Quote}")
        

        print()
        print("Do you want to hear more quotes")
        user_input_2 = input("Type (Y) for Yes or (N) for No: ")
        print()

        if user_input_2.lower() == 'n':
            print("Have a lovely day")
            break
        
# main()