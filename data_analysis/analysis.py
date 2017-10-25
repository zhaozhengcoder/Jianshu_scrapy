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
    Show.show_top_author(new_merge_list)


#显示文字数量最高的作者
def top_articles_num(top_num=20):
    sql='select uid,nickname,articles_num from jianshu_user order by articles_num desc  limit {top_num};'.format(top_num=top_num)
    top_articles=DB.db_select(sql)
    print (top_articles)



#显示文字数/被喜欢数最高的作者
def top_articles_per_beliked(top_num=20):
    sql=" select uid,nickname, beliked_num, words_num ,beliked_num/words_num as new1 from jianshu_user order by new1 desc limit {top_num};".format(top_num=top_num)
    articles_per_beliked=DB.db_select(sql)
    print (articles_per_beliked)

#用户按照粉丝比例的分布
def follower_distribution(follower_num=1000):
    sql="  select count(*) from jianshu_user where follower_num > {follower_num} ;".format(follower_num=follower_num)
    distribution=DB.db_select(sql)
    print (distribution)
    print (distribution[0][0])
    return distribution[0][0]

def analysis_distribution():
    sql="select count(*) from jianshu_user ;"
    total_user_count=DB.db_select(sql)[0][0]
    dis_dict={}
    follower_num=1000
    dis_dict[follower_num]=follower_distribution(follower_num)
    follower_num=2000
    dis_dict[follower_num]=follower_distribution(follower_num)
    follower_num=4000
    dis_dict[follower_num]=follower_distribution(follower_num)
    follower_num=5000
    dis_dict[follower_num]=follower_distribution(follower_num)
    follower_num=10000
    dis_dict[follower_num]=follower_distribution(follower_num)
    follower_num=20000
    dis_dict[follower_num]=follower_distribution(follower_num)
    for key in dis_dict:
        print (key , "  ",dis_dict[key])


#to-do  timeline


#to-do 用户1 到用户2 的距离


if __name__=='__main__':
    #top_author()
    #top_articles_num()
    #top_articles_per_beliked()
    #follower_distribution()
    analysis_distribution()

