#Homework #5
import praw
import random
import time
import datetime
import traceback

# this is the login information for our bot
username='BotForCS'
password='kisskiss123'
client_id='hEc7tn14KiMDSQ'
client_secret='yDW6bUzDb5t-XQtWbMYvJbNRSS4'
user_agent='CS40_Bot'

# connect to reddit 
reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent,
    username=username,
    password=password
    )

count = 0
upvote_count = 0
rep_count = 0
top_auths = []

against=['Bernie', 'Donald','Trump','Donald Trump', 'Sanders','Kamala','Kamala Harris','Beth','Warren','Castro']
bad=['terrible','not right','idiotic','a loser','crazy','power hungry']
forr= ['YANG #YANGGANG','Andrew Yang','Yang','Mayor Pete','BootEdgeEdge','Mayor BootyBooty','Pete']
good= ['smart','innovative','fresh','an entrepeneuer','a savior']
screw= ['SCREW','F&@%','I hate','No one likes','No one should support']
collective= ['We are','The American People are','The People are','Americans are']
support=['for','with', 'standing behind','in support of','loving']
platform=['the American Way','Gun Control','my freedom','all of us']

pattern1 = '<AGAINST> is <BAD>. <FORR> is <GOOD>. Have you seen the policies? They will right America economically and socially'
pattern2 = '<SCREW> <AGAINST>. <COLLECTIVE> <SUPPORT> <FORR>!'
pattern3 = '<AGAINST> doesn\'t know what <FORR> stands for. It\'s ridiculous how people just accept what\'s said. DO YOUR RESEARCH PEOPLE. He stands for <PLATFORM>.'
pattern4 = '<COLLECTIVE> <SUPPORT> <FORR>. NOT <AGAINST>.'
pattern5 = 'The only way to describe the other candidates is <BAD>. <COLLECTIVE> <SUPPORT> <FORR>!'
patterns = [pattern1,pattern2,pattern3,pattern4,pattern5]

with open ('index.html', 'w') as f:
    code = ('<head>'+
            '<meta name="description" content="This will outline my favorite things that bots posted.">'+
            '<title> HW #5 Bots </title>' +
            '<h1> Bot Project</h1>' +
            
            '<p> I wrote my bot to be writing posts in support of  both Pete Butigege and Andrew Yang</p>' +
            '<h3> My favorite discussion: </h3> <a href="https://www.reddit.com/r/csci040/comments/e33zyy/plagerized_from_rpete_buttigieg_its_crazy_how/f91pqdc?utm_source=share&utm_medium=web2x"> Comment UPDATE Thread</a> <br> <img src="commentphoto.png" alt="Bot conversation screenshot.">'+
            '<p> My favorite conversation was the image above because the bots are all talking about different candidates and taking postitions that have nothing to do with eachother.' +
            ' I think that this is sometimes representative of the real world to because sometimes people just outta nowhere come up with a nother argument that doesn\'t always ' +
            'have to do with the conversation at hand.'
            '<h3> My Score should be: </h3>' +
            '<p> 90 for the base assignment, 5 for upvoting each comment, 5 for writing over 200 comments, 10 for posting 20 plagerized submissions leading to a ' +
            'total of <strong>110/100</strong> points.</p>')
    
    f.write(code)
    print('Website written')

    
    

