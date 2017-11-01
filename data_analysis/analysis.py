import Config
import DB
import Show


#统计粉丝数和被喜欢数目最高的作者
def top_author(top_num=50):
    sql='select uid,nickname,follower_num, beliked_num from jianshu_user order by follower_num desc  limit {top_num};'.format(top_num=top_num)
    follow_list=DB.db_select(sql)
    sql='select uid,nickname,follower_num ,beliked_num from jianshu_user order by beliked_num desc  limit {top_num};'.format(top_num=top_num)
    beliked_list=DB.db_select(sql)
    
    merge_list=[]
    merge_list.extend(follow_list)
    merge_list.extend(beliked_list)
    merge_set=set(merge_list)
    new_merge_list=list(merge_set)
    #show nickanme
    for item in new_merge_list:
        print (item)
    Show.show_top_author(new_merge_list)


#显示文字数量最高的作者
def top_articles_num(top_num=20):
    sql='select uid,nickname,articles_num from jianshu_user order by articles_num desc  limit {top_num};'.format(top_num=top_num)
    top_articles=DB.db_select(sql)
    #print (top_articles)
    for item in top_articles:
        print (item[1],end=',')



#显示文字数/被喜欢数最高的作者
def top_articles_per_beliked(top_num=20):
    sql=" select uid,nickname, beliked_num, words_num ,beliked_num/words_num as new1 from jianshu_user order by new1 desc limit {top_num};".format(top_num=top_num)
    articles_per_beliked=DB.db_select(sql)
    #print (articles_per_beliked)
    for item in articles_per_beliked:
        print (item[1],end=',')


def follower_distribution(item_list):
    sql="select count(*) from jianshu_user where follower_num > {follower_num1} and follower_num < {follower_num2};".format(follower_num1=item_list[0],follower_num2=item_list[1])
    print (sql)
    distribution=DB.db_select(sql)
    #print (distribution)
    print (distribution[0][0])
    return distribution[0][0]

#用户按照粉丝比例的分布
def analysis_following_distribution():
    range_num=[[0,10],[10,20],[20,30],[30,40],[40,50],[50,100],[100,200],[200,500],[500,1000],[1000,2000],[2000,5000],[5000,10000],[10000,20000]]
    result=[]
    for item in range_num:
        result.append(follower_distribution(item))
    print (result)


def analysis_beliked_distribution():
    pass



if __name__=='__main__':
    #top_author(20)
    #top_articles_num()
    #top_articles_per_beliked()
    analysis_following_distribution()