while True:
    try:
        result = random.choice(patterns)
        result = result.replace('<AGAINST>',random.choice(against))
        result = result.replace('<BAD>',random.choice(bad))
        result = result.replace('<FORR>',random.choice(forr))
        result = result.replace('<GOOD>',random.choice(good))
        result = result.replace('<SCREW>',random.choice(screw))
        result = result.replace('<COLLECTIVE>',random.choice(collective))
        result = result.replace('<SUPPORT>',random.choice(support))
        result = result.replace('<PLATFORM>',random.choice(platform))
        text = result + ' (i\'m a bot btw)'
        
        r = reddit.subreddit('csci040')
        subred = list(r.hot())
        sub = random.choice(subred)

        
        plagerized = list(reddit.subreddit('Pete_Buttigieg').hot())
        
        
        print('new iteration at:',str(datetime.datetime.now()))
        print(sub)
    #(task 2): get a list of all of the comments in the submission
        comments = []
        comments=sub.comments.list()

    
        #post new submission
        p_title = random.choice(plagerized).title
        p_text = random.choice(plagerized).selftext
        r.submit(title = 'Plagiarized from r/Pete_Buttigieg ' + p_title, selftext = p_text)
        print('Posted New')

        #Make author's list
        auths = []
        topcoms = list(sub.comments)
        for com in topcoms:
            auths.append(str(com.author))

        x = 1
        for auth in auths:
            if username not in auths:
                x = 1
            if username in auths:
                x = 0
        if x == 0:
            sub.reply(text)
            print('Posted top comment')
                

        
        for com in comments:
            if 'pete' in str(com.body).lower():
                com.upvote()
                print('upvoted')
                upvote_count += 1

        
        # HINT1: there is a one-line command in the praw quick-start guide
        # that accomplishes this task.
        # HINT2: whenever we work on a program, you need to somehow check that the
        # things your programming is doing are correct.  In this case, one thing
        # we can do is to check the length of the comments variable.
        # You should manually ensure that the printed length is the same as the
        # length displayed on reddit.  If it's not, then there are some comments
        # that you are not correctly identifying, and you need to figure out
        # which comments those are and how to include them.

        print('len(comments)=',len(comments))

        if len(comments) == 0:
            print('len(comments)=',len(comments))
            sub.reply(text)
            print('Length was 0, I posted')
            print('len(comments)=',len(comments))
            
        
        # FIXME (task 3): filter comments to remove comments that were generated by your bot
        not_my_comments=[]
        for com in comments:
            if username not in str(com.author):
                not_my_comments.append(com)
        # HINT1: completing this task requires only a single for loop and a single if statement.
        # The PRAW quick-start guide has the contents of the for loop/if statement.
        # HINT2: as before, you need to check that your code is working somehow.
        # reddit does not provide any list of comments generated by your bot,
        # but you can easily check this number manually by subtracting the number
        # of comments you know you've posted from the number above.
        print('len(not_my_comments)=',len(not_my_comments))
        

        # FIXME (task 4): filter the list to also remove comments that you've already replied to
        comments_without_replies=[]
        x = 0
        for com in not_my_comments:
            x = 0
            for rep in com.replies:
                if username in str(rep.author):
                    x = 1
            if x == 0:
                comments_without_replies.append(com)
                
        # HINT1: completing this task requires only a single for loop and a single if statement.
        # The PRAW quick-start guide has the contents of the for loop/if statement.
        # HINT2: again, you need to check that this is working
        if len(comments_without_replies) == 0:
            print('Sleeping. Out of comments to reply to')
        print('len(comments_without_replies)=',len(comments_without_replies))
        

        # FIXME (task 5): randomly select one of the comments that we haven't replied to yet
        # HINT: There is a function in python's random module for doing this.
        # See the documentation at https://docs.python.org/3/library/random.html
        
        comment1 = random.choice(comments_without_replies)
        
        

        # FIXME (task 7): post a reply to the selected comment
        # HINT: We covered how to do this in class on 12 Nov.
        # See the reddit.py lecture notes or the PRAW quick start guide.
        comment1.reply(text)
        '''
        for com in comments:
            if len(com.replies) == 0:
                print('No Replies, Commenting')
                com.reply(text)
        '''
        
        
        # FIXME (task 8): check all submissions in the /r/csci040 subreddit to see if your
        # bot has not created a top-level comment in that submission.  If it has not,
        # then create a top-level comment.
        # HINT1: The PRAW quick-start guide contains all the information you need to know
        # about PRAW to complete this task.
        # HINT2: The code for this task will have to be placed in multiple places throughout
        # this file.
        
        # sleep for 10-15 minutes so that you don't overload reddit
        count+=1
        print('count = ', count)
        print('upvotes = ', upvote_count)
        print('Sleeping at end. Will comment again. \n\n\n\n\n')
        time.sleep(10*60)
    except Exception:
        traceback.print_exc()
        print('count = ', count)
        print('upvotes = ', upvote_count)
        print('Slight error occured\n\n\n\n\n')
        time.sleep(10*60)
        
        #time.sleep(10*60+random.randrange(5*60))
    
    

